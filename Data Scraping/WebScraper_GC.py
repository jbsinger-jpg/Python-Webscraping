from urllib.request import urlopen as uReq  # alias
from bs4 import BeautifulSoup as soup  # alias
import re


def changeUrl(url, pageNum):
    url = url[0:url.find("page=") + len("page=")]  # takes pages num with more than 1 digit into consideration
    next_url = url + str(pageNum)
    return next_url


def removeInvalidColumnNames(column_names_all, attrs_in_file):
    i = 0  # index for all column attributes
    j = 0  # index where match not found

    while i < len(column_names_all):
        if j < len(attrs_in_file):
            match = re.match(column_names_all[i], attrs_in_file[j])
            if match:
                j += 1
        i += 1

    if match is None and i == len(column_names_all):
        attrs_in_file.pop(j)


def fillMissingInfo(file_in, file_out):
    file_out = open("webOut.txt", "a")
    file_contents = list()

    attributes_all = ["Card Dimensions (L x H):", "Core Clock:", "Gaming Mode (Default):", "DVI:",
                      "DisplayPort:", "HDMI:", "Item #:", "Max Resolution:", "Model #:", "Name:", "Price:",
                      "Return Policy:", "Slot Width:"]  # columns in table
    attributes_all.sort()
    file_in.seek(0)  # bring pointer back to beginning of file
    attrs_in_file = file_in.readlines()  # attrs_in_file = array (elements determined by "\n" in loopThroughPages())
    attrs_in_file.sort()
    print(attrs_in_file)

    file_contents.clear()
    for attr in attrs_in_file:
        attr = re.sub("\n", "", attr)
        file_contents.append(attr)

    removeInvalidColumnNames(attributes_all, file_contents)
    i = 0
    while i < len(attributes_all):
        match = re.match(attributes_all[i], file_contents[i], re.IGNORECASE)
        if match:
            file_contents.append(" ")  # keeps list from giving index error

            # IF WANTING TO REMOVE COLUMN NAMES UNCOMMENT LINE BELOW
            # file_contents[i] = re.sub(attributes_all[i], "", file_contents[i])
        else:
            file_contents.insert(i, " ")  # make field non-existent
        i += 1
    i = 0
    while len(attributes_all) < len(file_contents):
        file_contents.pop(-1)  # remove entries where match is found
        i += 1
    print(file_contents)
    i = 0

    while i < len(file_contents):  # don't append comma to last entry in file
        if i < (len(file_contents) - 1):
            file_out.write(file_contents[i] + ",")
        else:
            file_out.write(file_contents[i])
        i += 1

    file_out.write("\n")  # set values to be generated for new entry
    file_out.close()


def loopThroughPages(my_url, currPage, totalPageAmount):
    while currPage <= totalPageAmount:
        page = uReq(my_url)
        page_html = page.read()
        # print(page_html) # decoded html
        page.close()

        page_soup = soup(page_html, "html.parser")  # makes html usable for python commands
        containers = page_soup.findAll("div", {"class": "item-container"})

        for container in containers:
            name = container.a.img['alt']
            prices = container.findAll("ul", {"class": "price"})

            try:
                price = prices[0].text  # text inherited from parent in HTML code
            except IndexError:  # if tag doesn't exist for product
                pass

            file = open("webScraper.txt", "w+")

            print("Name: " + name)
            name = re.sub(",", " ", name)
            file.write("Name: " + name + "\n")  # attr for in_file

            # reformat with indexing
            price = price[price.find("$"):(price.find(".") + 3)]
            print("Price: " + price)
            price = re.sub(",", "", price)
            file.write("Price: " + price + "\n")  # attr for in_file

            try:
                info = container.findAll("div", {"class": "item-info"})[0]
                i = 0
                item_features = info.findAll("ul", {"class": "item-features"})[0].contents

                while i < len(item_features):

                    if item_features[i].text == "Return Policy: View Return Policy":
                        policy = "Return Policy: Varies"
                        print(policy)
                        file.write(policy + "\n")  # attr for in_file
                    else:
                        print(item_features[i].text)
                        item = str(item_features[i].text)
                        item = re.sub(",", " ", item)
                        file.write(item + "\n")  # attr for in_file
                    i += 1

            except IndexError:
                pass

            file_out = open("webOut.txt", "a")
            fillMissingInfo(file_in=file, file_out=file_out)
            print("\n")
            file.write("\n")
            file.close()
            file_out.close()
        currPage += 1
        # print(currPage)
        my_url = changeUrl(my_url, currPage)
        # print(my_url)


loopThroughPages("https://www.newegg.com/p/pl?d=graphics+cards&page=1", 1, 2)

