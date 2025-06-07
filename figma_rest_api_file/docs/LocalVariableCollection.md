# LocalVariableCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The unique identifier of this variable collection. | 
**name** | **String** | The name of this variable collection. | 
**key** | **String** | The key of this variable collection. | 
**modes** | [**Vec<models::LocalVariableCollectionModesInner>**](LocalVariableCollection_modes_inner.md) | The modes of this variable collection. | 
**default_mode_id** | **String** | The id of the default mode. | 
**remote** | **bool** | Whether this variable collection is remote. | 
**hidden_from_publishing** | **bool** | Whether this variable collection is hidden when publishing the current file as a library. | [default to false]
**variable_ids** | **Vec<String>** | The ids of the variables in the collection. Note that the order of these variables is roughly the same as what is shown in Figma Design, however it does not account for groups. As a result, the order of these variables may not exactly reflect the exact ordering and grouping shown in the authoring UI. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


