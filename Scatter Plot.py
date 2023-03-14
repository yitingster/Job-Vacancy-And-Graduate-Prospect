
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

####################################################################
### 1. Importing Job Vacancy Dataset and Overview ####

f = "C:/Users/Yi Ting/Desktop/CA2/Data/job-vacancy-topline.csv"
raw_job = pd.read_csv(f, header = 0, index_col = 'year')
raw_job.index.astype(int)

### Job Vacancy Dataset Overview ####
print("***Job Vacancy Dataset Overview***")

#shape
print("The shape of the data is {}".format(raw_job.shape))

#Index - Year range of the dataset
print("The Job Vacancy data is from the year of {} to {}".format(
    raw_job.index.min(),raw_job.index.max()))

#Columns
print("The columns are: {}".format(list(raw_job.columns)))

#Checking for NA Values
if True in raw_job.isnull():
    print("There are missing values.")
else:
    print("There are no missing values.")   
print()

#Summary of dataset
print("***Summary of Job Vacancy Dataset:***")
print(raw_job.info())
print()

#Descriptive Statistic of dataset
print("***Descriptive Statistic of Job Vacancy Dataset:***")
print(raw_job.describe())

print('________________________________________________________________')


####################################################################
#### 2. Importing GDP Dataset and Overview ####

f_path = "C:/Users/Yi Ting/Desktop/CA2/Data/per-capita-gni-and-per-capita-gdp-at-current-prices-annual.csv"
raw_gdp = pd.read_csv(f_path, header = 0, names = ['year', 'type', 'value'], index_col = 'year')
raw_gdp.index.astype(int)

#Extract GDP data
gdp = raw_gdp[raw_gdp['type'] == 'Per Capita GDP' ]

### GDP Dataset Overview ####
print("***GDP Dataset Overview***")

#shape
print("The shape of the data is {}".format(gdp.shape))

#Index - Year range of the dataset
print("The GDP data is from the year of {} to {}".format(
    gdp.index.min(),gdp.index.max()))

#Columns
print("The columns are: {}".format(list(gdp.columns)))

#Checking for NA Values
if True in gdp['value'].isnull():
    print("There are missing values.")
else:
    print("There are no missing values.")   
print()

#Summary of dataset
print("***Summary of GDP Dataset:***")
print(gdp.info())
print()

#Descriptive Statistic of dataset
print("***Descriptive Statistic of GDP Dataset:***")
print(gdp.describe())

####################################################################
#### 3. Data Sorting and Graph Plotting ####

#Exclude data from 2019 for job vacancy dataset
job = raw_job[0:-1]


#Extract data from year 1990-2018 and only value for GDP dataset
gdp2 = gdp.loc[1990:2018,:]['value']

#Combining two data
combined = pd.merge(job,gdp2, how = 'left', on = 'year')
combined.reset_index(inplace = True)

### Plotting Scatter Plot ####
fig = sns.scatterplot(data=combined, x="value", y="job_vacancy", hue = "year", size="year",
                sizes = (20,200))
fig.set(xlabel="Current GDP per capita (SGD)", ylabel = "Job Vacancy")
fig.set_title('Scatter plot of Job Vacancy vs Current GDP per capita')
plt.legend(bbox_to_anchor=(1, 1), loc=2) 
plt.show()


