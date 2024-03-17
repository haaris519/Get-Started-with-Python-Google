#!/usr/bin/env python
# coding: utf-8

# # **Waze Project**
# **Course 2 - Get Started with Python**

# Welcome to the Waze Project!
# 
# Your Waze data analytics team is still in the early stages of their user churn project. Previously, you were asked to complete a project proposal by your supervisor, May Santner. You have received notice that your project proposal has been approved and that your team has been given access to Waze's user data. To get clear insights, the user data must be inspected and prepared for the upcoming process of exploratory data analysis (EDA).
# 
# A Python notebook has been prepared to guide you through this project. Answer the questions and create an executive summary for the Waze data team.

# # **Course 2 End-of-course project: Inspect and analyze data**
# 
# In this activity, you will examine data provided and prepare it for analysis. This activity will help ensure the information is,
# 
# 1.   Ready to answer questions and yield insights
# 
# 2.   Ready for visualizations
# 
# 3.   Ready for future hypothesis testing and statistical methods
# <br/>
# 
# **The purpose** of this project is to investigate and understand the data provided.
# 
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings.
# <br/>
# 
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation
# * How can you best prepare to understand and organize the provided information?
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities
# 
# * Compile summary information about the data to inform next steps
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into variables
# 
# 
# <br/>
# 
# Follow the instructions and answer the following questions to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work.
# 
# 

# # **Identify data types and compile summary information**
# 

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**

# Throughout these project notebooks, you'll see references to the problem-solving framework, PACE. The following notebook components are labeled with the respective PACE stages: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided driver data?
# 
# 
# *Begin by exploring your dataset and consider reviewing the Data Dictionary.*

# ==> ENTER YOUR RESPONSE HERE

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Imports and data loading**
# 
# Start by importing the packages that you will need to load and explore the dataset. Make sure to use the following import statements:
# 
# *   `import pandas as pd`
# 
# *   `import numpy as np`
# 

# In[1]:


# Import packages for data manipulation
### YOUR CODE HERE ###
import pandas as pd
import numpy as np


# Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[2]:


# Load dataset into dataframe
df = pd.read_csv('waze_dataset.csv')


# ### **Task 2b. Summary information**
# 
# View and inspect summary information about the dataframe by **coding the following:**
# 
# 1.   df.head(10)
# 2.   df.info()
# 
# *Consider the following questions:*
# 
# 1. When reviewing the `df.head()` output, are there any variables that have missing values?
# 
# 2. When reviewing the `df.info()` output, what are the data types? How many rows and columns do you have?
# 
# 3. Does the dataset have any missing values?

# In[3]:


### YOUR CODE HERE ###
df.head(10)


# In[4]:


### YOUR CODE HERE ###
df.info()


# ==> ENTER YOUR RESPONSES TO QUESTIONS 1-3 HERE

# ### **Task 2c. Null values and summary statistics**
# 
# Compare the summary statistics of the 700 rows that are missing labels with summary statistics of the rows that are not missing any values.
# 
# **Question:** Is there a discernible difference between the two populations?
# 

# In[5]:


# Isolate rows with null values
### YOUR CODE HERE ###
# Isolate rows with null values in the 'label' column
missing_labels_subset = df[df['label'].isnull()]

# Compute summary statistics for the subset with missing labels
summary_statistics_missing_labels = missing_labels_subset.describe()

# Compare summary statistics between the subset with missing labels and the complete dataset
print("Summary statistics for rows with missing labels:")
print(summary_statistics_missing_labels)

# Display summary statistics for rows without any missing values
print("\nSummary statistics for rows without any missing values:")
print(df.dropna().describe())

# Display summary stats of rows with null values
### YOUR CODE HERE ###


# In[6]:


# Isolate rows without null values
### YOUR CODE HERE ###

# Display summary stats of rows without null values
### YOUR CODE HERE ###


# ==> ENTER YOUR RESPONSE HERE

# ### **Task 2d. Null values - device counts**
# 
# Next, check the two populations with respect to the `device` variable.
# 
# **Question:** How many iPhone users had null values and how many Android users had null values?

# In[7]:


# Get count of null values by device
### YOUR CODE HERE ###
null_values_by_device = missing_labels_subset['device'].value_counts()
# Display the count of null values for each device
print("Count of null values by device:")
print(null_values_by_device)


# ==> ENTER YOUR RESPONSE HERE

