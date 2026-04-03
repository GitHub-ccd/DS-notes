
# SQL and Relational Databases - Introduction

## Introduction

In this section, you'll learn about SQL, which stands for Structured Query Language. It has been around since the 1970s and there are many different dialects of the language including MySQL, SQLite, and PostgreSQL, to name a few. Each of these has particularities such as specific functions or keywords for that specific implementation. All of these, however, have the same basic structures including keywords like `SELECT` for querying databases, and the same general database architecture. Toward the end of this section, you'll learn about more advanced SQL operations. You'll also get a chance to answer some SQL interview questions to help prepare you for your job search!


## The Structure of SQL Databases 

SQL databases are the root container for data. Databases are a collection of tables. Each table is similar to a csv-file or a spreadsheet within an Excel workbook. That is, tables are two-dimensional objects with specific columns and associated entries organized into rows. To demonstrate, here is an outline of a database structure:

<img src="images/Database-Schema.png" width=700>

In the diagram, each rectangle is a table, with the table name listed at the top. In this case, we have 8 tables: productlines, products, orderdetails, employees, offices, customers, orders, and payments. Below each of the table names, we have a list of the various column names associated with that table. So for example, the productlines table has four columns: productLine, textDescription, htmlDescription and image. 

### Relational Data

SQL is designed to work with **relational data**. This really just means pieces of data that are related to each other. In the example above, data on the employees table has some relationship to data on the offices table, indicating that an employee may be associated with a specific office location. Likewise, certain orders are associated with certain customers. Lots of real world data is inherently related. For example, students have an association to a course, ingredients are related to a recipe.

You may also note that some of these column names are preceded by an asterix (\*). This indicates that this is the **primary key** for the table. A primary key is a unique identifier for a table. That is, there can only be unique values for this column entry. lastName would not be a good choice for a primary key as it's common for people to have the same last names or even firstName + lastName pairings.

If you look closely, you'll see that the columns that are the primary key for one table can also appear on other tables. This is known as a **foreign key** aka the primary key from a different ("foreign") table. This is the core idea of how data on different tables is associated in a relational database. If you were told a specific customerNumber, and then given a list of order data that included the customerNumber, you could determine which orders were placed by that customer by matching up the primary and foreign keys.

The lines, circles, arrows, and tick marks are showing different categorizations on exactly how this data is linked. You'll learn much more about these relationships later.

## Connecting to and Querying SQL Databases 

Your initial primary use case of SQL will be querying data stored within databases. To do this, you connect to the database with some sort of tool. This could be via Python, as you'll see in the next lesson, the command line, or a GUI tool such as SQLWorkbench. Once you're connected to the database, you can then read and select data from the database, or even write data to the database. To retrieve data from one or more tables you usually use a `SELECT` statement. 

A simple query would look something like this:

```SQL
SELECT col1, col2, col3
FROM table
WHERE records match criteria
LIMIT 100;
```

Don't worry if this is confusing now, you'll soon learn what each line does. For now, just notice that queries start with the `SELECT` clause, followed by what you want to select. If selecting multiple columns, you separate them with a comma. Then you specify where that data is being retrieved from the using the `FROM` clause followed by the table name. Afterward, you can provide conditions such as filters or limits on the amount of data returned.


## Interview Practice
Data retrieval is the most foundational and arguably most important skill in a Data Scientist's toolbox. In your first job as a Data Scientist, you'll quickly learn that it's usually up to you to get the data you need to solve the problem at hand. This means that you need to be an expert at working with relational databases. You can know all the Python and Machine Learning and Statistics in the world, but they're useless if you don't have data to aim those skills at!

Toward the end of this section, you'll review some of the more complex concepts you've learned about SQL queries. Then you'll test your knowledge of relational databases with a short quiz. Finally, you'll end with a lab that features real world interview questions pertaining to SQL and relational databases from major companies such as Facebook and Google!


## Summary

In this lesson, you got a quick overview of what SQL is and saw an actual SQL query! Remember that there are multiple SQL dialects all with particular differences, but the overall language is generally fairly similar and interchangeable. You also learned that knowledge of SQL is important for job interviews since data retrieval is a foundational part of the data science process. 
