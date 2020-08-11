# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # 2030ICT/7030ICT
# ## Introduction to Big Data Analytics
# Assignment Specifications Part 1
# 
# Group Submission - Louise Howard, Caleb Davis, Mark English
# 
# 
# %% [markdown]
# ## Section 1 - Data Analysis & Interpretation
# 
# Part 1 - Analyse by Comparison
# 
# Choose your two favourite cities/locations. We will explore the difference between them by answering the following questions:
# 
# Sydney and Brisbane

# %%
# import all libraries required in the code
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# read in the data from the supplied assignment file and check input via table 
df = pd.read_csv("data_assignment.csv")


# %%
# Describe the dataset (e.g.: type of column, value range)
# How many rows (first # outputted) and columns are in the dataset
print(f'Describe the dataset:')
print(f'Shape {df.shape},')
print(f'Column Headers {df.columns}')

# This can be deleted later as using for information on table c


# %%
# Which city has more jobs? 

selectedCity1 = 'Sydney'
selectedCity2 = 'Brisbane'

# Count the number of times Brisbane is in the data table and assume each is for a job
brisNumber2 = (df["Location"].value_counts().loc[selectedCity2])

# Count the number of times Brisbane is in the data table and assume each is for a job
sydneyNumber1 = (df["Location"].value_counts().loc[selectedCity1])

print(f'{selectedCity1} has {sydneyNumber1} jobs, while {selectedCity2} has {brisNumber2} jobs.')


# %%
# Setup Dictionaries for Selecteded cities Sydney and Brisbane so we can count the number of jobs per Job Type and the top jobs per Classification

#selectedCity1 = 'Sydney'
subclasses = []
for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity1:
        subclasses.append(df['Classification'][i])

# Use a dict to count dupes
SydCityJobCount = {}
for i in range(len(subclasses)):
    if subclasses[i] not in SydCityJobCount:
        SydCityJobCount[subclasses[i]] = 1
    else:
        count = SydCityJobCount[subclasses[i]]
        SydCityJobCount[subclasses[i]] = count + 1

# setup Job Type Numbers
jobclasses1 = []

for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity1:
        jobclasses1.append(df['JobType'][i])

# Use a dict to count duplicate Classifications
SydCityJobTypeCount = {}
for i in range(len(jobclasses1)):
    if jobclasses1[i] not in SydCityJobTypeCount:
        SydCityJobTypeCount[jobclasses1[i]] = 1
    else:
        count = SydCityJobTypeCount[jobclasses1[i]]
        SydCityJobTypeCount[jobclasses1[i]] = count + 1  

# Get top 5 Companies
Compamyclasses1 = []

for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity1:
        Compamyclasses1.append(df['Company'][i])

# Use a dict to count duplicate Classifications
SydCityCompanyCount = {}
for i in range(len(Compamyclasses1)):
    if Compamyclasses1[i] not in SydCityCompanyCount:
        SydCityCompanyCount[Compamyclasses1[i]] = 1
    else:
        count = SydCityCompanyCount[Compamyclasses1[i]]
        SydCityCompanyCount[Compamyclasses1[i]] = count + 1  


# Details for the second selected city - Brisbane

#selectedCity2 = 'Brisbane'
subclasses2 = []

for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity2:
        subclasses2.append(df['Classification'][i])

# Use a dict to count duplicate Classifications
BrisCityJobCount = {}
for i in range(len(subclasses2)):
    if subclasses2[i] not in BrisCityJobCount:
        BrisCityJobCount[subclasses2[i]] = 1
    else:
        count = BrisCityJobCount[subclasses2[i]]
        BrisCityJobCount[subclasses2[i]] = count + 1

# Number of Jobs in Brisbane by Type
jobclasses2 = []

for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity2:
        jobclasses2.append(df['JobType'][i])

# Use a dict to count duplicate Classifications
BrisCityJobTypeCount = {}
for i in range(len(jobclasses2)):
    if jobclasses2[i] not in BrisCityJobTypeCount:
        BrisCityJobTypeCount[jobclasses2[i]] = 1
    else:
        count = BrisCityJobTypeCount[jobclasses2[i]]
        BrisCityJobTypeCount[jobclasses2[i]] = count + 1  

# Get top 5 Companies
Compamyclasses2 = []

for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity2:
        Compamyclasses2.append(df['Company'][i])

# Use a dict to count duplicate Classifications
BrisCityCompanyCount = {}
for i in range(len(Compamyclasses2)):
    if Compamyclasses2[i] not in BrisCityCompanyCount:
        BrisCityCompanyCount[Compamyclasses2[i]] = 1
    else:
        count = BrisCityCompanyCount[Compamyclasses2[i]]
        BrisCityCompanyCount[Compamyclasses2[i]] = count + 1                        


# %%
# How many jobs each type (casual, fulltime, etc.) are there in each city?

# Sydney
SydCityJobTypeCount


