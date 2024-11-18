select
select client_id, name as asset_name,
maturity_date as event_date from bonds
WHERE maturity_date >= '2023-09-01' AND maturity_date <= '2024-08-31' UNION
select client_id, name as asset_name,
dividend_date as event_date from stocks
WHERE dividend_date >= '2023-09-01' AND dividend_date <= '2024-08-31'
order by event_date

//'Stock Dividend Payment' as event_type


UNION
select client_id, name as asset_name,
dividend_date as event_date from stocks
WHERE dividend_date >= '2023-09-01' AND dividend_date <= '2024-08-31'