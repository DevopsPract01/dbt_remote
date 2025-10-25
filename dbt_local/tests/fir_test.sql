-- tests/customer_exists.sql
select *
from {{ ref('customer_stg') }}
where customerid = '2822211'