# ConnectorTextBackground

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corner_radius** | Option<**f64**> | Radius of each corner if a single radius is set for all corners | [optional][default to 0]
**corner_smoothing** | Option<**f64**> | A value that lets you control how \"smooth\" the corners are. Ranges from 0 to 1. 0 is the default and means that the corner is perfectly circular. A value of 0.6 means the corner matches the iOS 7 \"squircle\" icon shape. Other values produce various other curves. | [optional]
**rectangle_corner_radii** | Option<**Vec<f64>**> | Array of length 4 of the radius of each corner of the frame, starting in the top left and proceeding clockwise.  Values are given in the order top-left, top-right, bottom-right, bottom-left. | [optional]
**fills** | [**Vec<models::Paint>**](Paint.md) | An array of fill paints applied to the node. | 
**styles** | Option<**std::collections::HashMap<String, String>**> | A mapping of a StyleType to style ID (see Style) of styles present on this node. The style ID can be used to look up more information about the style in the top-level styles field. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


