WITH unbanned_users AS (
    SELECT users_id
    FROM Users
    WHERE banned = 'No'
),
unbanned_trips AS (
    SELECT
        t.request_at,
        t.status
    FROM Trips AS t
    WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
      AND t.client_id IN (SELECT users_id FROM unbanned_users)
      AND t.driver_id IN (SELECT users_id FROM unbanned_users)
),
num_cancelled AS (
    SELECT
        request_at,
        COUNT(*) AS c
    FROM unbanned_trips
    WHERE status <> 'completed'
    GROUP BY request_at
),
num_total AS (
    SELECT
        request_at,
        COUNT(*) AS c
    FROM unbanned_trips
    GROUP BY request_at
)

SELECT
    t.request_at AS Day,
    ROUND(COALESCE(c.c, 0) * 1.0 / t.c, 2) AS `Cancellation Rate`
FROM num_total t
LEFT JOIN num_cancelled c
    ON t.request_at = c.request_at
ORDER BY t.request_at;
