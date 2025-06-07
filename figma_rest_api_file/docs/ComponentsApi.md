# \ComponentsApi

All URIs are relative to *https://api.figma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_component**](ComponentsApi.md#get_component) | **GET** /v1/components/{key} | Get component
[**get_file_components**](ComponentsApi.md#get_file_components) | **GET** /v1/files/{file_key}/components | Get file components



## get_component

> models::InlineObject7 get_component(key)
Get component

Get metadata on a component by key.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | The unique identifier of the component. | [required] |

### Return type

[**models::InlineObject7**](inline_object_7.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_file_components

> models::InlineObject6 get_file_components(file_key)
Get file components

Get a list of published components within a file library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to list components from. This must be a main file key, not a branch key, as it is not possible to publish from branches. | [required] |

### Return type

[**models::InlineObject6**](inline_object_6.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

