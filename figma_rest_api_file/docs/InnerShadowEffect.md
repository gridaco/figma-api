# InnerShadowEffect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**models::Rgba**](RGBA.md) | The color of the shadow | 
**blend_mode** | [**models::BlendMode**](BlendMode.md) | Blend mode of the shadow | 
**offset** | [**models::Vector**](Vector.md) | How far the shadow is projected in the x and y directions | 
**radius** | **f64** | Radius of the blur effect (applies to shadows as well) | 
**spread** | Option<**f64**> | The distance by which to expand (or contract) the shadow.  For drop shadows, a positive `spread` value creates a shadow larger than the node, whereas a negative value creates a shadow smaller than the node.  For inner shadows, a positive `spread` value contracts the shadow. Spread values are only accepted on rectangles and ellipses, or on frames, components, and instances with visible fill paints and `clipsContent` enabled. When left unspecified, the default value is 0. | [optional][default to 0]
**visible** | **bool** | Whether this shadow is visible. | 
**bound_variables** | Option<[**models::BaseShadowEffectBoundVariables**](BaseShadowEffect_boundVariables.md)> |  | [optional]
**r#type** | Option<**String**> | A string literal representing the effect's type. Always check the type before reading other properties. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


