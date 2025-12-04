# PublishedComponentSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The unique identifier for the component set. | 
**file_key** | **String** | The unique identifier of the Figma file that contains the component set. | 
**node_id** | **String** | The unique identifier of the component set node within the Figma file. | 
**thumbnail_url** | Option<**String**> | A URL to a thumbnail image of the component set. | [optional]
**name** | **String** | The name of the component set. | 
**description** | **String** | The description of the component set as entered by the publisher. | 
**created_at** | **String** | The UTC ISO 8601 time when the component set was created. | 
**updated_at** | **String** | The UTC ISO 8601 time when the component set was last updated. | 
**user** | [**models::User**](User.md) | The user who last updated the component set. | 
**containing_frame** | Option<[**models::FrameInfo**](FrameInfo.md)> | The containing frame of the component set. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


