#!/usr/bin/env python
# coding: utf-8

# # Section 5: S5_Data_Cleaning TOC and Notes
# 
# The order of the content and summary important commands of the leasson. 

# ## 1. Data Cleaning in Pandas - Introduction
# [See Notebook](./dsc-introduction-pandas-etl-onl01-dtsc-ft-030220/index.ipynb)
# 
# 
# Extract Transform Load (ETL) --> primary tool is pandas. <br>
# df = pd.read_csv('Yelp_Reviews.csv', index_col=0)<br>
# df['Review_Word_Length'] = df['text'].map(lambda x: len(x.split())) # apply function to col <br>
# df.groupby('business_id')['stars'].mean().head() # Group data <br>
# df[df.duplicated(keep=False)].sort_values(by='business_id') # Use the keep=False to keep the duplicates and sort values to put  duplicates next to each other <br>
# df = df[df.duplicated()] # remove duplicates <br> 
# // Pivot table [wikipeida](https://en.wikipedia.org/wiki/Pivot_table) <br>
# usr_reviews = df.pivot(index='user_id', columns='business_id', values='stars') # Here user_id are the rows and business_id are cols number of stars are in the cell. Some cells will be NaN. 

# ## 2. Lambda Functions
# [See Notebook](./dsc-lambda-functions-onl01-dtsc-ft-030220/index.ipynb)
# 
# throw-away functions on the fly <br>
# df['text'].map(lambda x: len(x.split())).head() # labda Fn example <br>
# df['text'].map(lambda x: 'Good' if any([word in x.lower() for word in ['awesome', 'love', 'good', 'great']]) else 'Bad').head() # Lambda Fn--> t is an interesting demonstration of chaining a conditional, any method, and a list comprehension all inside a lambda function!<br>
# df.date.map(lambda x: x[:4]).head() # ways to access df cols are many I guess ?? <br>
# sorted(names, key=lambda x: x.split()[1]) # because in names there are First and Last name <br>
# 
# [See Lab](./dsc-lambda-functions-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 3. Pandas Groupby 
# [See Notebook](./dsc-pandas-groupby-onl01-dtsc-ft-030220/index.ipynb)
# 
# df.groupby('Sex') <==> df.groupby(df['Sex'])<br>   # equivalent statements 
# df.groupby('Sex').sum()     # use an <b>aggregation function</b> by chaining the call to the end <br>
# * .min(): returns the minimum value for each column by group
# * .max(): returns the maximum value for each column by group
# * .mean(): returns the average value for each column by group
# * .median(): returns the median value for each column by group
# * .count(): returns the count of each column by group
# 
# df.groupby(['Sex', 'Pclass']).mean()   #  <b>Multiple groups</b>
# grouped = df.groupby(['Sex', 'Pclass'])['Survived'].mean()   <br>
# print(grouped['female'])  <br>

# ## 4. Combining DataFrames with Pandas
# [See Notebook](./dsc-combining-dataframes-pandas-onl01-dtsc-ft-030220/index.ipynb)
# 
# When thinking about joins, it is easy to conceptualize them as Venn diagrams.
# 
# * An <b>Outer Join</b> returns all records from both tables
# * An <b>Inner Join</b> returns only the records with matching keys in both tables
# * A <b>Left Join</b> returns all the records from the left table, as well as any records from the right table that have a matching key with a record from the left table
# * A <b>Right Join</b> returns all the records from the right table, as well as any records from the left table that have a matching key with a record from the right table
# 
# joined_df = df1.join(df2, how='inner')    # df1 inner join df2 <br>
# 
# [See Lab](./dsc-combining-dataframes-pandas-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 5. Pivot Tables With Pandas
# [See Notebook](./dsc-pivot-tables-pandas-onl01-dtsc-ft-030220/index.ipynb)
# 
# * <b>Wide</b> format = each column is a variable and each row is observation ; <b>Long</b> format =  each index is a point in time for each observation
# * <b>flattened</b> index structures =  
# * <b>multi-hierarchical</b> index structures = structuring our data with multiple levels of indexes, allowing us to cleanly and easily represent different combinations of data
# some_dataframe.pivot(index='State', columns='Gender', values='Deaths_mean')<br>
# .stack() and unstack() methods <br>
# 
# [See Lab](./dsc-pivot-tables-pandas-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 6. Dealing with Missing Data
# [See Notebook](./dsc-dealing-missing-data-onl01-dtsc-ft-030220/index.ipynb)
# 
# 
# ///Take Notes later
# 
# [Take the Quiz](./dsc-dealing-missing-data-quiz/README.md)
# 
# [See Lab](./dsc-dealing-missing-data-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 7. More on Missing Data 
# [See Notebook](./dsc-more-on-missing-data-onl01-dtsc-ft-030220/index.ipynb)
# 
# // add notes here later
# 
# [See Lab](./dsc-more-on-missing-data-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 8. Project - Data Cleaning
# [See Project](./dsc-data-cleaning-project-onl01-dtsc-ft-030220/index.ipynb)
# 
# Project summary......

# ## 9. Data Cleaning in Pandas - Recap
# [See Notebook](./dsc-summary-data-cleaning-pandas-onl01-dtsc-ft-030220/index.ipynb)
# summary notes

# ## 10. The 3-17-2020 study group code along
# 
# [See Notebook](./Groupby_StudyGroup_codealong.ipynb)

# In[ ]:




