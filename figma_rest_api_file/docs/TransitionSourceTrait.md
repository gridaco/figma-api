# TransitionSourceTrait

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transition_node_id** | Option<**String**> | Node ID of node to transition to in prototyping | [optional]
**transition_duration** | Option<**f64**> | The duration of the prototyping transition on this node (in milliseconds). This will override the default transition duration on the prototype, for this node. | [optional]
**transition_easing** | Option<[**models::EasingType**](EasingType.md)> | The easing curve used in the prototyping transition on this node. | [optional]
**interactions** | Option<[**Vec<models::Interaction>**](Interaction.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


