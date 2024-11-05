#!/usr/bin/env python
# coding: utf-8

# ### 1] Importing Libraries & Datasets

# In[68]:


import pandas as pd
import numpy as np


# In[69]:


data = pd.read_csv(r'C:\Users\NEXT\Documents\Third year\NTI\final python project\Final Project\anime.csv')


# ### 2] Exploratory Data Analysis (Understanding & Inspecting Data)

# In[70]:


#Check the head of the DataFrame
data.head()


# In[71]:


#Check the tail of the DataFrame
data.tail()


# In[72]:


#rows-cols
data.shape


# In[73]:


#Details
data.info()


# In[74]:


#dataset Statistics
data.describe()


# In[75]:


#Column names
data.columns


# ### 3] Data Preprocessing

# In[76]:


#Check Null values and hundle it
data.isna().sum()


# In[77]:


data = data.dropna()


# In[78]:


#Check Duplicate and hundle it
data.duplicated().sum()


# In[92]:


#Drop unnecessary columns
data = data.drop(columns=['Description', 'Demographic'])


# ### 4] Data Analysis & Visualization

# In[80]:


# 1) Top 10 Anime by Popularity
Top10 = data.nlargest(10, 'Popularity')
Top10


# In[81]:


#bar plot for Top 10 Anime with x-axis: English and Y-axis: Popularity
import plotly.express as px


# In[82]:


fig = px.bar(top_10_anime, 
             x='Popularity', 
             y='English', 
             orientation='h', 
             title='Top 10 Anime by Popularity',
             labels={'English': 'Anime Title (English)', 'Popularity': 'Popularity'},
             color='Popularity', 
             color_continuous_scale='Blues')

# Show the plot
fig.show() 


# In[83]:


# 2)Score distribution

fig = px.histogram(data, 
                   x='Score', 
                   title='Score Distribution of Anime',
                   labels={'Score': 'Score'},
                   nbins=20,  # Adjust the number of bins as needed
                   color_discrete_sequence=['pink'])  # Set the color to pink

# Show the plot
fig.show()


# In[84]:


print(data['Aired'].head(20))


# In[85]:


print(data['Aired'].unique())


# In[86]:


raw_data = pd.read_csv(r'C:\Users\NEXT\Documents\Third year\NTI\final python project\Final Project\anime.csv')
print(raw_data['Aired'].head(20))


# In[87]:


# Function to extract the first year from the "Aired" column
def extract_year(aired_string):
    import re
    # Use regex to find a year in the string
    match = re.search(r'\b(\d{4})\b', aired_string)
    return int(match.group(1)) if match else None

# Apply the function to extract the year
raw_data['Year'] = raw_data['Aired'].apply(extract_year)

# Check the result
print(raw_data[['Aired', 'Year']].head(20))


# In[88]:


# Make sure "Members" is an integer type
raw_data['Members'] = pd.to_numeric(raw_data['Members'], errors='coerce')

# Group by Year and sum the Members
yearwise_members = raw_data.groupby('Year')['Members'].sum().reset_index()

# Display the result
print(yearwise_members)


# In[89]:


# Get the top 7 years by total members
top_7_years = yearwise_members.nlargest(7, 'Members')

# Display the result
print(top_7_years)


# In[90]:


# Create a bar plot for top 7 years by total members
fig = px.bar(top_7_years, 
             x='Year', 
             y='Members', 
             title='Top 7 Years by Total Members',
             labels={'Year': 'Year', 'Members': 'Total Members'},
             color='Members', 
             color_continuous_scale='Blues')

# Show the plot
fig.show()


# # 4)Type
# #Output::
# #Type
# #TV       569
# #Movie    235
# #OVA       84

# In[91]:


# Step 1: Group by 'Type' and count the number of entries
type_counts = data['Type'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']  # Rename columns for clarity

# Display the result
print(type_counts)


# In[93]:


# Step 2: Check unique values in the 'Type' column
unique_types = data['Type'].unique()

# Display the unique types
print(unique_types)


# In[94]:


# Step 3: Count the number of members for each type
type_counts = data.groupby('Type')['Members'].sum().reset_index()

# Display the result
print(type_counts)


# In[101]:


# Check for missing values in the 'Type' column
missing_types = data['Type'].isnull().sum()
print(f"Missing values in 'Type': {missing_types}")


# In[103]:


output = pd.DataFrame({
    'Type': ['TV', 'Movie', 'OVA'],
    'Count': [569, 235, 84]  # Replace these counts with the actual if available
})

print(output)


# In[104]:


# Assuming you have this DataFrame for types and counts
data = {
    'Type': ['TV', 'Movie', 'OVA'],
    'Count': [569, 235, 84]
}
df = pd.DataFrame(data)

# Create a pie chart
plt.figure(figsize=(8, 6))  # Set the figure size
plt.pie(df['Count'], labels=df['Type'], autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[105]:


# Sample data (assuming this is your DataFrame structure)
data = {
    'Genres': [
        'ActionAction, AdventureAdventure, FantasyFantasy',
        'ComedyComedy, RomanceRomance',
        'ActionAction, FantasyFantasy',
        'ActionAction, Sci-FiSci-Fi',
        'DramaDrama, RomanceRomance'
    ]
}
df = pd.DataFrame(data)


# In[106]:


# Step 1: Count occurrences of each genre
# Split the genres by comma and expand into a new DataFrame
genre_counts = df['Genres'].str.split(', ', expand=True).stack().value_counts()


# In[107]:


# Convert to DataFrame
genre_counts_df = genre_counts.reset_index()
genre_counts_df.columns = ['Genres', 'Count']


# In[108]:


# Step 2: Select top genres (if required, otherwise you can plot all)
top_genres = genre_counts_df.head(5)  # Adjust the number as needed


# In[109]:


# Step 3: Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(top_genres['Genres'], top_genres['Count'], color='skyblue')
plt.title('Top Genres')
plt.xlabel('Genres')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()


# In[110]:


# Sample data (assuming this is your DataFrame structure)
data = {
    'Studio': [
        'Studio A', 'Studio B', 'Studio A', 'Studio C', 'Studio B', 
        'Studio A', 'Studio D', 'Studio C', 'Studio B', 'Studio A'
    ]
}
df = pd.DataFrame(data)


# In[111]:


# Step 1: Count occurrences of each studio
studio_counts = df['Studio'].value_counts()


# In[112]:


# Convert to DataFrame
studio_counts_df = studio_counts.reset_index()
studio_counts_df.columns = ['Studio', 'Count']


# In[113]:


# Step 2: Select top studios (if required, otherwise you can plot all)
top_studios = studio_counts_df.head(5)  # Adjust the number as needed


# In[114]:


# Step 3: Create a bar plot
plt.figure(figsize=(10, 6))
plt.bar(top_studios['Studio'], top_studios['Count'], color='lightgreen')
plt.title('Top Studios')
plt.xlabel('Studios')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()


# In[115]:


# Sample data (assuming this is your DataFrame structure)
data = {
    'Source': [
        'Manga', 'Original', 'Manga', 'Light novel', 'Manga',
        'Original', 'Light novel', 'Manga', 'Novel', 'Original'
    ]
}
df = pd.DataFrame(data)


# In[116]:


# Step 1: Count occurrences of each source
source_counts = df['Source'].value_counts()


# In[117]:


# Convert to DataFrame (optional for pie plot, but useful for inspection)
source_counts_df = source_counts.reset_index()
source_counts_df.columns = ['Source', 'Count']


# In[118]:


# Step 2: Create a pie plot
plt.figure(figsize=(8, 8))
plt.pie(source_counts, labels=source_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Sources')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[ ]:




