# BaseTypeStyle

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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