# Now, of the rows with null values, calculate the percentage with each device&mdash;Android and iPhone. You can do this directly with the [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html) function.

# In[9]:


# Calculate % of iPhone nulls and Android nulls
### YOUR CODE HERE ###
# Calculate % of iPhone nulls and Android nulls
# Calculate the count of null values for each device
null_values_by_device = missing_labels_subset['device'].value_counts()

# Calculate the total count of null values
total_null_values = null_values_by_device.sum()

# Calculate the percentage of null values for each device
percentage_nulls_by_device = (null_values_by_device / total_null_values) * 100

# Display the percentage of nulls for each device
print("Percentage of null values by device:")
print(percentage_nulls_by_device)


# How does this compare to the device ratio in the full dataset?

# In[11]:


# Calculate % of iPhone users and Android users in full dataset
### YOUR CODE HERE ###
# Calculate the count of each device in the full dataset
device_counts = df['device'].value_counts()
total_devices = device_counts.sum()
percentage_iphone_users = (device_counts['iPhone'] / total_devices) * 100
percentage_android_users = (device_counts['Android'] / total_devices) * 100
print("Percentage of iPhone users in the full dataset:", percentage_iphone_users)
print("Percentage of Android users in the full dataset:", percentage_android_users)


# The percentage of missing values by each device is consistent with their representation in the data overall.
# 
# There is nothing to suggest a non-random cause of the missing data.

# Examine the counts and percentages of users who churned vs. those who were retained. How many of each group are represented in the data?

# In[13]:


# Calculate counts of churned vs. retained
### YOUR CODE HERE ###
# Calculate counts of churned vs. retained customers
churn_counts = df['label'].value_counts()
print("Counts of churned vs. retained customers:")
print(churn_counts)


# This dataset contains 82% retained users and 18% churned users.
# 
# Next, compare the medians of each variable for churned and retained users. The reason for calculating the median and not the mean is that you don't want outliers to unduly affect the portrayal of a typical user. Notice, for example, that the maximum value in the `driven_km_drives` column is 21,183 km. That's more than half the circumference of the earth!

# In[17]:


# Calculate median values of all columns for churned and retained users
### YOUR CODE HERE ###
# Group the data by the 'label' column and calculate the median values for each group
# Group the data by the 'label' column
grouped_data = df.groupby('label')

# Calculate the median for each variable for churned and retained users
median_values_by_label = grouped_data.median()

print("Median values for churned and retained users:")
print(median_values_by_label)


# This offers an interesting snapshot of the two groups, churned vs. retained:
# 
# Users who churned averaged ~3 more drives in the last month than retained users, but retained users used the app on over twice as many days as churned users in the same time period.
# 
# The median churned user drove ~200 more kilometers and 2.5 more hours during the last month than the median retained user.
# 
# It seems that churned users had more drives in fewer days, and their trips were farther and longer in duration. Perhaps this is suggestive of a user profile. Continue exploring!

# Calculate the median kilometers per drive in the last month for both retained and churned users.
# 
# Begin by dividing the `driven_km_drives` column by the `drives` column. Then, group the results by churned/retained and calculate the median km/drive of each group.

# In[19]:


# Add a column to df called `km_per_drive`
### YOUR CODE HERE ###

# Group by `label`, calculate the median, and isolate for km per drive
### YOUR CODE HERE ###
# Add a new column 'km_per_drive' to the DataFrame
df['km_per_drive'] = df['driven_km_drives'] / df['drives']

# Group the results by 'label' and calculate the median km/drive for each group
median_km_per_drive_by_label = df.groupby('label')['km_per_drive'].median()

# Display the median km/drive for churned and retained users
print("Median kilometers per drive in the last month for churned and retained users:")
print(median_km_per_drive_by_label)


# The median retained user drove about one more kilometer per drive than the median churned user. How many kilometers per driving day was this?
# 
# To calculate this statistic, repeat the steps above using `driving_days` instead of `drives`.

# In[20]:


# Add a column to df called `km_per_driving_day`
### YOUR CODE HERE ###
# Add a new column 'drives_per_driving_day' to the DataFrame
df['drives_per_driving_day'] = df['drives'] / df['driving_days']

# Group the results by 'label' and calculate the median drives per driving day for each group
median_drives_per_driving_day_by_label = df.groupby('label')['drives_per_driving_day'].median()

