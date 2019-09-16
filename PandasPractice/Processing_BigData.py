
import pandas as pd

#read in the data set
url = 'https://raw.githubusercontent.com/sabidi1/BigData/master/PandasPractice/GlobalTemperatures.csv'

temperatures = pd.read_csv(url)
#display the first 50 data entries
temperatures.head(50)


#json = pd.read_json('https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json')
#json.tail(50)
#json.shape

#last 50 entries/rows.
temperatures.tail(50)

temperatures['LandAverageTemperature'].describe()

temperatures['LandMaxTemperature'].describe()

temperatures['LandAndOceanAverageTemperature'].describe()

temperatures[['LandMaxTemperature','LandAndOceanAverageTemperature']]

temperatures[0:10]

#Select a subset of rows
temperatures.iloc[1:10, 1:4]

#select a subset of columns
temperatures.loc[1:10,['LandAverageTemperature', 'LandMaxTemperature' ]]

#filter data and show first 50 entries
temperatures[temperatures.LandAverageTemperature > 4].iloc[:50]                                         

#find  all entries with missing values. Display the first 10 entries.
null_data = temperatures[temperatures.isnull().any(axis = 1)]
print(temperatures.iloc[:10])

#Where temperature > 2, then set it equal to 4.66
temperatures.loc[temperatures['LandAverageTemperature'] > 2, 'LandAverageTemperature'] = 4.66
temperatures[0:10]

#Sort Data in descending order
temperatures.sort_values(by='LandAverageTemperatureUncertainty', ascending=False)

#Group Data
groupData = temperatures.groupby('LandAverageTemperature')
groupData.first()