# %%
# How many jobs each type (casual, fulltime, etc.) are there in each city?

#Brisbane
BrisCityJobTypeCount 


# %%
#In each city, which are top 5 job sectors? How many jobs are there in each sector?
# Sort the Sydney City Dictionary and show top 5 work sectors by job number
sortedSydneyCount = sorted(SydCityJobCount.items(), key = lambda x: x[1], reverse = True)
print(f'The top 5 Job sectors in {selectedCity1} are')
sortedSydneyCount[0:5]


# %%
# Sort the Brisbane City Dictionary and show top 5 work sectors by job number
sortedBrisbaneCount = sorted(BrisCityJobCount.items(), key = lambda x: x[1], reverse = True)

print(f'The top 5 Job sectors in {selectedCity2} are')
sortedBrisbaneCount[0:5]


# %%
# Visualise the top 5 job sectors in pie chart for each city - Sydney

ListCityJobCount1 = sortedSydneyCount[0:5]
Labels1 = []
Size1 = []
CutOff1 = 5
OtherCount1 = 0
for i in range(len(ListCityJobCount1)):
    if i < CutOff1:
        Labels1.append(ListCityJobCount1[i][0])
        Size1.append(ListCityJobCount1[i][1])
    else:
        OtherCount1 = OtherCount1 + ListCityJobCount1[i][1]

# Pie chart for job market share of cities
plt.pie(Size1, labels=Labels1, colors=sns.color_palette(), autopct='%1.1f%%', startangle=90, pctdistance= 0.8, radius=1)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title(f'{selectedCity1} Jobs by Market Share',size=16,loc='center')
plt.show()


# %%
# Visualise the top 5 job sectors in pie chart for each city - Brisbane

ListCityJobCount2 = sortedBrisbaneCount[0:5]
Labels2 = []
Size2 = []
CutOff2 = 5
OtherCount2 = 0
for i in range(len(ListCityJobCount2)):
    if i < CutOff2:
        Labels2.append(ListCityJobCount2[i][0])
        Size2.append(ListCityJobCount2[i][1])
    else:
        OtherCount2 = OtherCount2 + ListCityJobCount2[i][1]

# Pie chart for job market share of cities
plt.pie(Size2, labels=Labels2, colors=sns.color_palette(), autopct='%1.1f%%', startangle=90, pctdistance= 0.8, radius=1)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title(f'{selectedCity2} Jobs by Market Share',size=16,loc='center')
plt.show()


# %%
# In each city, list the job salary range with the corresponding number of jobs. Which city is more well-paid?
SalRangeA = []
for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity1:
        SalRangeA.append(df['HighestSalary'][i])

SalRangeB = []
for i in range(len(df['Location'])):
    if df['Location'][i] == selectedCity2:
        SalRangeB.append(df['HighestSalary'][i])

SalRangeACount = {}
for i in range(len(SalRangeA)):
    if SalRangeA[i] not in SalRangeACount:
        SalRangeACount[SalRangeA[i]] = 1
    else:
        count = SalRangeACount[SalRangeA[i]]
        SalRangeACount[SalRangeA[i]] = count + 1 


SalRangeBCount = {}
for i in range(len(SalRangeB)):
    if SalRangeB[i] not in SalRangeBCount:
        SalRangeBCount[SalRangeB[i]] = 1
    else:
        count = SalRangeBCount[SalRangeB[i]]
        SalRangeBCount[SalRangeB[i]] = count + 1 


# %%
print(f'{selectedCity1} has salary ranges of {SalRangeACount}')


CityA = SalRangeACount.keys()
Citya = SalRangeACount.values()

plt.bar(CityA, Citya, width = 10)
plt.title(f'Job Distribution by Salary in {selectedCity1}')
plt.xlabel('Salary in thousands')
plt.show()


# %%
print(f'{selectedCity2} has salary ranges of {SalRangeBCount}')


CityB = SalRangeBCount.keys()
Cityb = SalRangeBCount.values()

plt.bar(CityB, Cityb, width = 10)
plt.title(f'Job Distribution by Salary in {selectedCity2}')
plt.xlabel('Salary in thousands')
plt.show()

# %% [markdown]
# # In each city, list the job salary range with the corresponding number of jobs. Which city is more well-paid? (1 point)
# # Sydney has both a higher number of jobs and the graph shows a larger proportion of sydney jobs are in those higher brackets that in brisbane
# 

# %%
# List top 5 companies in each city? Which sectors do they belong to?

#Sydney Companies
sortedSydCompanies = sorted(SydCityCompanyCount.items(), key = lambda x: x[1], reverse = True)

print(f'The top 5 Companies in {selectedCity1} are')
sortedSydCompanies[0:6]


# %%
# List top 5 companies in each city? Which sectors do they belong to?

#Brisbane Companies

sortedBrisCompanies = sorted(BrisCityCompanyCount.items(), key = lambda x: x[1], reverse = True)

