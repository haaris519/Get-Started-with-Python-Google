#!/usr/bin/env python
# coding: utf-8

# # **TikTok Project**
# **Course 2 - Get Started with Python**

# Welcome to the TikTok Project!
# 
# You have just started as a data professional at TikTok.
# 
# The team is still in the early stages of the project. You have received notice that TikTok's leadership team has approved the project proposal. To gain clear insights to prepare for a claims classification model, TikTok's provided data must be examined to begin the process of exploratory data analysis (EDA).
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # **Course 2 End-of-course project: Inspect and analyze data**
# 
# In this activity, you will examine data provided and prepare it for analysis.
# <br/>
# 
# **The purpose** of this project is to investigate and understand the data provided. This activity will:
# 
# 1.   Acquaint you with the data
# 
# 2.   Compile summary information about the data
# 
# 3.   Begin the process of EDA and reveal insights contained in the data
# 
# 4.   Prepare you for more in-depth EDA, hypothesis testing, and statistical analysis
# 
# **The goal** is to construct a dataframe in Python, perform a cursory inspection of the provided dataset, and inform TikTok data team members of your findings.
# <br/>
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation
# * How can you best prepare to understand and organize the provided TikTok information?
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning and future exploratory data analysis (EDA) and statistical activities
# 
# * Compile summary information about the data to inform next steps
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into variables
# 
# <br/>
# 
# To complete the activity, follow the instructions and answer the questions below. Then, you will us your responses to these questions and the questions included in the Course 2 PACE Strategy Document to create an executive summary.
# 
# Be sure to complete this activity before moving on to Course 3. You can assess your work by comparing the results to a completed exemplar after completing the end-of-course project.

# # **Identify data types and compile summary information**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.
# 
# # **PACE stages**
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:
# 
# 

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided information?
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
# *   `import pandas as pd`
# 
# *   `import numpy as np`
# 

# In[2]:


import pandas as pd
import numpy as np


# Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[3]:


# Load dataset into dataframe
data = pd.read_csv("tiktok_dataset.csv")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by **coding the following:**
# 
# 1. `data.head(10)`
# 2. `data.info()`
# 3. `data.describe()`
# 
# *Consider the following questions:*
# 
# **Question 1:** When reviewing the first few rows of the dataframe, what do you observe about the data? What does each row represent?
# 
# **Question 2:** When reviewing the `data.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# **Question 3:** When reviewing the `data.describe()` output, what do you notice about the distributions of each variable? Are there any questionable values? Does it seem that there are outlier values?
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[4]:


data.head(10)


# In[5]:


data.info()


# In[6]:


data.describe()


# **Business Analyst Report**
# 
# **1. Introduction**
# - Brief overview of the purpose of the report.
# - Introduction to the dataset and its significance.
# - Statement of the problem or objective of the analysis.
# 
# **2. Data Overview**
# - Summary statistics of the dataset.
# - Description of the columns and their significance.
# 
# **3. Analysis of Claim Status**
# - Breakdown of the claim status categories.
# - Analysis of verified and non-verified claims.
# - Insights into the distribution of claims under review.
# 
# **4. Video Metrics Analysis**
# - Examination of video metrics including view count, like count, share count, download count, and comment count.
# - Trends and patterns observed in the video metrics.
# - Correlation analysis between different video metrics.
# 
# **5. Author Ban Status**
# - Analysis of the impact of author ban status on video metrics.
# - Comparison of video performance based on author ban status.
# 
# **6. Video Duration Analysis**
# - Evaluation of video duration and its impact on viewer engagement.
# - Comparison of viewer engagement for videos of different durations.
# 
# **7. Conclusion**
# - Summary of key findings from the analysis.
# - Insights into factors influencing video performance and claim status.
# - Recommendations for further actions or analysis.
# 
# **8. Appendix**
# - Additional charts, graphs, or tables supporting the analysis.
# - Details on data preprocessing steps if applicable.

# ### **Task 2c. Understand the data - Investigate the variables**
# 
# In this phase, you will begin to investigate the variables more closely to better understand them.
# 
# You know from the project proposal that the ultimate objective is to use machine learning to classify videos as either claims or opinions. A good first step towards understanding the data might therefore be examining the `claim_status` variable. Begin by determining how many videos there are for each different claim status.

# In[7]:


claim_status_counts = data['claim_status'].value_counts()
print("Different values for claim status and their counts:")
print(claim_status_counts)


# **Question:** What do you notice about the values shown?
# 
# There are two distinct categories of claim status: "claim" and "opinion".
# The counts of these categories are relatively balanced, with 9608 instances of "claim" and 9476 instances of "opinion".
# This suggests that the dataset contains a substantial number of both claims and opinions, indicating a diverse set of assertions or statements being analyzed.

