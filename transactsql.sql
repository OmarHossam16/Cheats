DECLARE @x int=3; -- Declare Variable
SET @x=5; -- Assign Value
SET @i = SELECT COUNT(*) FROM Table -- @i = num of rows
SELECT DISTINCT --Remove Duplicates
CREATE TABLE #Table -- Temp Table "BAD PERFORMANCE"
INSERT table1 (ID,Name) SELECT ID,Name From table2 -- Insert Column ID,Name in table 1 from table 2 
WHERE EXISTS(SELECT * FROM ..)
CONCAT(col1,', ',col2) -- if null adds space
SUBSTRING('str',1,2) -- ('str',from,to)
IFF(i>3,'Then','Else')
CHOOSE(2,'1','2','3') -- >> 2
COALESCE(name,age) -- Returns the first row	 of (name,age) with non-Null value
NULLIF(first,second) -- first=second > NULL (else) > first
ISNULL(name,'N/A') -- Replace Null with N/A
TRY_CAST('str' AS int) -- Convrt Value from datatype to another & Return Null if datatype incompatible
Convert(char(8),TIMESTAMP,112) -- Same as CAST but adds style for example 112
TRY_PARSE('22/9/2018' AS datetime2 USING 'en-US') --Convert str to datetime & Return Null if datatype incompatible
ISNUMERIC(5) -- True > 1 , False > 0
SYSDATETIME()
SUM() MIN() MAX() COUNT() AVG() -- Aggregation Functions should be with GROUP BY

-- Stored Procedure (Function)
CREATE PROC Function @arg VARCHAR = 'default value'AS -- Declare Function
INSERT Table values(@arg) -- Inserts Data to table
exec Function 'arg passed' -- Execute Function 

CREATE PROC Function @arg VARCHAR = 0 AS
SET @arg = (SELECT COUNT(*) FROM Table Where arg=@arg)
DECLARE @c int
EXEC Function 3, @c OUTPUT
SELECT @c

sp_helptext 'SP_Name' --Gets the Code of the SP
-------------------------------

--Synonym ( Another name for a table )
CREATE SYNONYM Table
FOR dbo.Table
-----------------
--Dynamic SQL C and Can't be in Queries"
DECLARE @sqlcode AS NVARCHAR(256)=
N"SELECT * FROM TABLE";
EXEC sys.sp_executesql @sqlcode;
-------------------------------

--Functions(Can Be in Queries)
CREATE Function dbo.MySUM(@n1,@n2) AS
BEGIN
RETURN @n1+@n2
END --Declare

SELECT FROM TABLE dbo.MySUM(col1,col2) --Call
--------------------------------

-- Triggers "BAD PERFORMANCE !"
CREATE TRIGGER tg_Trigger ON Table
FOR UPDATE AS PRINT 'Triggered!'
UPDATE Table SET... 

CREATE TRIGGER tg_Trigger ON Order -- Update Stock when item is ordered
FOR INSERT AS 
DECLARE @q int=(SELECT Q FROM INSERTED)
DECLARE @id int=(SELECT ID FROM INSERTED)
UPDATE Products
SET Stock=Stock-@q WHERE ID=@id
------------------------------

-- VIEW & CTE
CREATE VIEW ViewTable AS SELECT ID,Name FROM Table --View

WITH CTE_Table AS (SELECT ID,Name FROM Table) --CTE "GOOD PERFORMANCE"
------------------
CREATE SYNONYM dbo.ShortAlias FOR dbo.Long.Obj -- Like AS in Columns		

-- IF --
IF (OBJECT_ID(@Table) IS NOT NULL) -- OBJECT_ID() Get obj_ID else NULL
BEGIN
DROP TABLE @Table
END
ELSE
BEGIN
PRINT 'NOT FOUND'
END
---------

-- WHILE
DECLARE @c INT=0
WHILE @i <5
BEGIN
--Code
END
-----------

-- MERGE
MERGE INTO Table AS T 
USING TableUpdate AS TU
ON T.ID = TU.ID
WHEN MATCHED THEN
--Code for example UPDATE
WHEN NOT MATCHED THEN
--Code for example INSERT
OUTPUT $action, INSERTED.ID,DELETED.ID -- Not Required Just Print Action 
GO
-----------------------

-- TRY CATCH "Not Prefered"
BEGIN TRY
--Code
END TRY
BEGIN CATCH
PRINT 'ERROR'
SELECT ERROR_MESSAGE() --Optional "Logs The Error" (MESSAGE,NUMBER,SEVERITY,PROCEDURE,LINE)
THROW  
END CATCH
-------------

--Transactions ( ALL or NOTHING )
BEGIN TRY
--Code
COMMIT TRANSACTION
END TRY
BEGIN CATCH
--Code
ROLLBACK TRANSACTION

--OR
SET XACT_ABORT ON
COMMIT TRANSACTION
SET XACT_ABORT OFF
-----------------
#CURSERS "BAD PERFORMANCE"
#Index on ForeignKeys "Better Performance"
#Sort DESC "Better Performance"
#Cluster Index "BEST PERFORMANCE"

--METADATA
SELECT * FROM sys.tables --databases columns objects
SELECT @@VERSION AS Version
SELECT SERVERPROPERTY('Collation') AS Collation
SELECT * FROM sys.dm_exec_connections -- Info active connections
SELECT * FROM sys.dm_exec_sessions -- Info active users
EXEC sys.sp_databases; -- Info
EXEC sys.sp_help N'Table'; -- Info
EXEC sys.sp_tables 
@table_name='%' , @table_owner=N'Owner'; --Info
----------------

--Partitioning Windows & Ranking RANK.pdf
SElECT SUM(col) RANK() OVER(PARTITION BY ID)

SELECT ID,Price,
RANK() OVER(PARTITION BY ID ORDER BY Price DESC) AS R,
DENSE_RANK() OVER(PARTITION BY ID ORDER BY Price DESC) AS DR,
ROW_NUMBER() OVER(PARTITION BY ID ORDER BY Price DESC) AS RN,
NTILE(5) OVER(PARTITION BY ID ORDER BY Price DESC) AS N
FROM Table ORDER BY ID;
--------------------------

--LAG & LEAD OFFSETS
SELECT LEAD(col,1,ifnull_defaultvalue)
OVER(ORDER BY col1) --Gets the value of the next 1 row

SELECT LAG(col,1,ifnull_defaultvalue)
OVER(ORDER BY col1) --Gets the value of the pervious 1 row
----------------------

--PIVOTING 
-- COL --> ROW & ROW --> COL
------------

--GROUPING SETS
SELECT ID,Qty,SUM(Qty) FROM Table
GROUP BY GROUPING SETS((ID),(Qty),()) -- Groups Multiple Queries 

--CUBE & ROLLUP