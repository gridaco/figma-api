## Prerequisites

- `brew install openapi-generator`

**/v1/file only**

```bash
openapi-generator-cli generate \
  -i openapi/openapi.file.yaml \
  -c openapi/config.json \
  -g rust \
  -t ./templates \
  -o generated-client
```
