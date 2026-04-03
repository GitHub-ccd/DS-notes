
# SQL and Relational Databases - Recap

## Introduction

In this section, you learned how to construct different `SELECT` queries in SQL. You then got some extra practice with constructing advanced queries and applied this knowledge to some real-world job interview questions!


## SELECT

The first thing you saw with SQL is how to select data from tables. You saw how to connect to a database and query basic data from a table using column names or the wildcard parameter `*`. 

## Filters

After looking at basic `SELECT` statements, you then saw how to filter your selections using the `WHERE` clause.

## Ordering

Along with filtering, you also saw how to order your query selections. To do this, you use the `ORDER BY` clause. Remember that the default behavior there is to return results in ascending order. You can verbosely specify this with the `ASC` keyword, or modify the behavior to sort in descending order with the `DESC` keyword.

## Grouping

Next up, you saw how to create aggregates with your data. This involved using the `GROUP BY` statement. You saw that you can both explicitly state the column names that you wish to group by or that you can use aliases for the columns using numbers such as 1,2,3. You also got to investigate some aggregate functions such as `COUNT()`, `MAX()`, `MIN()`, and `AVG()`. Finally, you also saw that you can filter based on the results of aggregate functions using the `HAVING` clause. 

## Joins

After taking a look at more complex queries for a single table, you started to investigate how you could combine data from multiple tables. You did this using the `JOIN` clause. Remember that you can specify the links between tables with the `USING()` clause if the column name is identical between the tables or the `ON` clause if you must specify the link more manually. You also saw how to alias table names during your joins.

## Subqueries

With some of the more complicated join and aggregate scenarios that began to arise, you also saw how to use subqueries to break down complex queries into parts. You also saw how you could potentially create aggregates of aggregates using subqueries.

## Database Administration

You saw how to create databases, tables, and subsequently populate those containers with data. You also saw how to delete or modify information. Database administration is a complex topic that has a lot more considerations including user permissions and improving query execution time, but this was a solid introduction to get you up and running.

## Queries and Technical Questions in Interviews

You can expect to run into SQL questions on job interviews. Often times when asked to write a query, you'll be given a hypothetical situation and asked to write a query, without having an ERD diagram or tables to look at. When working through these questions, it's important to clarify your assumptions, and to ask questions to make sure that your assumptions are actually correct! Once you have the information you need, be sure to write clean, well-structured SQL code. Consider capitalizing the SQL keywords, and use semantic variable names for any tables or fields you have to assume exist when writing your queries. This is also a situation where thinking out loud and engaging your interviewer is a great strategy. They're likely trying to evaluate how you would work on a team, just as much as they're trying to evaluate your technical knowledge or your ability to get data from a relational database.

## Open-ended Questions in Interviews

You may also encounter open-ended SQL questions where there is no single correct solution. When faced with these sorts of interview questions, have an opinion, and be ready to back it up with your rationale! For these sorts of questions, interviewers are often trying to evaluate *how* you approach problems and evaluate your thought process, so helping them understand your thought process is very important!

## The Internet Is Your Friend

All of the real-world interview questions you worked through in this section came from popular interview sites such as Glassdoor. If you still feel a bit shaky about your ability to answer SQL/relational database questions in an interview, that's okay -- practice makes perfect! Don't be afraid to peruse sites like Glassdoor and others to look for the types of SQL questions you can expect to see during the interview process. Just make sure that when you look at the questions, you try to answer them yourself first before looking at the answers others have posted!

## Summary

Congratulations! You should have a good amount of SQL skills to harness in your data adventures going forward! While you are apt to use other tools such as Pandas to do a lot of your exploratory analysis and data manipulation, databases provide a much more powerful data storage option then flat files like csv or excel workbooks. You also got some experience practicing the type of technical questions you will encounter when interviewing for jobs. The more practice you get, the more comfortable you will be when you're actually interviewing!
