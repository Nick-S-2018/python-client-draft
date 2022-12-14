# SearchRequest

Payload for search operation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [default to ""]
**fulltext_filter** | **object** |  | [optional] 
**attr_filter** | **object** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**max_matches** | **int** |  | [optional] 
**sort** | **[object]** |  | [optional] 
**sort_old** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**aggs** | [**[Aggregation]**](Aggregation.md) |  | [optional] 
**expressions** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**highlight** | [**Highlight**](Highlight.md) |  | [optional] 
**source** | **object** |  | [optional] 
**options** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**profile** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


