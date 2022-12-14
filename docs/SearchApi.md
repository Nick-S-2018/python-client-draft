# manticoresearch.SearchApi

All URIs are relative to *http://127.0.0.1:9308*

Method | HTTP request | Description
------------- | ------------- | -------------
[**percolate**](SearchApi.md#percolate) | **POST** /json/pq/{index}/search | Perform reverse search on a percolate index
[**search**](SearchApi.md#search) | **POST** /json/search | Performs a search


# **percolate**
> SearchResponse percolate(index,percolate_request)

Perform reverse search on a percolate index

Performs a percolate search. 
This method must be used only on percolate indexes.

Expects two parameters: the index name and an object with array of documents to be tested.
An example of the documents object:

  ```
  {"query":{"percolate":{"document":{"content":"sample content"}}}}
  ```

Responds with an object with matched stored queries: 

  ```
  {'timed_out':false,'hits':{'total':2,'max_score':1,'hits':[{'_index':'idx_pq_1','_type':'doc','_id':'2','_score':'1','_source':{'query':{'match':{'title':'some'},}}},{'_index':'idx_pq_1','_type':'doc','_id':'5','_score':'1','_source':{'query':{'ql':'some | none'}}}]}}
  ```


### Example

```python
import manticoresearch
from manticoresearch.api import search_api
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.search_response import SearchResponse
from manticoresearch.model.percolate_request import PercolateRequest
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    index = "index_example" # str | Name of the percolate index
    percolate_request = PercolateRequest(
        query={},
    ) # PercolateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Perform reverse search on a percolate index
        api_response = api_instance.percolate(index, percolate_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling SearchApi->percolate: %s\n" % e)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Name of the percolate index | 
 **percolate_request** | [**PercolateRequest**](PercolateRequest.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | items found |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResponse search(search_request)

Performs a search


Expects an object with mandatory properties:
* the index name
* the match query object
Example :

  ```
  {'index':'movies','query':{'bool':{'must':[{'query_string':' movie'}]}},'script_fields':{'myexpr':{'script':{'inline':'IF(rating>8,1,0)'}}},'sort':[{'myexpr':'desc'},{'_score':'desc'}],'profile':true}
  ```

It responds with an object with:
- time of execution
- if the query is timed out
- an array with hits (matched documents) found
- if profiling is enabled, an additional array with profiling information attached


  ```
  {'took':10,'timed_out':false,'hits':{'total':2,'hits':[{'_id':'1','_score':1,'_source':{'gid':11}},{'_id':'2','_score':1,'_source':{'gid':12}}]}}
  ```

Alternatively, you can use auxillary query objects to build your search queries as it's shown in the example below.
For more information about the match query syntax and additional parameters that can be added to  request and response, please check: https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP.


### Example

```python
import manticoresearch
from manticoresearch.api import search_api
from manticoresearch.model.search_request import SearchRequest
from manticoresearch.model.error_response import ErrorResponse
from manticoresearch.model.search_response import SearchResponse
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:9308
# See configuration.py for a list of all supported configuration parameters.
configuration = manticoresearch.Configuration(
    host = "http://127.0.0.1:9308"
)


# Enter a context with an instance of the API client
with manticoresearch.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search_api.SearchApi(api_client)
    search_request = SearchRequest(
        index="test",
        fulltext_filter=,
        attr_filter=,
        limit=1,
        offset=1,
        max_matches=1,
        sort=[
            ,
        ],
        sort_old=[{"test":"asc"},"id"],
        aggs=[
            Aggregation(
                name="agg1",
                field="field1",
                size=10,
            ),
        ],
        expressions=[
            {},
        ],
        highlight=Highlight(),
        source=,
        options={},
        profile=True,
    ) # SearchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Performs a search
        api_response = api_instance.search(search_request)
        pprint(api_response)
    except manticoresearch.ApiException as e:
        print("Exception when calling SearchApi->search: %s\n" % e)


    # An example of the alternative way to build search requests using auxillary query objects
    search_req = manticoresearch.model.SearchRequest()
          
    #Setting a search index:
    search_req.index = 'test'
  
    #Setting extra search settings:
    search_req.offset = 0
    search_req.limit = 10
    search_req.profile = True
    search_req.options = {'ranker': 'bm25'}
    #For detailed information on search options see https://manual.manticoresearch.com/Searching/Options#Search-options   

    #Setting the `_source` property:
    search_req.source = 'field1'
    search_req.source = ['field1', 'field2*']

    #setting `_source` property with auxillary object
    search_req.source = manticoresearch.model.SourceByRules()
    search_req.source.includes = ['field1', 'field2*']
    search_req.source.excludes = ['field3']
    #For detailed information on the `source` property see https://manual.manticoresearch.com/Searching/Search_results#Source-selection

    #Setting the `sort` property:
    search_req.sort = ['body']

    #setting `sort` property with auxillary obejcts
    sort2 = manticoresearch.model.SortOrder('price', 'desc')
    sort3 = manticoresearch.model.SortMVA('codes', 'desc', 'max')
    search_req.sort += [sort2,sort3]
    #For detailed information on sorting see https://manual.manticoresearch.com/Searching/Sorting_and_ranking#HTTP

    #Setting the `expressions` property:
    expr = {'expr': 'min(price,15)'}
    search_req.expressions = [expr]
    search_req.expressions += [ {'expr2': 'max(price,15)'} ]
    #For detailed information on expressions see https://manual.manticoresearch.com/Searching/Expressions#Expressions-in-HTTP-JSON
    
    #Setting the `aggs` property with auxillary object:
    agg1 = manticoresearch.model.Aggregation('agg1', 'body', 10)
    search_req.aggs = [agg1] + [ manticoresearch.model.Aggregation('agg2', 'price') ]
    #For detailed information on aggregations see https://manual.manticoresearch.com/Searching/Faceted_search#Aggregations

    #Settting the `highlight` property with auxillary object:
    highlight = manticoresearch.model.Highlight()
    highlight.fieldnames = ['body']
    highlight.test = 1
    highlight.post_tags = '</post_tag>'
    highlight.encoder = 'default'
    highlight.snippet_boundary = 'sentence'
    search_req.highlight = highlight 

    # settting `highlight.fields` property with auxillary object
    highlightField = manticoresearch.model.HighlightField('body')
    highlightField2 = manticoresearch.model.HighlightField('price', 5, 10)
    highlight.fields = [highlightField, highlightField2]
    search_req.highlight = highlight 
    #For detailed information on highlighting see https://manual.manticoresearch.com/Searching/Highlighting#Highlighting

    #Setting the `fulltext_filter` property using different filter objects:
    search_req.fulltext_filter = manticoresearch.model.QueryFilter('test')
    search_req.fulltext_filter = manticoresearch.model.MatchFilter('test', 'title')
    search_req.fulltext_filter = manticoresearch.model.MatchPhraseFilter('test phrase', 'title')
    search_req.fulltext_filter = manticoresearch.model.MatchOpFilter('test1 test2', 'title', 'and')
    #For detailed information on fulltext filters see https://manual.manticoresearch.com/Searching/Full_text_matching/Basic_usage#HTTP

    #Setting the `attr_filter` property using different filter objects:
    search_req.attr_filter = manticoresearch.model.EqualsFilter('price', 20)
    
    inFilter = manticoresearch.model.InFilter('price', [1,2])
    inFilter.values += [10,11]
    search_req.attr_filter = inFilter
    
    rangeFilter = manticoresearch.model.RangeFilter('price', lte = 20)
    rangeFilter.gte = 5
    search_req.attr_filter = rangeFilter
    rangeFilter.gt = 100
    rangeFilter.lt = 200
    search_req.attr_filter = rangeFilter
    
    geoFilter = manticoresearch.model.GeoDistanceFilter(location_anchor={'lat':10,'lon':20}, location_source='field1,field2')
    geoFilter.location_source='field3,field4'
    geoFilter.distance_type='adaptive'
    geoFilter.distance='100 km'
    search_req.attr_filter = geoFilter
    #For detailed information on range filters see https://manual.manticoresearch.com/Searching/Filters#Range-filters
    #For detailed information on geo distance filters see https://manual.manticoresearch.com/Searching/Filters#Geo-distance-filters

    #Setting the `attr_filter` property using bool filter object:
    boolFilter = manticoresearch.model.BoolFilter()
    boolFilter.must_not = [ manticoresearch.model.EqualsFilter('body', 'test') ]
    search_req.attr_filter = boolFilter
    
    fulltext_filter = manticoresearch.model.MatchFilter('test', 'title')
    nestedBoolFilter = manticoresearch.model.BoolFilter()
    nestedBoolFilter.should = [manticoresearch.model.EqualsFilter('code', 'a'), fulltext_filter]
    boolFilter.must = [nestedBoolFilter]
    
    boolFilter.must += [ manticoresearch.model.EqualsFilter('price', 10) ]
    search_req.attr_filter = boolFilter
    #For detailed information on Bool queries see https://manual.manticoresearch.com/Searching/Filters#bool-query
    
    #Sending the search request we've built and getting the response:
    pprint(search_req)
    api_response = search_api.search(search_req)
    pprint(api_response)

```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

