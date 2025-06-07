# HasLayoutTrait

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_bounding_box** | Option<[**models::Rectangle**](Rectangle.md)> |  | 
**absolute_render_bounds** | Option<[**models::Rectangle**](Rectangle.md)> |  | 
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


