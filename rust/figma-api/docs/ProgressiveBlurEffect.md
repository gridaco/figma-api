# ProgressiveBlurEffect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**r#type** | **String** | A string literal representing the effect's type. Always check the type before reading other properties. | 
**visible** | **bool** | Whether this blur is active. | 
**radius** | **f64** | Radius of the blur effect | 
**bound_variables** | Option<[**models::BaseBlurEffectBoundVariables**](BaseBlurEffect_boundVariables.md)> |  | [optional]
**blur_type** | **String** | The string literal 'PROGRESSIVE' representing the blur type. Always check the blurType before reading other properties. | 
**start_radius** | **f64** | The starting radius of the progressive blur | 
**start_offset** | [**models::Vector**](Vector.md) | The starting offset of the progressive blur | 
**end_offset** | [**models::Vector**](Vector.md) | The ending offset of the progressive blur | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


