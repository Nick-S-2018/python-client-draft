import manticoresearch 
import sys
from pprint import pprint

configuration = manticoresearch.Configuration(
    host = "http://localhost:9308"
)
client = manticoresearch.ApiClient(configuration)
search_api = manticoresearch.SearchApi(client)

configuration.client_side_validation = False
#print(configuration.client_side_validation)

#query = manticoresearch.model.Query( manticoresearch.model.Match() )

search_req = manticoresearch.model.SearchRequest()

# sort1 = 'body'
# sort2 = manticoresearch.model.SortOrder('price', 'desc')
# sort3 = manticoresearch.model.SortMVA('codes', 'desc', 'max')
#print(search_req.max_matches)
search_req.index = 'test'
# search_req.offset = 0
# search_req.limit = 2
# search_req.max_matches = 2
# search_req.profile = True
# search_req.options = {'ranker': 'bm25'}
# search_req.sort = [sort1,sort2,sort3]

# search_req.source = 'body'
# search_req.source = ['body', 'pric*']
# search_req.source = manticoresearch.model.SourceByRules()
#search_req.source.excludes = ['body']

# expr = {'expr': 'min(price,15)'}
# search_req.expressions = [expr]
# search_req.expressions += [{'expr2': 'max(price,15)'}]
#
# agg1 = manticoresearch.model.Aggregation('agg1', 'body', 10)
# search_req.aggs = [agg1] + [ manticoresearch.model.Aggregation('agg2', 'price') ]

# highlight = manticoresearch.model.Highlight()
# highlight.fieldnames = ['body']
# highlight.test = 1
# highlight.post_tags = 'q'
# highlight.encoder = 'default'
# highlight.snippet_boundary = 'sentence'
#
# highlightField = manticoresearch.model.HighlightField('body')
# highlightField2 = manticoresearch.model.HighlightField('price', 5, 10)
# highlight.fields = [highlightField, highlightField2]
# search_req.highlight = highlight 


# search_req.fulltext_filter = manticoresearch.model.QueryFilter('qaz')
# search_req.fulltext_filter = manticoresearch.model.MatchFilter('qaz', 'title')
# search_req.fulltext_filter = manticoresearch.model.MatchPhraseFilter('qaz', 'title')
# search_req.fulltext_filter = manticoresearch.model.MatchOpFilter('qaz zaq', 'title', 'and')
# search_req.fulltext_filter = manticoresearch.model.MatchFilter('qaz', 'title')

# search_req.attr_filter = manticoresearch.model.EqualsFilter('price', 20)
# search_req.attr_filter = manticoresearch.model.InFilter('price', [11,12,10])
#
# rangeFilter = manticoresearch.model.RangeFilter('price', lte = 20)
# search_req.attr_filter = rangeFilter

# geoFilter = manticoresearch.model.GeoDistanceFilter(location_anchor={'lat':10,'lon':20})
# geoFilter.location_source='price,body'
# geoFilter.distance_type='adaptive'
# geoFilter.distance='100 km'
# search_req.attr_filter = geoFilter

boolFilter = manticoresearch.model.BoolFilter()
fulltext_filter = manticoresearch.model.MatchFilter('qaz', 'title')
nestedBoolFilter = manticoresearch.model.BoolFilter()
nestedBoolFilter.should = [manticoresearch.model.EqualsFilter('body', ['edc']),fulltext_filter]
boolFilter.must = [manticoresearch.model.EqualsFilter('price', 20),nestedBoolFilter]
search_req.attr_filter = boolFilter

#pprint(search_req.fulltext_filter.to_dict())
pprint(search_req)

api_resp = search_api.search(search_req)
print(api_resp)

sys.exit()

search_req1 = {'index':'test', 'query': { 'bool': { 'must': [{'equals': {'price': 2}}]}}}
pprint(search_req1)


api_resp = search_api.search(search_req1)
print(api_resp)

print(req['query']['bool']['must'][0])
print(search_req1['query']['bool']['must'][0])
print(req['query']['bool']['must'][0] == search_req1['query']['bool']['must'][0])

sys.exit()
search_req.max_matches = 1
match = manticoresearch.model.Match()
match.query_string = ''
highlight = manticoresearch.model.Highlight()
highlight.fields = ['content']
search_req1 = {
    'index':'test',
    'query': {'match': {match.query_fields: match.query_string}},
    'highlight': highlight
}
api_resp = search_api.search(search_req1)
print(api_resp)

search_req.index = 'test'
search_req.query = manticoresearch.model.Query()
search_req.query.match = match
#search_req.query = {'match': {'*': 'qaz'}}
search_req.highlight = highlight
print(search_req)
api_resp = search_api.search(search_req)
print(api_resp)
