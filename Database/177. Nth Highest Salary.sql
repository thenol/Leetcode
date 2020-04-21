
-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

-- 来源：力扣（LeetCode）
-- 链接：https://leetcode-cn.com/problems/nth-highest-salary
-- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set n = N-1;
  RETURN (
      # Write your MySQL query statement below.
      select ifnull(
      (
      select distinct Salary getNthHighestSalary
      from Employee
      order by Salary desc
      limit n, 1
      ), null)
  );
END

-- 作者：Cassie_Q
-- 链接：https://leetcode-cn.com/problems/nth-highest-salary/solution/mysql-177-di-ngao-de-xin-shui-by-cassie_q/
-- 来源：力扣（LeetCode）
-- 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。