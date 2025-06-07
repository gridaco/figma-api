# \ComponentSetsApi

All URIs are relative to *https://api.figma.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_component_set**](ComponentSetsApi.md#get_component_set) | **GET** /v1/component_sets/{key} | Get component set
[**get_file_component_sets**](ComponentSetsApi.md#get_file_component_sets) | **GET** /v1/files/{file_key}/component_sets | Get file component sets



## get_component_set

> models::InlineObject9 get_component_set(key)
Get component set

Get metadata on a published component set by key.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**key** | **String** | The unique identifier of the component set. | [required] |

### Return type

[**models::InlineObject9**](inline_object_9.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## get_file_component_sets

> models::InlineObject8 get_file_component_sets(file_key)
Get file component sets

Get a list of published component sets within a file library.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**file_key** | **String** | File to list component sets from. This must be a main file key, not a branch key, as it is not possible to publish from branches. | [required] |

### Return type

[**models::InlineObject8**](inline_object_8.md)

### Authorization

[OAuth2](../README.md#OAuth2), [PersonalAccessToken](../README.md#PersonalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

