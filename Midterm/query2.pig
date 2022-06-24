lineorder = LOAD '/user/ec2-user/lineorder.tbl' USING PigStorage('|') AS (lo_orderkey:int, lo_linenumber:int, lo_custkey:int, lo_partkey:int, lo_suppkey:int, lo_orderdate:int, lo_orderpriority:chararray, lo_shippriority:chararray, lo_quantity:int, lo_extendedprice:int, lo_ordertotalprice:int, lo_discount:int, lo_revenue:int, lo_supplycost:int, lo_tax:int, lo_commitdate:int, lo_shipmode:chararray);

filterDiscount = FILTER lineorder BY lo_discount > 8;
filterQuantity = FILTER filterDiscount BY lo_quantity > 33;
groupQuantity = GROUP filterQuantity BY lo_quantity;
sumRevenue = FOREACH groupQuantity GENERATE group as lo_quantity, SUM(filterQuantity.lo_revenue) as revenue;
STORE sumRevenue INTO 'Query2' using PigStorage(',');

