# Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier for comment. | 
**client_meta** | [**models::CommentClientMeta**](Comment_client_meta.md) |  | 
**file_key** | **String** | The file in which the comment lives | 
**parent_id** | Option<**String**> | If present, the id of the comment to which this is the reply | [optional]
**user** | [**models::User**](User.md) | The user who left the comment | 
**created_at** | **String** | The UTC ISO 8601 time at which the comment was left | 
**resolved_at** | Option<**String**> | If set, the UTC ISO 8601 time the comment was resolved | [optional]
**message** | **String** | The content of the comment | 
**order_id** | Option<**String**> | Only set for top level comments. The number displayed with the comment in the UI | 
**reactions** | [**Vec<models::Reaction>**](Reaction.md) | An array of reactions to the comment | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


