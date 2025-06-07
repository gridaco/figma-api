# TypeStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**font_family** | Option<**String**> | Font family of text (standard name). | [optional]
**font_post_script_name** | Option<**String**> | PostScript font name. | [optional]
**font_style** | Option<**String**> | Describes visual weight or emphasis, such as Bold or Italic. | [optional]
**italic** | Option<**bool**> | Whether or not text is italicized. | [optional][default to false]
**font_weight** | Option<**f64**> | Numeric font weight. | [optional]
**font_size** | Option<**f64**> | Font size in px. | [optional]
**text_case** | Option<**String**> | Text casing applied to the node, default is the original casing. | [optional]
**text_align_horizontal** | Option<**String**> | Horizontal text alignment as string enum. | [optional]
**text_align_vertical** | Option<**String**> | Vertical text alignment as string enum. | [optional]
**letter_spacing** | Option<**f64**> | Space between characters in px. | [optional]
**fills** | Option<[**Vec<models::Paint>**](Paint.md)> | An array of fill paints applied to the characters. | [optional]
**hyperlink** | Option<[**models::Hyperlink**](Hyperlink.md)> | Link to a URL or frame. | [optional]
**opentype_flags** | Option<**std::collections::HashMap<String, f64>**> | A map of OpenType feature flags to 1 or 0, 1 if it is enabled and 0 if it is disabled. Note that some flags aren't reflected here. For example, SMCP (small caps) is still represented by the `textCase` field. | [optional]
**semantic_weight** | Option<**String**> | Indicates how the font weight was overridden when there is a text style override. | [optional]
**semantic_italic** | Option<**String**> | Indicates how the font style was overridden when there is a text style override. | [optional]
**paragraph_spacing** | Option<**f64**> | Space between paragraphs in px, 0 if not present. | [optional][default to 0]
**paragraph_indent** | Option<**f64**> | Paragraph indentation in px, 0 if not present. | [optional][default to 0]
**list_spacing** | Option<**f64**> | Space between list items in px, 0 if not present. | [optional][default to 0]
**text_decoration** | Option<**String**> | Text decoration applied to the node, default is none. | [optional][default to None]
**text_auto_resize** | Option<**String**> | Dimensions along which text will auto resize, default is that the text does not auto-resize. TRUNCATE means that the text will be shortened and trailing text will be replaced with \"…\" if the text contents is larger than the bounds. `TRUNCATE` as a return value is deprecated and will be removed in a future version. Read from `textTruncation` instead. | [optional][default to None]
**text_truncation** | Option<**String**> | Whether this text node will truncate with an ellipsis when the text contents is larger than the text node. | [optional][default to Disabled]
**max_lines** | Option<**f64**> | When `textTruncation: \"ENDING\"` is set, `maxLines` determines how many lines a text node can grow to before it truncates. | [optional]
**line_height_px** | Option<**f64**> | Line height in px. | [optional]
**line_height_percent** | Option<**f64**> | Line height as a percentage of normal line height. This is deprecated; in a future version of the API only lineHeightPx and lineHeightPercentFontSize will be returned. | [optional][default to 100]
**line_height_percent_font_size** | Option<**f64**> | Line height as a percentage of the font size. Only returned when `lineHeightPercent` (deprecated) is not 100. | [optional]
**line_height_unit** | Option<**String**> | The unit of the line height value specified by the user. | [optional]
**is_override_over_text_style** | Option<**bool**> | Whether or not this style has overrides over a text style. The possible fields to override are semanticWeight, semanticItalic, hyperlink, and textDecoration. If this is true, then those fields are overrides if present. | [optional]
**bound_variables** | Option<[**models::TypeStyleAllOfBoundVariables**](TypeStyle_allOf_boundVariables.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


