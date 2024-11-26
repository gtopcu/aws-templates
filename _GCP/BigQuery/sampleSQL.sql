

-- This query shows a list of the daily top Google Search terms.
SELECT
   refresh_date AS Day,
   term AS Top_Term,
       -- These search terms are in the top 25 in the US each day.
   rank,
FROM `bigquery-public-data.google_trends.top_terms`
WHERE
   rank = 1
       -- Choose only the top term each day.
   AND refresh_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 2 WEEK)
       -- Filter to the last 2 weeks.
GROUP BY Day, Top_Term, rank
ORDER BY Day DESC


--------------------------------------------------------------------------------

SELECT
  name,
  SUM(number) AS total
FROM
  `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY
  name
ORDER BY
  total DESC
LIMIT
  10;

--------------------------------------------------------------------------------