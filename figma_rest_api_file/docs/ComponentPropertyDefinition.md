# ComponentPropertyDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**r#type** | [**models::ComponentPropertyType**](ComponentPropertyType.md) | Type of this component property. | 
**default_value** | [**models::ComponentPropertyDefinitionDefaultValue**](ComponentPropertyDefinition_defaultValue.md) |  | 
**variant_options** | Option<**Vec<String>**> | All possible values for this property. Only exists on VARIANT properties. | [optional]
**preferred_values** | Option<[**Vec<models::InstanceSwapPreferredValue>**](InstanceSwapPreferredValue.md)> | Preferred values for this property. Only applicable if type is `INSTANCE_SWAP`. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