print(f'The top 5 Companies in {selectedCity2} are')
sortedBrisCompanies[1:6]


# %%
def ClassCount(Location):
    return Location['Classification'].value_counts()[0:3]


# %%
Bris = df.loc[df['Location'] == selectedCity2]
Bris1 = Bris.loc[df['Company'] == 'Jora Local']
print(ClassCount(Bris1), end = '\n \n')
Bris2 = Bris.loc[df['Company'] == 'u&u. Recruitment Partners']
print(ClassCount(Bris2), end = '\n \n')
Bris3 = Bris.loc[df['Company'] == 'Hudson']
print(ClassCount(Bris3), end = '\n \n')
Bris4 = Bris.loc[df['Company'] == 'The University of Queensland']
print(ClassCount(Bris4), end = '\n \n')
Bris5 = Bris.loc[df['Company'] == 'Programmed Skilled Workforce']
print(ClassCount(Bris5), end = '\n \n')
# same again for second city
Snd = df.loc[df['Location'] == selectedCity1]
Snd1 = Snd.loc[df['Company'] == 'Jora Local']
print(ClassCount(Snd1), end = '\n \n')
Snd2 = Snd.loc[df['Company'] == 'Robert Walters']
print(ClassCount(Snd2), end = '\n \n')
Snd3 = Snd.loc[df['Company'] == 'Design & Build']
print(ClassCount(Snd3), end = '\n \n')
Snd4 = Snd.loc[df['Company'] == 'Bluefin Resources Pty Limited']
print(ClassCount(Snd4), end = '\n \n')
Snd5 = Snd.loc[df['Company'] == 'Paxus']
print(ClassCount(Snd5), end = '\n \n')


# %%
# Between 2 cities, which do you think it is better for employees. Explain your choice

# %% [markdown]
# Part 2 - Analyse by Time

# %%
#extra stuff needed before we continue
df["Date"] = df["Date"].replace(to_replace = r'T.*', value = '', regex = True)
months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
DayOfTheWeek = {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0}
dates = df['Date'].value_counts()
Dates = []
for i in range(len(dates)):
    Dates.append(dates.index[i])

for j in range(len(Dates)):
    ThisDate = Dates[j].split('-')
    Dates[j] = ThisDate[1:3]

def xToDay(x):
    if (x == 0):
        return 'Sunday'
    elif (x == 1):
        return 'Monday'
    elif (x == 2):
        return 'Tuesday'
    elif (x == 3):
        return 'Wednesday'
    elif (x == 4):
        return 'Thursday'
    elif (x == 5):
        return 'Friday'
    elif (x == 6):
        return 'Saturday'


# %%
# Visualise the number of job posts by day of week (Graph)
x = int
for i in range(len(Dates)):
    # Find day of the week
    if (Dates[i][0] == '10'):
        x = int(Dates[i][1]) % 7 
    elif (Dates[i][0] == '11'): 
        x = (int(Dates[i][1]) + 31) % 7 
    # store counter to dictionary
    DayOfTheWeek[xToDay(x)] = DayOfTheWeek[xToDay(x)] + dates[i]
#DayOfTheWeek
plt.figure(figsize=(10,5))
plt.title('Number of Postings By Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Job Postings')
Yaxis = DayOfTheWeek.values()
Xaxis = DayOfTheWeek.keys()
plt.bar(Xaxis, Yaxis, align = 'center')


# %%
# Visualise the number of job posts by day of the month. (Graph)
DayOfTheMonth = {'01': 0,'02': 0,'03': 0,'04': 0,'05': 0,'06': 0,'07': 0,'08': 0,'09': 0,'10': 0,'11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0,'19': 0,'20': 0,'21': 0,'22': 0,'23': 0,'24': 0,'25': 0,'26': 0,'27': 0,'28': 0,'29': 0,'30': 0, '31': 0}
x = int
for i in range(len(Dates)):
    # store counter to dictionary
    DayOfTheMonth[Dates[i][1]] = int(DayOfTheMonth[Dates[i][1]]) + dates[i]
#DayOfTheMonth
plt.figure(figsize=(15,10))
plt.title('Number of Postings By Day of the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Number of Job Postings')
Yaxis = DayOfTheMonth.values()
Xaxis = DayOfTheMonth.keys()
plt.bar(Xaxis, Yaxis, align = 'center')


# %%
# Visualise trending of the job postings for the big cities (Graph)
#2nd for loop for each selcity
Bris
Snd
# Other 3 top 5

# %% [markdown]
# Part 3 - Forecasting and skill extractions

# %%
# Using moving average for 7 days and 30 days to predict the number of job postings and visualise them in line chart
# Which one creates a better prediction


# %%
# Choose your favourite job sector/sub-sector, then use TF/IDF to extract important keywords. 
# Visualise them in word cloud # chart (hint: you can use the online tool https://wordart.com/create or similar websites

# %% [markdown]
# Section 2 - Discussion

# %%



