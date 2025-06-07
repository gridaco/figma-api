# DirectionalTransition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**r#type** | **String** |  | 
**direction** | **String** |  | 
**duration** | **f64** | The duration of the transition in milliseconds. | 
**easing** | [**models::Easing**](Easing.md) | The easing curve of the transition. | 
**match_layers** | Option<**bool**> | When the transition `type` is `\"SMART_ANIMATE\"` or when `matchLayers` is `true`, then the transition will be performed using smart animate, which attempts to match corresponding layers an interpolate other properties during the animation. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


