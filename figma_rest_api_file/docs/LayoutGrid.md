# LayoutGrid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **String** | Orientation of the grid as a string enum  - `COLUMNS`: Vertical grid - `ROWS`: Horizontal grid - `GRID`: Square grid | 
**section_size** | **f64** | Width of column grid or height of row grid or square grid spacing. | 
**visible** | **bool** | Is the grid currently visible? | 
**color** | [**models::Rgba**](RGBA.md) | Color of the grid | 
**alignment** | **String** | Positioning of grid as a string enum  - `MIN`: Grid starts at the left or top of the frame - `MAX`: Grid starts at the right or bottom of the frame - `STRETCH`: Grid is stretched to fit the frame - `CENTER`: Grid is center aligned | 
**gutter_size** | **f64** | Spacing in between columns and rows | 
**offset** | **f64** | Spacing before the first column or row | 
**count** | **f64** | Number of columns or rows | 
**bound_variables** | Option<[**models::LayoutGridBoundVariables**](LayoutGrid_boundVariables.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


