# Write your MySQL query statement below
SELECT D.Name AS Department, E1.Name AS Employee, E1.Salary AS Salary
FROM Employee AS E1, Department AS D
# Does E1 havea  top three salary in department?
WHERE
(
    # This is a subquery
    # How many salaries in the same department as E1 are larger?
    SELECT COUNT(DISTINCT E2.salary)
    FROM Employee AS E2
    # E2 is every other employee
    WHERE E1.DepartmentId = E2.DepartmentId AND E2.Salary > E1.Salary
) < 3
AND E1.DepartmentId = D.id;