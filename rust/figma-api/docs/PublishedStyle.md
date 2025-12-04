# PublishedStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | The unique identifier for the style | 
**file_key** | **String** | The unique identifier of the Figma file that contains the style. | 
**node_id** | **String** | ID of the style node within the figma file | 
**style_type** | [**models::StyleType**](StyleType.md) |  | 
**thumbnail_url** | Option<**String**> | A URL to a thumbnail image of the style. | [optional]
**name** | **String** | The name of the style. | 
**description** | **String** | The description of the style as entered by the publisher. | 
**created_at** | **String** | The UTC ISO 8601 time when the style was created. | 
**updated_at** | **String** | The UTC ISO 8601 time when the style was last updated. | 
**user** | [**models::User**](User.md) | The user who last updated the style. | 
**sort_position** | **String** | A user specified order number by which the style can be sorted. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


