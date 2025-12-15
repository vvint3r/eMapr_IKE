<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Presto SQL Cheat Sheet: Basic to Advanced for Airbnb Marketing Analytics

This cheat sheet covers foundational to advanced Presto SQL concepts with Airbnb-focused marketing analytics examples. It emphasizes practical patterns often combined in real queries.

***

## 1. Basic SELECT \& Filtering

```sql
SELECT city, booking_date, bookings
FROM airbnb_bookings
WHERE city = 'Paris' AND booking_date >= DATE '2023-01-01'
ORDER BY booking_date DESC
LIMIT 10
```

*Filter bookings for Paris from 2023 onward.*

***

## 2. Aggregations \& GROUP BY

```sql
SELECT city, COUNT(DISTINCT user_id) AS unique_bookers, SUM(bookings) AS total_bookings
FROM airbnb_bookings
WHERE booking_date BETWEEN DATE '2023-01-01' AND DATE '2023-03-31'
GROUP BY city
ORDER BY total_bookings DESC
```

*Count unique bookers and total bookings per city in Q1 2023.*

***

## 3. Joins

```sql
SELECT c.campaign_name, COUNT(DISTINCT b.user_id) AS users_booked
FROM marketing_campaigns c
LEFT JOIN airbnb_bookings b
  ON c.campaign_id = b.campaign_id
GROUP BY c.campaign_name
ORDER BY users_booked DESC
```

*Analyze bookings attributed to each marketing campaign.*

***

## 4. Window Functions

```sql
SELECT
  city,
  booking_date,
  bookings,
  SUM(bookings) OVER (PARTITION BY city ORDER BY booking_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS bookings_7day_sum,
  AVG(bookings) OVER (PARTITION BY city ORDER BY booking_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS bookings_7day_avg
FROM airbnb_bookings
ORDER BY city, booking_date
```

*7-day rolling sum and average bookings per city.*

***

## 5. Subqueries \& CTEs (WITH Clauses)

```sql
WITH top_campaigns AS (
  SELECT campaign_id, COUNT(*) AS total_clicks
  FROM marketing_clicks
  GROUP BY campaign_id
  ORDER BY total_clicks DESC
  LIMIT 5
)
SELECT c.campaign_name, b.city, COUNT(*) AS bookings
FROM top_campaigns t
JOIN marketing_campaigns c ON t.campaign_id = c.campaign_id
JOIN airbnb_bookings b ON b.campaign_id = c.campaign_id
GROUP BY c.campaign_name, b.city
ORDER BY bookings DESC
```

*Analyze cities contributing to bookings from top 5 campaigns.*

***

## 6. CASE Statements

```sql
SELECT
  booking_date,
  city,
  bookings,
  CASE
    WHEN bookings >= 100 THEN 'High'
    WHEN bookings >= 50 THEN 'Medium'
    ELSE 'Low'
  END AS booking_volume_category
FROM airbnb_bookings
WHERE booking_date BETWEEN DATE '2023-01-01' AND DATE '2023-01-31'
```

*Categorize booking volume by city and date.*

***

## 7. String Functions \& Pattern Matching

```sql
SELECT
  user_email,
  SUBSTR(user_email, INSTR(user_email, '@') + 1) AS email_domain
FROM users
WHERE email_domain LIKE '%gmail.com%'
```

*Extract and filter users by email domain for targeted campaigns.*

***

## 8. Combining Aggregation, Joins \& Window Functions

```sql
WITH daily_bookings AS (
  SELECT city, booking_date, COUNT(*) AS bookings
  FROM airbnb_bookings
  GROUP BY city, booking_date
)
SELECT
  city,
  booking_date,
  bookings,
  SUM(bookings) OVER (PARTITION BY city ORDER BY booking_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS bookings_last_7_days,
  RANK() OVER (PARTITION BY city ORDER BY booking_date DESC) AS recent_booking_rank
FROM daily_bookings
WHERE booking_date BETWEEN DATE '2023-03-01' AND DATE '2023-03-31'
ORDER BY city, booking_date
```

*Track 7-day booking totals and rank recent dates per city.*

***

## 9. Handling Missing Dates with Calendar Table (Essential for Moving Averages)

```sql
WITH calendar AS (
  SELECT sequence_date
  FROM
    (SELECT min(booking_date) AS start_date, max(booking_date) AS end_date FROM airbnb_bookings) AS bounds,
    UNNEST(sequence(bounds.start_date, bounds.end_date, INTERVAL '1' DAY)) AS t(sequence_date)
), bookings_filled AS (
  SELECT
    c.sequence_date AS booking_date,
    COALESCE(b.bookings, 0) AS bookings,
    b.city
  FROM calendar c
  CROSS JOIN (SELECT DISTINCT city FROM airbnb_bookings) cities
  LEFT JOIN airbnb_bookings b
    ON b.booking_date = c.sequence_date AND b.city = cities.city
)
SELECT
  city,
  booking_date,
  AVG(bookings) OVER (
    PARTITION BY city
    ORDER BY booking_date
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS moving_avg_7d
FROM bookings_filled
ORDER BY city, booking_date
```

*Create complete date sets and compute accurate 7-day moving averages.*

***

This sequence clearly builds from simple selects, through aggregation and joins, to sophisticated windowing and data preparation—crucial for Airbnb marketing analysis like campaign attribution, booking trends, and customer segmentation.

