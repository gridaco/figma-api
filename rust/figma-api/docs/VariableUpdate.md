# VariableUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action to perform for the variable. | 
**id** | **String** | The id of the variable to update. | 
**name** | Option<**String**> | The name of this variable. | [optional]
**description** | Option<**String**> | The description of this variable. | [optional]
**hidden_from_publishing** | Option<**bool**> | Whether this variable is hidden when publishing the current file as a library. | [optional][default to false]
**scopes** | Option<[**Vec<models::VariableScope>**](VariableScope.md)> | An array of scopes in the UI where this variable is shown. Setting this property will show/hide this variable in the variable picker UI for different fields. | [optional]
**code_syntax** | Option<[**models::VariableCodeSyntax**](VariableCodeSyntax.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


