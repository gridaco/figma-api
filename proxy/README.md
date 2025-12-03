# WIP - Figma API (figma file proxy server & client)

Faster Figma proxy api with caching

## Capabilities

### Design Query

Query specific part of the design

### Caching & Prefetching

All responses are cached by default. + The service will listen to figma webhooks (if provided) and save the changes.
Response time will be much faster.

- general responses
- images (proxy-hosted, not expiring)
- changes (with webhooks)

### Enhanced Webhooks

Proxy webhooks with figma-file-proxy-server's features

### Cross Sync & Diff

Push changes with proxy, sync with plugin and track diffs in-between

### Reserved Urls

Fetching preview & for baking design to image, you can use reserved url right away.
For example,

`https://your-figma-proxy-host.com/images/XXXX@2x.png`

### Custom embeddings

You can make custom design embeddings with [figma-view](https://github.com/gridaco/figma-view), with your own branding.

## Changes

### `/files`

Extended response

```json
{
    ...
    "indexing": true,
    "has_updates": false,
    "indexing_progress": {
      "file": "indexing",
      "images": "indexed"
    }
}
```

## Other projects

- [fimga-archives](https://github.com/gridaco/figma-archives) Public figma community file archiver
- [figma-view](https://github.com/gridaco/figma-view) Embeddable React component renderes Figma node natively
