# SectionNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A string uniquely identifying this node within the document. | 
**name** | **String** | The name given to the node by the user in the tool. | 
**r#type** | **String** | The type of this node, represented by the string literal \"SECTION\" | 
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
**fills** | [**Vec<models::Paint>**](Paint.md) | An array of fill paints applied to the node. | 
**styles** | Option<**std::collections::HashMap<String, String>**> | A mapping of a StyleType to style ID (see Style) of styles present on this node. The style ID can be used to look up more information about the style in the top-level styles field. | [optional]
**strokes** | Option<[**Vec<models::Paint>**](Paint.md)> | An array of stroke paints applied to the node. | [optional]
**stroke_weight** | Option<**f64**> | The weight of strokes on the node. | [optional][default to 1]
**stroke_align** | Option<**String**> | Position of stroke relative to vector outline, as a string enum  - `INSIDE`: stroke drawn inside the shape boundary - `OUTSIDE`: stroke drawn outside the shape boundary - `CENTER`: stroke drawn centered along the shape boundary | [optional]
**stroke_join** | Option<**String**> | A string enum with value of \"MITER\", \"BEVEL\", or \"ROUND\", describing how corners in vector paths are rendered. | [optional][default to Miter]
**stroke_dashes** | Option<**Vec<f64>**> | An array of floating point numbers describing the pattern of dash length and gap lengths that the vector stroke will use when drawn.  For example a value of [1, 2] indicates that the stroke will be drawn with a dash of length 1 followed by a gap of length 2, repeated. | [optional]
**fill_override_table** | Option<[**std::collections::HashMap<String, models::HasGeometryTraitAllOfFillOverrideTable>**](HasGeometryTrait_allOf_fillOverrideTable.md)> | Map from ID to PaintOverride for looking up fill overrides. To see which regions are overriden, you must use the `geometry=paths` option. Each path returned may have an `overrideID` which maps to this table. | [optional]
**fill_geometry** | Option<[**Vec<models::Path>**](Path.md)> | Only specified if parameter `geometry=paths` is used. An array of paths representing the object fill. | [optional]
**stroke_geometry** | Option<[**Vec<models::Path>**](Path.md)> | Only specified if parameter `geometry=paths` is used. An array of paths representing the object stroke. | [optional]
**stroke_cap** | Option<**String**> | A string enum describing the end caps of vector paths. | [optional][default to None]
**stroke_miter_angle** | Option<**f64**> | Only valid if `strokeJoin` is \"MITER\". The corner angle, in degrees, below which `strokeJoin` will be set to \"BEVEL\" to avoid super sharp corners. By default this is 28.96 degrees. | [optional][default to 28.96]
**children** | [**Vec<models::SubcanvasNode>**](SubcanvasNode.md) | An array of nodes that are direct children of this node | 
**absolute_bounding_box** | [**models::Rectangle**](Rectangle.md) |  | 
**absolute_render_bounds** | [**models::Rectangle**](Rectangle.md) |  | 
**preserve_ratio** | Option<**bool**> | Keep height and width constrained to same ratio. | [optional][default to false]
**constraints** | Option<[**models::LayoutConstraint**](LayoutConstraint.md)> | Horizontal and vertical layout constraints for node. | [optional]
**relative_transform** | Option<[**Vec<Vec<f64>>**](Vec.md)> | A transformation matrix is standard way in computer graphics to represent translation and rotation. These are the top two rows of a 3x3 matrix. The bottom row of the matrix is assumed to be [0, 0, 1]. This is known as an affine transform and is enough to represent translation, rotation, and skew.  The identity transform is [[1, 0, 0], [0, 1, 0]].  A translation matrix will typically look like:  ``` [[1, 0, tx],   [0, 1, ty]] ```  and a rotation matrix will typically look like:  ``` [[cos(angle), sin(angle), 0],   [-sin(angle), cos(angle), 0]] ```  Another way to think about this transform is as three vectors:  - The x axis (t[0][0], t[1][0]) - The y axis (t[0][1], t[1][1]) - The translation offset (t[0][2], t[1][2])  The most common usage of the Transform matrix is the `relativeTransform property`. This particular usage of the matrix has a few additional restrictions. The translation offset can take on any value but we do enforce that the axis vectors are unit vectors (i.e. have length 1). The axes are not required to be at 90° angles to each other. | [optional]
**size** | Option<[**models::Vector**](Vector.md)> | Width and height of element. This is different from the width and height of the bounding box in that the absolute bounding box represents the element after scaling and rotation. Only present if `geometry=paths` is passed. | [optional]
**layout_align** | Option<**String**> |  Determines if the layer should stretch along the parent's counter axis. This property is only provided for direct children of auto-layout frames.  - `INHERIT` - `STRETCH`  In previous versions of auto layout, determined how the layer is aligned inside an auto-layout frame. This property is only provided for direct children of auto-layout frames.  - `MIN` - `CENTER` - `MAX` - `STRETCH`  In horizontal auto-layout frames, \"MIN\" and \"MAX\" correspond to \"TOP\" and \"BOTTOM\". In vertical auto-layout frames, \"MIN\" and \"MAX\" correspond to \"LEFT\" and \"RIGHT\". | [optional]
**layout_grow** | Option<**f64**> | This property is applicable only for direct children of auto-layout frames, ignored otherwise. Determines whether a layer should stretch along the parent's primary axis. A `0` corresponds to a fixed size and `1` corresponds to stretch. | [optional][default to Variant0]
**layout_positioning** | Option<**String**> | Determines whether a layer's size and position should be determined by auto-layout settings or manually adjustable. | [optional][default to Auto]
**min_width** | Option<**f64**> | The minimum width of the frame. This property is only applicable for auto-layout frames or direct children of auto-layout frames. | [optional][default to 0]
**max_width** | Option<**f64**> | The maximum width of the frame. This property is only applicable for auto-layout frames or direct children of auto-layout frames. | [optional][default to 0]
**min_height** | Option<**f64**> | The minimum height of the frame. This property is only applicable for auto-layout frames or direct children of auto-layout frames. | [optional][default to 0]
**max_height** | Option<**f64**> | The maximum height of the frame. This property is only applicable for auto-layout frames or direct children of auto-layout frames. | [optional][default to 0]
**layout_sizing_horizontal** | Option<**String**> | The horizontal sizing setting on this auto-layout frame or frame child. - `FIXED` - `HUG`: only valid on auto-layout frames and text nodes - `FILL`: only valid on auto-layout frame children | [optional]
**layout_sizing_vertical** | Option<**String**> | The vertical sizing setting on this auto-layout frame or frame child. - `FIXED` - `HUG`: only valid on auto-layout frames and text nodes - `FILL`: only valid on auto-layout frame children | [optional]
**section_contents_hidden** | **bool** | Whether the contents of the section are visible | [default to false]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


