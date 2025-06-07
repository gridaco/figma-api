# HasFramePropertiesTrait

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clips_content** | **bool** | Whether or not this node clip content outside of its bounds | 
**background** | Option<[**Vec<models::Paint>**](Paint.md)> | Background of the node. This is deprecated, as backgrounds for frames are now in the `fills` field. | [optional]
**background_color** | Option<[**models::Rgba**](RGBA.md)> | Background color of the node. This is deprecated, as frames now support more than a solid color as a background. Please use the `fills` field instead. | [optional]
**layout_grids** | Option<[**Vec<models::LayoutGrid>**](LayoutGrid.md)> | An array of layout grids attached to this node (see layout grids section for more details). GROUP nodes do not have this attribute | [optional]
**overflow_direction** | Option<**String**> | Whether a node has primary axis scrolling, horizontal or vertical. | [optional][default to None]
**layout_mode** | Option<**String**> | Whether this layer uses auto-layout to position its children. | [optional][default to None]
**primary_axis_sizing_mode** | Option<**String**> | Whether the primary axis has a fixed length (determined by the user) or an automatic length (determined by the layout engine). This property is only applicable for auto-layout frames. | [optional][default to Auto]
**counter_axis_sizing_mode** | Option<**String**> | Whether the counter axis has a fixed length (determined by the user) or an automatic length (determined by the layout engine). This property is only applicable for auto-layout frames. | [optional][default to Auto]
**primary_axis_align_items** | Option<**String**> | Determines how the auto-layout frame's children should be aligned in the primary axis direction. This property is only applicable for auto-layout frames. | [optional][default to Min]
**counter_axis_align_items** | Option<**String**> | Determines how the auto-layout frame's children should be aligned in the counter axis direction. This property is only applicable for auto-layout frames. | [optional][default to Min]
**padding_left** | Option<**f64**> | The padding between the left border of the frame and its children. This property is only applicable for auto-layout frames. | [optional][default to 0]
**padding_right** | Option<**f64**> | The padding between the right border of the frame and its children. This property is only applicable for auto-layout frames. | [optional][default to 0]
**padding_top** | Option<**f64**> | The padding between the top border of the frame and its children. This property is only applicable for auto-layout frames. | [optional][default to 0]
**padding_bottom** | Option<**f64**> | The padding between the bottom border of the frame and its children. This property is only applicable for auto-layout frames. | [optional][default to 0]
**item_spacing** | Option<**f64**> | The distance between children of the frame. Can be negative. This property is only applicable for auto-layout frames. | [optional][default to 0]
**item_reverse_z_index** | Option<**bool**> | Determines the canvas stacking order of layers in this frame. When true, the first layer will be draw on top. This property is only applicable for auto-layout frames. | [optional][default to false]
**strokes_included_in_layout** | Option<**bool**> | Determines whether strokes are included in layout calculations. When true, auto-layout frames behave like css \"box-sizing: border-box\". This property is only applicable for auto-layout frames. | [optional][default to false]
**layout_wrap** | Option<**String**> | Whether this auto-layout frame has wrapping enabled. | [optional]
**counter_axis_spacing** | Option<**f64**> | The distance between wrapped tracks of an auto-layout frame. This property is only applicable for auto-layout frames with `layoutWrap: \"WRAP\"` | [optional]
**counter_axis_align_content** | Option<**String**> | Determines how the auto-layout frame’s wrapped tracks should be aligned in the counter axis direction. This property is only applicable for auto-layout frames with `layoutWrap: \"WRAP\"`. | [optional][default to Auto]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


