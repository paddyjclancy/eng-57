### May 11
# Introduction to SQL

Structured Query Language

## Terminology:

- Entity - Any object holding data, eg table
- Column - Alternatively attributes
- Rows   - Alternatively records, tuples
- DBMS   - Database Management System. Allows computer to perform database CRUD functions, eg Azure, MySQL, etc
- CRUD   - Create, Read, Update, Delete

## Table Relations

- Tables should be RELATIONAL
- [Table Name] : Square brackets for when referring to tables with spaces

### Keys:
- Primary Keys
  - Unique values
  - Only one per table
  - Can't be modified
  - Can't be null
    - eg "customer_id"


  - Composite Keys
      - Combination of two columns to create primary


  - Candidate Keys
    - Multiple primaries present
    - Requires selection of primary
      - NHS / NIS numbers

- Foreign Keys
  - Pointer / reference attribute for cross-relations
  - Can't be modified
  - Can't be null
  - Must exist as a primary key in table for reference


- Unique Keys
  - Attributes configured so no value may be repeated within
  - Can me null
  - Can be modified
  - eg "email", "NIS_num", etc...

### Relationship Types

- One to One
  - One row in A relates to one row in B


- One to Many
  - One row in A relates to multiple rows in B


- Many to Many
  - Multople rows in A relate to multiple rows in B
  - Requires two "One to Many" tables and a junction table
    - Junction table links primary keys from A and B (but are    foreign keys in this table)

## Data
### Database Management Systems - DBMS
Database Management System (DBMS) is a collection of programs which enables its users to access database, manipulate data, reporting / representation of  data .

- Hierarchical / Navigational
  - Supports parent-child relationship types
  - Tree structure
    - Nodes representing records
    - Branches representing fields
  - eg Windows Registry (Windows XP)
- Network
  - Supports many-to-many
  - Complex structures
  - eg RDM Server
- Relational
  - Defines database relationships in table / relationship form
  - Does not support many-to-many
  - eg SQL, MongoDB, Oracle
- Object Orientated
  - Allow the integration of databases, operating systems, spreadsheets, languages, AI systems, word processors, and other objects or applications.
  - Not very common currently

### Data Languages

- DML - Data Manipulation Language
  - Select
  - Insert
  - Update
  - Delete


- DDL - Data Definition Language
  - Create
  - Alter
  - Drop
  - Truncate
    - (Delete everything, leaving empty table)


- DCL - Data Control Language
  - Used by admin to allow access to devs
    - Grant
    - Revoke


- TCL - Transaction Control Language
  - Commit
  - Rollback
  - Savepoint

To create database within a server:

```SQL
    CREATE DATABASE database_name
```

To switch database once in a server, either use drop down box or command:

```SQL
    USE database_name
```
Excel (flat file) can be used to make a database, however it is lacking extensive command functionality - SQL programe are therefore more ideal.

### Data Types

- CHAR
  - Fixed length
  - 50% Faster retrieval
- VARCHAR("max value")
  - Adaptable length
  - More memory efficient
- INT
- DATETIME
- DECIMAL / NUMERIC
- FLOAT
  - Large numbers
- BINARY
  - Image / file
- BIT
  - Equivalent to binary / booleans
  - 0 / 1 / NULL


```SQL
    SP_HELP table_name
```

### Creating a Table

```SQL
    CREATE TABLE film_table
      (
        film_id INT IDENTITY(1,1),
        film_name VARCHAR(20),
        film_type VARCHAR(10),
        release_date DATE,
        director VARCHAR(20),
        writer VARCHAR(20),
        film_language VARCHAR(15),
        website_url VARCHAR(50),
        summary VARCHAR
      );
```
### Adding an Attribute
```SQL
    ALTER TABLE film_table
    ADD producer VARCHAR(20), rating INT;
```

```SQL    
    INSERT INTO film_table
    (
        producer, rating
    )
    VALUES
    (
        'Spielberg', 5
    );
```
```SQL
    INSERT INTO table_name (column1, column2, column3, ...)
    VALUES (value1, value2, value3, ...);
```
### Editing an Attribute
```SQL
    ALTER TABLE film_table
      ALTER COLUMN film_name VARCHAR(20) NOT NULL;
```

### Removing an Attribute
```SQL
    ALTER TABLE film_table
      DROP COLUMN film_name;
```
