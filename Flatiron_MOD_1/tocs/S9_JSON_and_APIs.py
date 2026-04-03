#!/usr/bin/env python
# coding: utf-8

# # Section 9: TOC and Notes
# 
# In this section, you’ll learn about an additional data type: JSON (which stands for JavaScript Object Notation), as well as APIs (Application Programming Interfaces).

# ## 1.  JSON and APIs - Introduction
# [See Notebook](./dsc-json-apis-intro-v2-1-onl01-dtsc-ft-030220/index.ipynb)
# 
# Whether it’s from an API or a NoSQL store, it's quite possible that some of the data you find yourself working with will be stored using JSON. In this section, you'll build the confidence to be able to import and transform such data.
# 
# Also, many companies provide access to their data via an API, so being able to connect to and work with data provided via an API is a critical skill as a professional data scientist!
# 

# ## 2.  JSON
# 
# [See Notebook](./dsc-json-v2-1-onl01-dtsc-ft-030220/index.ipynb)
# Use the JSON module to load and parse JSON documents
# 
# [See JSON Lab](./dsc-json-lab-v2-1-onl01-dtsc-ft-030220/index.ipynb)
# 

# ## 3. Working with Known JSON Schemas
# [See Notebook](./dsc-working-with-known-json-schemas-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See Working with Known JSON Schemas Lab](./dsc-working-with-known-json-schemas-lab-onl01-dtsc-ft-030220/index.ipynb)
# 

# ## 4. Exploring and Transforming JSON Schemas
# [See Notebook](./dsc-exploring-and-transforming-json-schemas-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See Exploring and Transforming JSON Schemas Lab](./dsc-exploring-and-transforming-json-schemas-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 5. 
# [See Notebook](./dsc-join-statements-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See Join Statements Lab](./dsc-join-statements-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 6. 
# [See Notebook](./dsc-one-to-many-and-many-to-many-joins-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See One-to-Many and Many-to-Many Joins Lab](./dsc-one-to-many-and-many-to-many-joins-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 7. 
# [See Notebook](./dsc-sql-subqueries-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See SQL Subqueries Lab](./dsc-sql-subqueries-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 8. 
# [See Notebook](./dsc-using-sql-with-pandas-lab-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See Using SQL with Pandas Lab](./dsc-using-sql-with-pandas-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 9. 
# [See Notebook](./dsc-sql-database-data-types/index.ipynb)
# 
# [See SQL Database Data Types Lab](./dsc-using-sql-with-pandas-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 10. 
# [See Notebook](./dsc-database-admin-101-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See Database Admin 101 Lab](./dsc-database-admin-101-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 11. 
# [See More Practice with SQL Queries Lab](./dsc-more-practice-with-sql-queries-lab-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See SQL Interview Questions - Quiz](./dsc-sql-interview-questions-quiz-onl01-dtsc-ft-030220/index.ipynb)
# 
# [See SQL Interview Questions Lab](./dsc-sql-interview-questions-lab-onl01-dtsc-ft-030220/index.ipynb)

# ## 12. 
# [See Recap notes](./dsc-sql-recap-v2-1-onl01-dtsc-ft-030220/index.ipynb)

# # practice projects

# <!DOCTYPE html>
# <html>
# <body>
# 
# <h2>Basic HTML Table and Markup the Jupyter notebook</h2>
# 
# <table style="width:100%">
#   <tr>
#     <th>Firstname</th>
#     <th>Lastname</th> 
#     <th>Age</th>
#   </tr>
#   <tr>
#     <td>Jill</td>
#     <td>Smith</td>
#     <td>50</td>
#   </tr>
#   <tr>
#     <td>Eve</td>
#     <td>Jackson</td>
#     <td>94</td>
#   </tr>
#   <tr>
#     <td>John</td>
#     <td>Doe</td>
#     <td>80</td>
#   </tr>
# </table>

# In[ ]:


# import a webpage
from urllib import request
with request.urlopen('http://python.org/') as response:
   html = response.read()
#html


# In[14]:


# Python google search ---> don't work
import requests, sys, webbrowser, bs4
search_str='chamila dharmawardhana'
res = requests.get('https://google.com/search?q='+''.join(search_str))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
linkElements = soup.select('.r a')
linkToOpen = min(5, len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))


# In[ ]:




