{{ config(materialized='table',alias='fir_exp',schema='PUBLIC',database='SLEEKMART_OMS') }}
select {{ var('test_value_first')}} as id,'{{ var('test_value_sec')}}' as name,
{{ var('test_value_third')}} as availability