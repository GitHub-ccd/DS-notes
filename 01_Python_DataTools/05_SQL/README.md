# Section 05 — SQL

Relational databases, SQL queries, and integrating SQL with pandas.

## Notebooks

| # | Notebook | Topic |
|---|----------|-------|
| 01 | `01_selecting_and_filtering.ipynb` | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `BETWEEN`, `IS NULL` |
| 02 | `02_database_admin.ipynb` | SQLite data types, `CREATE TABLE`, `INSERT`, `UPDATE`, `DELETE`, `commit` |
| 03 | `03_aggregation_and_groupby.ipynb` | `COUNT`/`SUM`/`AVG`/`MIN`/`MAX`, `GROUP BY`, aliases, `HAVING` |
| 04 | `04_joins.ipynb` | `INNER JOIN`, `LEFT JOIN`, `USING`, table aliases, 1:many, many:many |
| 05 | `05_subqueries.ipynb` | Subqueries in `WHERE`/`FROM`, `IN`, nested aggregates |
| 06 | `06_sql_with_pandas.ipynb` | `pd.read_sql()`, `df.query()`, `pandasql` |

## Reference Databases

Two standalone reference notebooks with their own databases are kept as-is:

- `Airport_database/Airport.ipynb` — Airport data (CSV + SQLite)
- `Chinook_database/Chinook_Sqlite.ipynb` — Chinook music store database
