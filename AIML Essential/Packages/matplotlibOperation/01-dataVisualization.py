# graphs for your data: univariate / bivariate 

# tools / packages do data visualization: 

# matplotlib 
# seaborn 
# pandas 
# plotly 

# features --- > Nothing but the columns 

# individually study each feature is called as univariate analysis 
# studying the data between various features are called as bivariate analysis

# let's make a graph for annual income : univariate


import pandas as pd
import matplotlib as plt

data = pd.read_csv('Mall_Customers.csv')
print(data.head())
plt.plot(data['Annual Income (k$) '])
plt.show()