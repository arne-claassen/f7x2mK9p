# Protocol Registry

Simple API for registering and retrieving study protocols. This API is used as a component in a larger
system, which uses `Protocol` to reference access the registration . Protocol names cannot be changed
once registered and serve as symbolic identifiers. They must be unique and follow the naming convention
of lower-case alphanumeric and underscores.

## Endpoints

| Methods   | Route             | Description                        |
|-----------|-------------------|------------------------------------|
| GET       | /protocol/        | Retrieve all protocols             |
| POST      | /protocol/        | Create new protocol                |
| GET       | /protocol/{name}/ | Retrieve specific protocol         |
