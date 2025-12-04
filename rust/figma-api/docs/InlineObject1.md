# InlineObject1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the file as it appears in the editor. | 
**role** | **String** | The role of the user making the API request in relation to the file. | 
**last_modified** | **String** | The UTC ISO 8601 time at which the file was last modified. | 
**editor_type** | **String** | The type of editor associated with this file. | 
**thumbnail_url** | **String** | A URL to a thumbnail image of the file. | 
**version** | **String** | The version number of the file. This number is incremented when a file is modified and can be used to check if the file has changed between requests. | 
**nodes** | [**std::collections::HashMap<String, models::InlineObject1NodesValue>**](inline_object_1_nodes_value.md) | A mapping from node IDs to node metadata. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


