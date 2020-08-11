### May 13
# Join queries

Used to merge data from multiple tables around a condition, think Venn diagrams.

### Inner Join

- A n B
- Join condition = the matching attributes

```SQL
    SELECT ProductID, ProductName, CategoryName

    FROM Products INNER JOIN Categories
    ON categories.categoryID = products.categoryID;
```

### Outer Join

LEFT OUTER

- A
- All rows in A, matching rows in B

```SQL
    SELECT customers.customerid,
           companyName,
           orderid
    FROM customers LEFT JOIN orders
    ON orders.customerid = customers.customerid
```

RIGHT OUTER

- B
- All rows in B, matching rows in A

```SQL
    SELECT customers.customerid,
           companyName,
           orderid
    FROM customers RIGHT JOIN orders
    ON orders.customerid = customers.customerid
```

FULL OUTER

- A u B
- All rows in A and B

```SQL
    SELECT customers.customerid,
       companyName,
       orderid
    FROM customers FULL OUTER JOIN orders
    ON orders.customerid = customers.customerid
```


## Arithmatic Operators

- BODMAS
- % : remainder


### Gross / Net
- Gross Total = Total costs prior to any deductions:

```SQL
    SELECT UnitPrice, Quantity, Discount,
    UnitPrice * Quantity AS "Gross Total"

    FROM OrderDetails;
```


- Net Total = Total costs including any deductions:

```SQL
    SELECT UnitPrice, Quantity, Discount,
    UnitPrice * Quantity * (1 - Discount) AS "Net Total"

    FROM [Order Details];
```

### Order by

```SQL
    SELECT UnitPrice, Quantity, Discount,
    UnitPrice * Quantity * (1 - Discount) AS 'Net Total'
    FROM [Order Details]

    ORDER BY 'Net Total' DESC;
```
- Default ascending order
- Use of alias not mandatory

### Group by

- Groups rows that have the same values into summary rows, like "find the number of customers in each country".

- Often used with aggregate functions  to group the result-set by one or more columns.

```SQL
    SELECT COUNT(CustomerID), Country
    FROM Customers
    GROUP BY Country;
```
- ^^^^^^^^^^^^^^^  Counts the number of IDs within each country

### Aggregate Functions

- Without use of GROUP BY statement, output will be on one row as everything will be processed.

- COUNT()
- MAX()
- MIN()
- SUM()
- AVG()

## String Functions

### Substring

- Creates a substring

```SQL
    SUBSTRING ('string', start, length)

    SELECT SUBSTRING ('SQL Tutorial', 5, 3) AS MatchPosition

                             Returns 'Tut'
```
### CHARINDEX

- Returns index of requested substring (character)
- Indices begin on 1 in SQL, however if not present will default to 0

```SQL
    SELECT CHARINDEX ('a', 'Paddy') AS MatchPosition;

                              Returns '2'
```

```SQL
    SELECT CHARINDEX ('OM', 'Customer') AS MatchPosition;

                              Returns '5'
```

### LEFT or RIGHT

- For the first (left), or last (right) characters

```SQL
    SELECT LEFT('string', 3)
                              Returns 'str'
```


### LTRIM or RTRIM

- Removes spaces at beginning (LTRIM) or end (RTRIM) of a string

```SQL
    SELECT LTRIM('    trim string')
                              Returns 'trim string'
```

### LEN
- Character count

```SQL
SELECT LEN('paddy')
                              Returns 5
```
### REPLACE
- To replace character x with character y

```SQL
    SELECT REPLACE('Paddy', 'P', 'B')
                              Returns 'Baddy'
```

### UPPER or LOWER

- Converts all characters to either UPPERcase or LOWERcase

```SQL
    SELECT UPPER('case')
                              Returns 'CASE'
```

### Escape Sequences

- When wanting to refer to just a ' within queries, use a pair - ''. The second is to end the sequence

```SQL
    SELECT ProductName
    FROM Products
    WHERE CHARINDEX('''', ProductName) != 0
```


## Date Functions

- SELECT GETDATE( ) : Returns current datetime
- SELECT SYSDATETIME ( ) : Returns system datetime
- DATEADD (d, 5, Orderdate) AS "Due Date" : Adds 5 days
- DATEDIFF (d, OrderDate, ShippedDate) AS "Ship Time" : Calculates difference
- YEAR(OrderDate) : Extract year  
  - yy / yyyy to match number of characters
- MONTH(OrderDate) : Extract month
  - m / mm to match number of characters
- DAY(OrderDate) : Extract day
  - d / dd to match number of characters

Date Formatting:
```SQL
    SELECT OrderID, FORMAT(OrderDate, 'dd/MM/yyyy')
    FROM Orders
```

## Case Statements

  - For when you need varying results output based on differing data

```SQL
    SELECT CASE
    WHEN DATEDIFF(d, OrderDate, ShippedDate) < 10 THEN 'On Time'
    ELSE 'Overdue'
    END AS "Status"
    FROM Orders
```
- Single apostrophes for case (cell) name
- Double apostrophes for alias

## Having

Used instead of WHERE when wanting to filter sub-totals / grouped data

```SQL
    SELECT SupplierID,
    SUM(UnitsOnOrder) AS "Total On Order",
    AVG(UnitsOnOrder) AS "Avg On Order"
    FROM Products

    GROUP BY SupplierID
    HAVING AVG(UnitsOnOrder) > 5
```

## Ordering - DEV vs SQL

### Logical Syntax Sequence - DEV

- SELECT
- DISTINCT
- FROM
- WHERE
- GROUP BY
- HAVING
- ORDER BY

### Processing Sequence - SQL

- FROM
- WHERE
- GROUP BY
- HAVING
- SELECT
- DISTINCT
- ORDER BY
