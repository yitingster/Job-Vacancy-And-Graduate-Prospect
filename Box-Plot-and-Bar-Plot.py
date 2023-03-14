import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

f = "C:/Users/Yi Ting/Desktop/CA2/Data/graduate-employment-survey-ntu-nus-sit-smu-suss-sutd.csv"
raw = pd.read_csv(f, header = 0, na_values=['-','NA', 'N/A', 'na'], encoding='latin-1')

####################################################################
### 1. Importing Graduate Employment Dataset and Overview ####

### Graduate Employment Dataset Overview ####
print("***Local University Graduate Employment Dataset Overview***")

#shape
print("The shape of the data is {}".format(raw.shape))

#Index - Year range of the dataset
print("The dataset is from the year of {} to {}".format(
    raw.year.min(),raw.year.max()))

#Columns
print("The columns are: {}".format(list(raw.columns)))
print()

#Checking for Missing Values
print('***Number of non NA Values***')
print(raw.count())
print()

#Summary of dataset
print("***Summary of Local University Graduate Employment Dataset:***")
print(raw.info())
print()

#Descriptive Statistic of dataset
print("***Descriptive Statistic of Local University Graduate Employment Dataset:***")
print(raw[['employment_rate_overall','gross_monthly_mean']].describe())


####################################################################
#### 2. Data Sorting and Graph Plotting ####

#Creating Shortform for University in a new column university2
uni = raw['university'].tolist()
uni = pd.unique(uni)
shortform = ['NTU', 'NUS', 'SMU', 'SIT', 'SUTD', 'SUSS']
uni_short = dict(zip(uni,shortform))
raw['university2'] = raw['university'].replace(uni_short,regex = True)

#Extract latest year 2018 data
uni_2018 = raw[raw['year']==2018]

#boxplot
ax = sns.boxplot(x="university2", y="gross_monthly_mean", 
                    data= uni_2018, hue = "university2")

ax.set(xlabel="University", ylabel = "Mean Gross Monthly Income")
ax.set_title('Mean Gross Monthly Income of Local University Graduates in 2018')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles, labels=labels, 
          title="University", bbox_to_anchor=(1, 1), loc=2)

#### Plot 2 ####
#Extract relevant data - year, employment rate and unniversity
raw2 = raw.loc[:,['year','employment_rate_overall','university2']]

#Groupby year and university
bar2 = raw2.groupby(['year','university2']).mean()
bar2.reset_index(inplace = True)

#Barplot
fig, ax2 = plt.subplots()
fig = sns.barplot(x="year", y="employment_rate_overall", data=bar2, hue = 'university2')
ax2.set(xlabel="year", ylabel = "employment rate (%)")
ax2.set_title('Employment Rate of Local University Graduates from 2013-2018')
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles=handles, labels=labels, 
          title="University", bbox_to_anchor=(1, 1), loc=2)
plt.show()

