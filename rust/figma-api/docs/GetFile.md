# GetFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the file as it appears in the editor. | 
**role** | [**models::Role**](Role.md) |  | 
**last_modified** | **String** | The UTC ISO 8601 time at which the file was last modified. | 
**editor_type** | [**models::EditorType**](EditorType.md) |  | 
**thumbnail_url** | Option<**String**> | A URL to a thumbnail image of the file. | [optional]
**version** | **String** | The version number of the file. This number is incremented when a file is modified and can be used to check if the file has changed between requests. | 
**document** | [**models::DocumentNode**](DocumentNode.md) |  | 
**components** | [**std::collections::HashMap<String, models::Component>**](Component.md) | A mapping from component IDs to component metadata. | 
**component_sets** | [**std::collections::HashMap<String, models::ComponentSet>**](ComponentSet.md) | A mapping from component set IDs to component set metadata. | 
**schema_version** | **f64** | The version of the file schema that this file uses. | [default to 0]
**styles** | [**std::collections::HashMap<String, models::Style>**](Style.md) | A mapping from style IDs to style metadata. | 
**link_access** | Option<**String**> | The share permission level of the file link. | [optional]
**main_file_key** | Option<**String**> | The key of the main file for this file. If present, this file is a component or component set. | [optional]
**branches** | Option<[**Vec<models::GetFileBranchesItem>**](GetFileBranchesItem.md)> | A list of branches for this file. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


