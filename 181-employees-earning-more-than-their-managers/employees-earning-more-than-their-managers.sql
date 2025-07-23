SELECT s.name AS Employee
FROM Employee s
join Employee m on s.managerId=m.id
where s.salary>m.salary;

-- SELECT e.name AS Employee
-- FROM Employee e
-- JOIN Employee m
--   ON e.managerId = m.id
-- WHERE e.salary > m.salary;
