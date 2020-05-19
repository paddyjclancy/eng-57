### May 14
# Sub-queries

- A nested query WITHIN another select statement
- Allows you to take results of one query and apply them to another


- Nested query is INNER query
  - Held in ( )
  - SQL Processing Sequence does this first
- Main query is OUTER query

```SQL
    SELECT CompanyName AS "Customer"
    FROM Customers
    WHERE CustomerID NOT IN
        (SELECT CustomerID FROM Orders)
```

Creating a new column using a sub-query:

```SQL
    SELECT OrderID, ProductID, UnitPrice, Quantity, Discount,
        (SELECT MAX(UnitPrice) FROM [Order Details]) AS "Max Price"
    FROM [Order Details];
```

# Derived Tables

- Creating a table through a subquery
- Then creating a join


- When making, test subquery functionality first

```SQL
    SELECT od.ProductID, sq1.totalamt AS "Total Sold for this Product",
    UnitPrice, UnitPrice/totalamt*100 AS "% of Total"
        FROM [Order Details] od
        INNER JOIN
            (SELECT ProductID, SUM(UnitPrice*Quantity) AS totalamt
            FROM [Order Details]
            GROUP BY ProductID) sq1 ON sq1.ProductID=od.ProductID;
```

# UNION, UNION ALL

- Creates single column from two queries
- UNION ALL shows duplicate values

```SQL
    SELECT EmployeeID AS "Employee/Supplier"
    FROM Employees
    UNION
    SELECT SupplierID
    FROM Suppliers;
```

# Intersect

- Only returns the commonality between two queries

```SQL
    SELECT EmployeeID AS "Employee/Supplier"
    FROM Employees
    INTERSECT
    SELECT SupplierID
    FROM Suppliers;
```

# Except

- Returns data that is in query 1 ONLY
  - Not in the Intersect

```SQL
    SELECT EmployeeID AS "Employee/Supplier"
    FROM Employees
    EXCEPT
    SELECT SupplierID
    FROM Suppliers;
                    --In Northwind this will return no values
```
