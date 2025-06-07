# LocalVariable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The unique identifier of this variable. | 
**name** | **String** | The name of this variable. | 
**key** | **String** | The key of this variable. | 
**variable_collection_id** | **String** | The id of the variable collection that contains this variable. | 
**resolved_type** | **String** | The resolved type of the variable. | 
**values_by_mode** | [**std::collections::HashMap<String, models::LocalVariableValuesByModeValue>**](LocalVariable_valuesByMode_value.md) | The values for each mode of this variable. | 
**remote** | **bool** | Whether this variable is remote. | 
**description** | **String** | The description of this variable. | 
**hidden_from_publishing** | **bool** | Whether this variable is hidden when publishing the current file as a library.  If the parent `VariableCollection` is marked as `hiddenFromPublishing`, then this variable will also be hidden from publishing via the UI. `hiddenFromPublishing` is independently toggled for a variable and collection. However, both must be true for a given variable to be publishable. | 
**scopes** | [**Vec<models::VariableScope>**](VariableScope.md) | An array of scopes in the UI where this variable is shown. Setting this property will show/hide this variable in the variable picker UI for different fields.  Setting scopes for a variable does not prevent that variable from being bound in other scopes (for example, via the Plugin API). This only limits the variables that are shown in pickers within the Figma UI. | 
**code_syntax** | [**models::VariableCodeSyntax**](VariableCodeSyntax.md) |  | 
**deleted_but_referenced** | Option<**bool**> | Indicates that the variable was deleted in the editor, but the document may still contain references to the variable. References to the variable may exist through bound values or variable aliases. | [optional][default to false]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


