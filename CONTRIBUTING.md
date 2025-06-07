## Prerequisites

- `brew install openapi-generator`

**/v1/file only**

```bash
openapi-generator generate \
  -i openapi/openapi.document.yaml \
  -g rust \
  -o generated-client
```
