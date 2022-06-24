lineorder = LOAD '/user/ec2-user/lineorder.tbl' USING PigStorage('|') AS (lo_orderkey:int, lo_linenumber:int, lo_custkey:int, lo_partkey:int, lo_suppkey:int, lo_orderdate:int, lo_orderpriority:chararray, lo_shippriority:chararray, lo_quantity:int, lo_extendedprice:int, lo_ordertotalprice:int, lo_discount:int, lo_revenue:int, lo_supplycost:int, lo_tax:int, lo_commitdate:int, lo_shipmode:chararray);

groupDiscount = GROUP lineorder BY lo_discount;
groupAvg = FOREACH groupDiscount GENERATE group as lo_discount, AVG(lineorder.lo_extendedprice);
STORE groupAvg INTO 'Query1' using PigStorage(',');

