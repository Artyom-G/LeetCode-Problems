# Write your MySQL query statement below
WITH salaries_by_department AS (
    SELECT DISTINCT d.name as dep_name, e.salary as sal FROM department AS d, employee AS e
    WHERE e.departmentID = d.id
), 
top_1_by_dep AS (
    SELECT dep_name, MAX(sal) as m_sal from salaries_by_department
    GROUP BY dep_name
),
top_2_by_dep AS (
    SELECT s.dep_name, MAX(s.sal) as m_sal FROM salaries_by_department as s, top_1_by_dep as t1
    WHERE s.dep_name = t1.dep_name and s.sal != t1.m_sal
    GROUP BY dep_name
),
top_3_by_dep AS (
    SELECT s.dep_name, MAX(s.sal) as m_sal FROM salaries_by_department as s, top_1_by_dep as t1, top_2_by_dep as t2
    WHERE s.dep_name = t1.dep_name and s.dep_name = t2.dep_name and s.sal != t1.m_sal and s.sal != t2.m_sal
    GROUP BY dep_name
),
top_sals_by_dep as (
    SELECT * FROM top_1_by_dep
    UNION
    SELECT * FROM top_2_by_dep
    UNION
    SELECT * FROM top_3_by_dep
)

SELECT t.dep_name as Department, e.name as Employee, t.m_sal as Salary FROM employee as e, top_sals_by_dep as t, department as d
WHERE e.salary = t.m_sal and t.dep_name = d.name and e.departmentId = d.id
