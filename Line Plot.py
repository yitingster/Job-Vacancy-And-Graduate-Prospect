import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

####################################################################
### 1. Importing Job Vacancy by Industry Dataset and Overview ####

f = "C:/Users/Yi Ting/Desktop/CA2/Data/job-vacancy-by-industry-level-2.csv"
raw = pd.read_csv(f, header = 0, na_values=['-','NA', 'N/A'])

### Job Vacancy Dataset Overview ####
print("***Job Vacancy by Industry Dataset Overview***")

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
print("***Summary of Job Vacancy by Industry Dataset:***")
print(raw.info())
print()

#Descriptive Statistic of dataset
print("***Descriptive Statistic of Job Vacancy by Industry Dataset:***")
print(raw.describe())

####################################################################
#### 2. Data Sorting and Graph Plotting ####

#remove data column not used
raw2 = raw.drop(columns = 'industry2')

#Combining data by industry using groupby
df = raw2.groupby(['year','industry1']).sum()
df.reset_index(inplace = True)

#Line Graph 
palette = sns.color_palette("mako_r", 4)

fig, ax = plt.subplots()
fig = sns.lineplot(data=df, x="year", y="job_vacancy", style = 'industry1',
             markers=True, hue="industry1", palette=palette)

ax.set(xlabel="year", ylabel = "Job Vacancy")
fig.set_title('Line Plot of Job Vacancy by Industry from 1990 to 2019')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[1:], labels=labels[1:], 
          title="Industry", bbox_to_anchor=(1, 1), loc=2)
plt.show()


