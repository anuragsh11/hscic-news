Steps to run searchNews.py
python searchNews -h usage: searchNews.py [-h] searchtype Value

Search your keyword example: searchNews.py AND A,B,C

positional arguments:
  searchtype  Search type OR and AND only
  Value       Parameter to search

optional arguments:
  -h, --help  show this help message and exit

example :

search using "OR" method

python searchNews.py OR September,2004 
9

search using AND

python searchNews.py AND September,2004 
1

Steps to run Unit testing

go to folder where the searchNews.py and test_sample are present in command prompt

run

1: pytest
-To run all test cases

2:pytest -rp
- To run all test cases and get passed test summary

3: pytest -ra
- to run all test cases and get the short test summary info
pytest module will fetch the test_*.py file and start running the test inside that

Part2
Raik = not available
Cache create for result 1
curl -s -X PUT -H "Content-Type: text/plain" -d "0 1 2 3 4 5 6" "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“Care,Quality,Commission"
Cache create for result 2
Cache create for result 2 curl -s -X PUT -H "Content-Type: text/plain" -d “9” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“September,2004"
Cache create for result 3
Cache create for result 3 curl -s -X PUT -H "Content-Type: text/plain" -d “6 8” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“general,population,generally"
Cache create for result 4
Cache create for result 4 curl -s -X PUT -H "Content-Type: text/plain" -d “1” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“Care,Quality,Commission,admission"
Cache create for result 5
Cache create for result 5 curl -s -X PUT -H "Content-Type: text/plain" -d “6” "http://$RIAK_HTTP_IP:$RIAK_HTTP_PORT/buckets/$RIAK_TEST_BUCKET/keys/“general,population,Alzheimer"
$KEY = “Care,Quality,Commission”

Retrive data from cache
Retrive data from cache CACHE_VALUE=$(redis-cli -h "$CACHE_PROXY_IP" -p "$CACHE_PROXY_PORT" "$RIAK_TEST_BUCKET:$KEY”)
Insert value with index
Curl -X put -H "Content-Type: text/plain" -d "April 15 , 2013 Thousands of GP practices ..." http://localhost:8098/buckets/indexname/hscicNews/keys/RESULT:5
Display key for document June 2013
Curl -I http://localhost:8098/buckets/indexname/hscicNews//keys=true