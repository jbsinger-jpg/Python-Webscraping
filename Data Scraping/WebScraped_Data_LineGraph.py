import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Visualization
# Does the operating speed of a graphics card correlate with its price?
sample_data = pd.read_csv("C:/Users/jacob/PycharmProjects/Tutorial/Pandas Conversion - WebOut - webOut.csv")
plt.plot(sample_data.Price, sample_data.Core_Clock_MHz, 'x:b', scaley=False)  # scaley overrides pyplot
                                                                              # auto-scaling feature

i = 0
y_list = list()
x_list = list()

while i < 3000:
    y_list.append(i)
    i += 100

i = 0
while i < 2500:
    x_list.append(i)
    i += 500

plt.yticks(y_list)
plt.xticks(x_list)

plt.xlabel("Price in USD ($)")
plt.ylabel("Core Clock (MHz)")

grid = sns.lmplot(x='Price', y='Core_Clock_MHz', data=sample_data, fit_reg=True)
grid.set(xticks=x_list, yticks=y_list, ylim=(0, 3000))
plt.show()
# Final Analysis
# For the majority of the GCs the price/performance ratio does seem to correlate
