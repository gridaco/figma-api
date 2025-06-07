# openapi spec

> From https://github.com/figma/rest-api-spec/blob/main/openapi/

- openapi.yaml: original spec
- openapi.file.yaml: document (node types) only spec

**/v1/file only removed paths & models**

- /v1/analytics/\*
- /v1/payments/\*
- /v1/activity_logs/\*
- /v2/webhooks/\*
- /v2/teams/\*
- /v1/projects/\*
- /v1/me
- /v1/dev_resources
- /v1/files/{file_key}/variables/\*
- /v1/files/{file_key}/dev_resources/\*
- /v1/files/{file_key}/comments/\*
- /v1/files/{file_key}/versions/\*

Removed models:

- "_LibraryAnalytics_"
- "_DevResource_"
- "_Payment_"
- "_ActivityLog_"
- "_Webhook_"
- "_Comment_"
- "_Team_"
- "_Project_"
- "_DevStatus_"
- "Me"
