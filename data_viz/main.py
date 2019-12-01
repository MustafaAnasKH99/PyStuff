import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]

sample_data = pd.read_csv('countries.csv')
 

china = sample_data[sample_data.country == 'China']
us = sample_data[sample_data.country == 'United States']

plt.plot(us.year, us.population / 10 ** 6)
plt.plot(china.year, china.population / 10 ** 6)
plt.legend(['USA', 'China'])
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()


# plt.plot(x, y)
# plt.plot(x, z)
# plt.title('TESTING')
# plt.xlabel("X")
# plt.ylabel("Y and Z")

# plt.legend(["this is y", "this is z"])

plt.show()