# Display the median drives per driving day for churned and retained users
print("Median drives per driving day for churned and retained users:")
print(median_drives_per_driving_day_by_label)


# Now, calculate the median number of drives per driving day for each group.

# In[21]:


# Add a column to df called `drives_per_driving_day`
### YOUR CODE HERE ###
# Add a new column 'drives_per_driving_day' to the DataFrame
df['drives_per_driving_day'] = df['drives'] / df['driving_days']

# Group the results by 'label' and calculate the median drives per driving day for each group
median_drives_per_driving_day_by_label = df.groupby('label')['drives_per_driving_day'].median()

# Display the median drives per driving day for churned and retained users
print("Median drives per driving day for churned and retained users:")
print(median_drives_per_driving_day_by_label)


# The median user who churned drove 698 kilometers each day they drove last month, which is almost ~240% the per-drive-day distance of retained users. The median churned user had a similarly disproporionate number of drives per drive day compared to retained users.
# 
# It is clear from these figures that, regardless of whether a user churned or not, the users represented in this data are serious drivers! It would probably be safe to assume that this data does not represent typical drivers at large. Perhaps the data&mdash;and in particular the sample of churned users&mdash;contains a high proportion of long-haul truckers.
# 
# In consideration of how much these users drive, it would be worthwhile to recommend to Waze that they gather more data on these super-drivers. It's possible that the reason for their driving so much is also the reason why the Waze app does not meet their specific set of needs, which may differ from the needs of a more typical driver, such as a commuter.

# Finally, examine whether there is an imbalance in how many users churned by device type.
# 
# Begin by getting the overall counts of each device type for each group, churned and retained.

# In[23]:


# For each label, calculate the number of Android users and iPhone users
### YOUR CODE HERE ###
# Calculate the number of Android and iPhone users for churned users
churned_device_counts = df[df['label'] == 'churned']['device'].value_counts()

# Calculate the number of Android and iPhone users for retained users
retained_device_counts = df[df['label'] == 'retained']['device'].value_counts()

# Display the counts of Android and iPhone users for churned and retained groups
print("Number of Android and iPhone users for churned users:")
print(churned_device_counts)
print("\nNumber of Android and iPhone users for retained users:")
print(retained_device_counts)


# Now, within each group, churned and retained, calculate what percent was Android and what percent was iPhone.

# In[24]:


# For each label, calculate the percentage of Android users and iPhone users
### YOUR CODE HERE ###
# Calculate the total number of users in the churned and retained groups
total_churned_users = churned_device_counts.sum()
total_retained_users = retained_device_counts.sum()
churned_android_percentage = (churned_device_counts['Android'] / total_churned_users) * 100
churned_iphone_percentage = (churned_device_counts['iPhone'] / total_churned_users) * 100

# Calculate the percentage of Android and iPhone users for retained users
retained_android_percentage = (retained_device_counts['Android'] / total_retained_users) * 100
retained_iphone_percentage = (retained_device_counts['iPhone'] / total_retained_users) * 100

# Display the percentages of Android and iPhone users for churned and retained groups
print("Percentage of Android and iPhone users for churned users:")
print("Android:", churned_android_percentage, "%")
print("iPhone:", churned_iphone_percentage, "%")

print("\nPercentage of Android and iPhone users for retained users:")
print("Android:", retained_android_percentage, "%")
print("iPhone:", retained_iphone_percentage, "%")


# The ratio of iPhone users and Android users is consistent between the churned group and the retained group, and those ratios are both consistent with the ratio found in the overall dataset.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 3. Conclusion**
# 
# Recall that your supervisor, May Santer, asked you to share your findings with the data team in an executive summary. Consider the following questions as you prepare to write your summary. Think about key points you may want to share with the team, and what information is most relevant to the user churn project.
# 
# **Questions:**
# 
# 1. Did the data contain any missing values? How many, and which variables were affected? Was there a pattern to the missing data?
# 
# 2. What is a benefit of using the median value of a sample instead of the mean?
# 
# 3. Did your investigation give rise to further questions that you would like to explore or ask the Waze team about?
# 
# 4. What percentage of the users in the dataset were Android users and what percentage were iPhone users?
# 
# 5. What were some distinguishing characteristics of users who churned vs. users who were retained?
# 
# 6. Was there an appreciable difference in churn rate between iPhone users vs. Android users?
# 
# 
# 
# 

# ==> ENTER YOUR RESPONSES TO QUESTIONS 1-6 HERE

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
