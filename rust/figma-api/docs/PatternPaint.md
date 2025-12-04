# PatternPaint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | Option<**bool**> | Is the paint enabled? | [optional][default to true]
**opacity** | Option<**f64**> | Overall opacity of paint (colors within the paint can also have opacity values which would blend with this) | [optional][default to 1]
**blend_mode** | [**models::BlendMode**](BlendMode.md) | How this node blends with nodes behind it in the scene | 
**r#type** | **String** | The string literal \"PATTERN\" representing the paint's type. Always check the `type` before reading other properties. | 
**source_node_id** | **String** | The node id of the source node for the pattern | 
**tile_type** | **String** | The tile type for the pattern | 
**scaling_factor** | **f64** | The scaling factor for the pattern | 
**spacing** | [**models::Vector**](Vector.md) | The spacing for the pattern | 
**horizontal_alignment** | **String** | The horizontal alignment for the pattern | 
**vertical_alignment** | **String** | The vertical alignment for the pattern | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


