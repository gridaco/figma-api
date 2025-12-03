## Architecture

- REST API
- Webhooks
- Cache images

## Storage - DB vs File (s3)

Since the file request response in a lerge json tree, it can simply be stored as a .json file and response the file content.

Thus, the metadata such as version and file mapping, last updated should be stored in a io database.

### Possible configurations

- DynamoDB & S3
- MongoDB Atlas & S3
- MongoDB

## Background Image Pre-fetching

Fetching images from figma api is a heavy task. It takes a long time and also should consider the rate limit.

In most cases, the root frame should be pre-fetched and cached.

To do this on the service layer, we can use a queue system such as SQS.
