### May 12
# Introduction to SQL (2)

Creating two tables, with a foreign key creating a link:

```SQL
    CREATE TABLE film_table
    (
      film_id INT IDENTITY(1,1),
      film_name VARCHAR(20),
      film_type VARCHAR(10),
      release_date DATE,

      PRIMARY KEY (film_id)
    );


    CREATE TABLE store_sales
    (
      sale_id INT IDENTITY(1,1),
      time_of_sale DATETIME,
      film_id INT,
      sale_cost_gbp DECIMAL (3,2),

      PRIMARY KEY (sale_id),
      FOREIGN KEY (film_id) REFERENCES film_table (film_id)
    );
```

Using UPDATE:

```SQL
    UPDATE film_table
    SET rating=10
    WHERE rating=5;
```

Using DELETE:

```SQL
    DELETE FROM film_table WHERE film_name = Interstellar;
```

### NULL
- NULL is not nothing
- NULL does not equate to 0
- NULL is not an empty string
- A value can be NULL, but NULL never equals NULL as it is an undefined value

### DELETE Cascade
A foreign key with cascade delete means that if a record in the parent table is deleted, then the corresponding records in the child table will automatically be deleted.

This is called a cascade delete in SQL Server.

```SQL
    CREATE TABLE store_sales
    (
        sale_id INT IDENTITY(1,1),
        time_of_sale DATETIME,
        film_id INT,
        sale_cost_gbp DECIMAL(3,2),

        PRIMARY KEY (sale_id),
        FOREIGN KEY (film_id) REFERENCES film_table (film_id)  ON DELETE CASCADE
    );
```

## Normal Form / Normalisation

NORMALISATION

- Elimination of data redundancies (repeats) to meet a defined form.

TRANSITATIVE FUNCTIONAL DEPENDENCY:

 - When a non-key attribute is functionally dependent on another non-key attribute, which is in turn dependent on the Primary Key.

### First Form
- Everything is as simple is possible
  - Only one value per cell
- No repeating groups

### Second Form
- Meets criteria of first form
- All non-key attributes are fully functionally dependent to primary keys
- If primary key is composite - then each component

### Third Form
- Meets criteria of third form
- There is NO transitative functional dependency


## Queries

Hiding duplicate values:
```SQL
    SELECT DISTINCT Country FROM Customers
    WHERE ContactTitle = 'Owner';
```

Conditional queries:
```SQL
    SELECT attributes FROM table
    WHERE something = something_else;

    SELECT attributes FROM table
    WHERE condition1 = met AND condition2 = met;
```

Finding similarities (Wildcards):
  - % - Substitute for zero or more characters
  - _ - Substitute for single character
  - [charlist] - Sets range of characters to match
    - eg LIKE [ABC]%
    - Returns values that start with either A, B, or C
  - [^charlist] - Sets range of characters to NOT match
    - eg LIKE [^ABC]%
    - Returns values that DO NOT start with A, B, or C

```SQL
    SELECT Country FROM Customers
    WHERE Country LIKE '___M%'


    SELECT Country FROM Customers
    WHERE Country LIKE '[ABC]%'

```

Finding values within multiple attribute cells:
- Alternatively NOT IN

```SQL
    SELECT * FROM Customers
    WHERE Region IN ('WA', 'SP')
```

Finding values within a range:

```SQL
SELECT * FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 06800 AND 09999;
```

Aggregate functions:
  - This is the only time we use the " "

```SQL
    SELECT COUNT(pk) AS "alias" FROM table
    (WHERE clause)
```

Limiting output:
- TOP command sorts attributes lexicographically

```SQL
    SELECT TOP 100 attribute FROM table
    WHERE condition;
```

Concatenation:
- To combine multiple Attributes

```SQL
    SELECT CompanyName AS 'Company Name',
           City + ',' + Country AS 'City'
    FROM Customers
```
