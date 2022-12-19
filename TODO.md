# ToDo

## 1. Storage Service

Refactor architecture to include a storage service shared between API and resizer in order to avoid sending base64 images through network.

![Arch-v2](docs/arch-v2.png?raw=true)

## 2. Size as Param

Include an extra param in the API and in the service to allow users to choose the resizing size.

## 3. Tests

Include unit tests, communication tests and system tests.

## 4. Logging

Configure proper logging for all services.

## 5. Centralize Queue Definitions

Centralize queue shared definitions in order to avoid the same variable to appear in multiple contexts. The current state make it really hard to mantain the queue service.

## 6. Refactor Resizer

The resizer code doesn't follow good practices. For maintainability, it would nice to improve the code.