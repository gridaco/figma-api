# WidgetNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A string uniquely identifying this node within the document. | 
**name** | **String** | The name given to the node by the user in the tool. | 
**visible** | Option<**bool**> | Whether or not the node is visible on the canvas. | [optional][default to true]
**locked** | Option<**bool**> | If true, layer is locked and cannot be edited | [optional][default to false]
**is_fixed** | Option<**bool**> | Whether the layer is fixed while the parent is scrolling | [optional][default to false]
**scroll_behavior** | **String** | How layer should be treated when the frame is resized | [default to Scrolls]
**rotation** | Option<**f64**> | The rotation of the node, if not 0. | [optional][default to 0]
**component_property_references** | Option<**std::collections::HashMap<String, String>**> | A mapping of a layer's property to component property name of component properties attached to this node. The component property name can be used to look up more information on the corresponding component's or component set's componentPropertyDefinitions. | [optional]
**plugin_data** | Option<[**serde_json::Value**](.md)> |  | [optional]
**shared_plugin_data** | Option<[**serde_json::Value**](.md)> |  | [optional]
**bound_variables** | Option<[**models::IsLayerTraitBoundVariables**](IsLayerTrait_boundVariables.md)> |  | [optional]
**explicit_variable_modes** | Option<**std::collections::HashMap<String, String>**> | A mapping of variable collection ID to mode ID representing the explicitly set modes for this node. | [optional]
**export_settings** | Option<[**Vec<models::ExportSetting>**](ExportSetting.md)> | An array of export settings representing images to export from the node. | [optional]
**children** | [**Vec<models::SubcanvasNode>**](SubcanvasNode.md) | An array of nodes that are direct children of this node | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


