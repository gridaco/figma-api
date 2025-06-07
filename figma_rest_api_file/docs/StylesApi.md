# \StylesApi

All URIs are relative to *https://api.figma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_styles**](StylesApi.md#get_file_styles) | **GET** /v1/files/{file_key}/styles | Get file styles
[**get_style**](StylesApi.md#get_style) | **GET** /v1/styles/{key} | Get style



## get_file_styles

> models::InlineObject11 get_file_styles(file_key)
Get file styles

Get a list of published styles within a file library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to list styles from. This must be a main file key, not a branch key, as it is not possible to publish from branches. | [required] |

### Return type

[**models::InlineObject11**](inline_object_11.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_style

> models::InlineObject12 get_style(key)
Get style

Get metadata on a style by key.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | The unique identifier of the style. | [required] |

### Return type

[**models::InlineObject12**](inline_object_12.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

