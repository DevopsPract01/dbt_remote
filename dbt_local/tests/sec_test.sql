-- tests/customer_exists.sql
select *
from {{ ref('orders_stg') }}
where  ORDERID=282221