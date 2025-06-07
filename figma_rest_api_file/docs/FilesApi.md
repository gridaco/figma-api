# \FilesApi

All URIs are relative to *https://api.figma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file**](FilesApi.md#get_file) | **GET** /v1/files/{file_key} | Get file JSON
[**get_file_meta**](FilesApi.md#get_file_meta) | **GET** /v1/files/{file_key}/meta | Get file metadata
[**get_file_nodes**](FilesApi.md#get_file_nodes) | **GET** /v1/files/{file_key}/nodes | Get file JSON for specific nodes
[**get_image_fills**](FilesApi.md#get_image_fills) | **GET** /v1/files/{file_key}/images | Get image fills
[**get_images**](FilesApi.md#get_images) | **GET** /v1/images/{file_key} | Render images of file nodes



## get_file

> models::InlineObject get_file(file_key, version, ids, depth, geometry, plugin_data, branch_data)
Get file JSON

Returns the document identified by `file_key` as a JSON object. The file key can be parsed from any Figma file url: `https://www.figma.com/file/{file_key}/{title}`.  The `document` property contains a node of type `DOCUMENT`.  The `components` property contains a mapping from node IDs to component metadata. This is to help you determine which components each instance comes from.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to export JSON from. This can be a file key or branch key. Use `GET /v1/files/:key` with the `branch_data` query param to get the branch key. | [required] |
**version** | Option<**String**> | A specific version ID to get. Omitting this will get the current version of the file. |  |
**ids** | Option<**String**> | Comma separated list of nodes that you care about in the document. If specified, only a subset of the document will be returned corresponding to the nodes listed, their children, and everything between the root node and the listed nodes.  Note: There may be other nodes included in the returned JSON that are outside the ancestor chains of the desired nodes. The response may also include dependencies of anything in the nodes' subtrees. For example, if a node subtree contains an instance of a local component that lives elsewhere in that file, that component and its ancestor chain will also be included.  For historical reasons, top-level canvas nodes are always returned, regardless of whether they are listed in the `ids` parameter. This quirk may be removed in a future version of the API. |  |
**depth** | Option<**f64**> | Positive integer representing how deep into the document tree to traverse. For example, setting this to 1 returns only Pages, setting it to 2 returns Pages and all top level objects on each page. Not setting this parameter returns all nodes. |  |
**geometry** | Option<**String**> | Set to \"paths\" to export vector data. |  |
**plugin_data** | Option<**String**> | A comma separated list of plugin IDs and/or the string \"shared\". Any data present in the document written by those plugins will be included in the result in the `pluginData` and `sharedPluginData` properties. |  |
**branch_data** | Option<**bool**> | Returns branch metadata for the requested file. If the file is a branch, the main file's key will be included in the returned response. If the file has branches, their metadata will be included in the returned response. Default: false. |  |[default to false]

### Return type

[**models::InlineObject**](inline_object.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_file_meta

> models::InlineObject4 get_file_meta(file_key)
Get file metadata

Get file metadata

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to get metadata for. This can be a file key or branch key. Use `GET /v1/files/:key` with the `branch_data` query param to get the branch key. | [required] |

### Return type

[**models::InlineObject4**](inline_object_4.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_file_nodes

> models::InlineObject1 get_file_nodes(file_key, ids, version, depth, geometry, plugin_data)
Get file JSON for specific nodes

Returns the nodes referenced to by `ids` as a JSON object. The nodes are retrieved from the Figma file referenced to by `file_key`.  The node ID and file key can be parsed from any Figma node url: `https://www.figma.com/file/{file_key}/{title}?node-id={id}`  The `name`, `lastModified`, `thumbnailUrl`, `editorType`, and `version` attributes are all metadata of the specified file.  The `linkAccess` field describes the file link share permission level. There are 5 types of permissions a shared link can have: `\"inherit\"`, `\"view\"`, `\"edit\"`, `\"org_view\"`, and `\"org_edit\"`. `\"inherit\"` is the default permission applied to files created in a team project, and will inherit the project's permissions. `\"org_view\"` and `\"org_edit\"` restrict the link to org users.  The `document` attribute contains a Node of type `DOCUMENT`.  The `components` key contains a mapping from node IDs to component metadata. This is to help you determine which components each instance comes from.  By default, no vector data is returned. To return vector data, pass the geometry=paths parameter to the endpoint. Each node can also inherit properties from applicable styles. The styles key contains a mapping from style IDs to style metadata.  Important: the nodes map may contain values that are `null`. This may be due to the node id not existing within the specified file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to export JSON from. This can be a file key or branch key. Use `GET /v1/files/:key` with the `branch_data` query param to get the branch key. | [required] |
**ids** | **String** | A comma separated list of node IDs to retrieve and convert. | [required] |
**version** | Option<**String**> | A specific version ID to get. Omitting this will get the current version of the file. |  |
**depth** | Option<**f64**> | Positive integer representing how deep into the node tree to traverse. For example, setting this to 1 will return only the children directly underneath the desired nodes. Not setting this parameter returns all nodes.  Note: this parameter behaves differently from the same parameter in the `GET /v1/files/:key` endpoint. In this endpoint, the depth will be counted starting from the desired node rather than the document root node. |  |
**geometry** | Option<**String**> | Set to \"paths\" to export vector data. |  |
**plugin_data** | Option<**String**> | A comma separated list of plugin IDs and/or the string \"shared\". Any data present in the document written by those plugins will be included in the result in the `pluginData` and `sharedPluginData` properties. |  |

### Return type

[**models::InlineObject1**](inline_object_1.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_image_fills

> models::InlineObject3 get_image_fills(file_key)
Get image fills

Returns download links for all images present in image fills in a document. Image fills are how Figma represents any user supplied images. When you drag an image into Figma, we create a rectangle with a single fill that represents the image, and the user is able to transform the rectangle (and properties on the fill) as they wish.  This endpoint returns a mapping from image references to the URLs at which the images may be download. Image URLs will expire after no more than 14 days. Image references are located in the output of the GET files endpoint under the `imageRef` attribute in a `Paint`.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to get image URLs from. This can be a file key or branch key. Use `GET /v1/files/:key` with the `branch_data` query param to get the branch key. | [required] |

### Return type

[**models::InlineObject3**](inline_object_3.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_images

> models::InlineObject2 get_images(file_key, ids, version, scale, format, svg_outline_text, svg_include_id, svg_include_node_id, svg_simplify_stroke, contents_only, use_absolute_bounds)
Render images of file nodes

Renders images from a file.  If no error occurs, `\"images\"` will be populated with a map from node IDs to URLs of the rendered images, and `\"status\"` will be omitted. The image assets will expire after 30 days. Images up to 32 megapixels can be exported. Any images that are larger will be scaled down.  Important: the image map may contain values that are `null`. This indicates that rendering of that specific node has failed. This may be due to the node id not existing, or other reasons such has the node having no renderable components. It is guaranteed that any node that was requested for rendering will be represented in this map whether or not the render succeeded.  To render multiple images from the same file, use the `ids` query parameter to specify multiple node ids.  ``` GET /v1/images/:key?ids=1:2,1:3,1:4 ``` 

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to export images from. This can be a file key or branch key. Use `GET /v1/files/:key` with the `branch_data` query param to get the branch key. | [required] |
**ids** | **String** | A comma separated list of node IDs to render. | [required] |
**version** | Option<**String**> | A specific version ID to get. Omitting this will get the current version of the file. |  |
**scale** | Option<**f64**> | A number between 0.01 and 4, the image scaling factor. |  |
**format** | Option<**String**> | A string enum for the image output format. |  |[default to png]
**svg_outline_text** | Option<**bool**> | Whether text elements are rendered as outlines (vector paths) or as `<text>` elements in SVGs.  Rendering text elements as outlines guarantees that the text looks exactly the same in the SVG as it does in the browser/inside Figma.  Exporting as `<text>` allows text to be selectable inside SVGs and generally makes the SVG easier to read. However, this relies on the browser's rendering engine which can vary between browsers and/or operating systems. As such, visual accuracy is not guaranteed as the result could look different than in Figma. |  |[default to true]
**svg_include_id** | Option<**bool**> | Whether to include id attributes for all SVG elements. Adds the layer name to the `id` attribute of an svg element. |  |[default to false]
**svg_include_node_id** | Option<**bool**> | Whether to include node id attributes for all SVG elements. Adds the node id to a `data-node-id` attribute of an svg element. |  |[default to false]
**svg_simplify_stroke** | Option<**bool**> | Whether to simplify inside/outside strokes and use stroke attribute if possible instead of `<mask>`. |  |[default to true]
**contents_only** | Option<**bool**> | Whether content that overlaps the node should be excluded from rendering. Passing false (i.e., rendering overlaps) may increase processing time, since more of the document must be included in rendering. |  |[default to true]
**use_absolute_bounds** | Option<**bool**> | Use the full dimensions of the node regardless of whether or not it is cropped or the space around it is empty. Use this to export text nodes without cropping. |  |[default to false]

### Return type

[**models::InlineObject2**](inline_object_2.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

