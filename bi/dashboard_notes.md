# Dashboard notes

`Meridia_Dashboard.pbix` is built from the eleven UTF-8 CSVs in `bi_export/`, written by section 6 of the notebook.

## Model

- `bi_fact_requests` - one row per closed request (31,502). `missed` is integer 0/1; `pct_1_2star` is already 0-100, not 0-1.
- Five dimension tables (category, department, district, channel, priority) join to the fact table. `bi_sq2_dept_priority`, `bi_sq3_priority` and `bi_sq4_channel` join on their own keys. All nine joins are many-to-one, single direction, with no orphan keys.
- `band` sorts by `band_order`; `priority` sorts by `sort_order`.
- Turn off Auto date/time before loading, or Power BI creates hidden date tables.

## Measures (on `bi_fact_requests`)

```dax
n_requests    = COUNTROWS ( 'bi_fact_requests' )
n_rated       = COUNT ( 'bi_fact_requests'[citizen_rating] )
response_rate = DIVIDE ( COUNT ( 'bi_fact_requests'[citizen_rating] ), COUNTROWS ( 'bi_fact_requests' ) )
on_time_rate  = 1 - AVERAGE ( 'bi_fact_requests'[missed] )
miss_rate     = AVERAGE ( 'bi_fact_requests'[missed] )
median_hours  = MEDIAN ( 'bi_fact_requests'[hours] )
mean_rating   = AVERAGE ( 'bi_fact_requests'[citizen_rating] )
```

`response_rate`, `on_time_rate` and `miss_rate` use the Percentage format; `n_requests` and `n_rated` are whole numbers, `median_hours` has 1 decimal and `mean_rating` 2.

## Pages

**P1 Promise.** Six KPI cards from `bi_kpi_overall`, which stay fixed under slicing: 61.9% on time, 38.1% missed, 72.3 h median, 4.20 mean rating, 34.8% response rate, and 31,502 requests / 10,972 ratings. Charts: mean rating by delay band (4.94 / 4.53 / 3.86 / 3.37 / 2.80 / 2.08) and miss rate by category (12.2% to 53.2%). Slicers: priority, category, channel.

**P2 Gap.** Department x priority rating (18 points, 0.35-0.38 spread per priority), median hours by priority (13.9 / 64.9 / 134.9), rating by channel (4.26 / 4.18 / 4.15 / 4.14). Slicers: priority, department, district. The priority slicer is synced with P1; district is for checking only.

## Conventions

- Bar and column charts start at 0. The department rating axis may start near 3.9 because the spread is the point.
- `bi_sq4_channel.csv` stores three decimals (mobile_app 4.255, in_person 4.175), so Power BI may show 4.25/4.26 and 4.17/4.18. The 0.11-star channel spread is unaffected.
- Okabe-Ito palette; on-screen text in English; conclusions worded as associations, not causes; no budget recommendation by district.
