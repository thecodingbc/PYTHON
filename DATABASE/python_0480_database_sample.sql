
-- Press Ctrl + Enter to run the sql at the cursor line



-- [EXAMPLE 1] simple select ==================================

-- show me everything inside employee table
select * from Employee


-- show me only firstname, lastname, title inside employee table
select firstname, lastname, title from employee


-- show me only firstname, lastname, title inside employee table, however rename the column name to 'Given Name' & 'SurName'
select firstname as 'Given Name', lastname as 'SurName', title from employee




-- [EXAMPLE 2] use 'where' to specify query condition ==================================

-- show me all your 'IT Staff'
select * from employee where title = 'IT Staff'


-- show me who lives in 'Calgary'
select * from employee where City = 'Calgary'


-- show me all employee whose employeeid is less than 5
select * from employee where EmployeeId != 1



-- [EXAMPLE 3] wildcard % matches any number of characters ================================

-- show me all employee whose lastname starts with letter 'P'
select * from employee where LastName like 'P%'


-- show me all employee whose address ends with 'SW'
select * from employee where address like '%SW'



-- [EXAMPLE 4] wildcard _ matches single character ================================

-- show me all employee whose postalcode like 'T2P __3'
select * from employee where postalcode like 'T2P __3'



-- [EXAMPLE 5] Use 'in' to filter multiple values ===================================

-- show me all employee who lives in 'Edmonton' and 'Lethbridge'
select * from employee where City in ('Edmonton', 'Lethbridge')



-- [EXAMPLE 6] Use between and to filter a range value =============================

-- show me all invoices where customerId is between 5 and 10
select * from Invoice where CustomerId between 5 and 10


-- [EXAMPLE 7] Use null and not null to filter has value or doesn't have value =====
select * from Invoice i where BillingState is null

select * from Invoice i where BillingState is not null