# GetFileNodes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the file as it appears in the editor. | 
**role** | [**models::Role**](Role.md) |  | 
**last_modified** | **String** | The UTC ISO 8601 time at which the file was last modified. | 
**editor_type** | [**models::EditorType**](EditorType.md) |  | 
**thumbnail_url** | **String** | A URL to a thumbnail image of the file. | 
**version** | **String** | The version number of the file. This number is incremented when a file is modified and can be used to check if the file has changed between requests. | 
**nodes** | [**std::collections::HashMap<String, models::GetFileNodesValue>**](GetFileNodesValue.md) | A mapping from node IDs to node metadata. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