# Next, examine the engagement trends associated with each different claim status.
# 
# Start by using Boolean masking to filter the data according to claim status, then calculate the mean and median view counts for each claim status.

# In[8]:


# What is the average view count of videos with "claim" status?
### YOUR CODE HERE ###
x=claim_status_counts['claim']
h=data[data['claim_status']=='claim']
o=h['video_view_count'].mean()

print("Different values for claim and their mean:")
print(o)


# In[9]:


x=claim_status_counts['opinion']
h=data[data['claim_status']=='opinion']
o=h['video_view_count'].mean()

print("Different values for opinion and their mean:")
print(o)


# **Question:** What do you notice about the mean and media within each claim category?
# 
# Now, examine trends associated with the ban status of the author.
# 
# Use `groupby()` to calculate how many videos there are for each combination of categories of claim status and author ban status.

# In[10]:


# Get counts for each group combination of claim status and author ban status
### YOUR CODE HERE ###

x=data.groupby(by=['claim_status', 'author_ban_status']).size()
print('Number of videos for each combination of claim status and author ban status:')
print(x)


# **Question:** What do you notice about the number of claims videos with banned authors? Why might this relationship occur?
# 
# Continue investigating engagement levels, now focusing on `author_ban_status`.
# 
# Calculate the median video share count of each author ban status.

# In[11]:


### YOUR CODE HERE ###
median_share_count_by_ban_status = data.groupby('author_ban_status')['video_share_count'].median()
print("Median video share count of each author ban status:")
print(median_share_count_by_ban_status)


# **Question:** What do you notice about the share count of banned authors, compared to that of active authors? Explore this in more depth.
# 
# Use `groupby()` to group the data by `author_ban_status`, then use `agg()` to get the count, mean, and median of each of the following columns:
# * `video_view_count`
# * `video_like_count`
# * `video_share_count`
# 
# Remember, the argument for the `agg()` function is a dictionary whose keys are columns. The values for each column are a list of the calculations you want to perform.

# In[14]:


### YOUR CODE HERE ###
# Calculate the median video share count of each author ban status using agg()

print("***************************************************************************")
# Define the aggregation dictionary
aggregations = {
    'video_view_count': ['count', 'mean', 'median'],
    'video_like_count': ['count', 'mean', 'median'],
    'video_share_count': ['count', 'mean', 'median']
}

# Group the data by 'author_ban_status' and calculate multiple summary statistics
engagement_metrics_by_ban_status = data.groupby('author_ban_status').agg(aggregations)

print("Engagement metrics by author ban status:")
print(engagement_metrics_by_ban_status)


# **Question:** What do you notice about the number of views, likes, and shares for banned authors compared to active authors?
# 
# Now, create three new columns to help better understand engagement rates:
# * `likes_per_view`: represents the number of likes divided by the number of views for each video
# * `comments_per_view`: represents the number of comments divided by the number of views for each video
# * `shares_per_view`: represents the number of shares divided by the number of views for each video

# In[15]:


# Create a likes_per_view column
### YOUR CODE HERE ###
# Create new columns for likes_per_view, comments_per_view, and shares_per_view
data['likes_per_view'] = data['video_like_count'] / data['video_view_count']



# Display the first few rows of the updated DataFrame to verify the new columns


# Create a comments_per_view column
### YOUR CODE HERE ###
data['comments_per_view'] = data['video_comment_count'] / data['video_view_count']
# Create a shares_per_view column
data['shares_per_view'] = data['video_share_count'] / data['video_view_count']
### YOUR CODE HERE ###
print(data.head())


# Use `groupby()` to compile the information in each of the three newly created columns for each combination of categories of claim status and author ban status, then use `agg()` to calculate the count, the mean, and the median of each group.

# In[17]:


### YOUR CODE HERE ###
aggregations = {
    'likes_per_view': ['count', 'mean', 'median'],
    'comments_per_view': ['count', 'mean', 'median'],
    'shares_per_view': ['count', 'mean', 'median']}
engagement_per_status = data.groupby(['claim_status', 'author_ban_status']).agg(aggregations)

print("Engagement metrics per combination of claim status and author ban status:")
print(engagement_per_status)


# **Question:**
# 
# How does the data for claim videos and opinion videos compare or differ? Consider views, comments, likes, and shares.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.
# 
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response.

# ### **Given your efforts, what can you summarize for Rosie Mae Bradshaw and the TikTok data team?**
# 
# *Note for Learners: Your answer should address TikTok's request for a summary that covers the following points:*
# 
# *   What percentage of the data is comprised of claims and what percentage is comprised of opinions?
# *   What factors correlate with a video's claim status?
# *   What factors correlate with a video's engagement level?
# 

# ==> ENTER YOUR RESPONSE HERE

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
