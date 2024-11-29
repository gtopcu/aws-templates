
--------------------------------------------------------------------------------

CREATE TABLE `PROJECT_ID.data_lineage_demo.nyc_green_trips_2021`
COPY `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2021`

--------------------------------------------------------------------------------

CREATE TABLE `PROJECT_ID.data_lineage_demo.total_green_trips_22_21`
AS SELECT vendor_id, COUNT(*) AS number_of_trips
FROM (
     SELECT vendor_id FROM `PROJECT_ID.data_lineage_demo.nyc_green_trips_2022`
     UNION ALL
     SELECT vendor_id FROM `PROJECT_ID.data_lineage_demo.nyc_green_trips_2021`
)
GROUP BY vendor_id

--------------------------------------------------------------------------------

--------------------------------------------------------------------------------

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

SELECT 
    COUNT(*) AS total_trips, 
    SUM(trip_duration) as total_trip_duration
FROM `unicorn-demo-354607.dataset.citibike_trips`
GROUP BY bike_id

--------------------------------------------------------------------------------

For a SQL table of the following format:
score INTEGER
rank INTEGER
refresh_date DATE
create a SELECT statement that select the top 1 rank,
display the score, rank, refresh_date
and order by refresh_date

