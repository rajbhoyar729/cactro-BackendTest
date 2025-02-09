# cactro-BackendTest

## Customizable Caching API

This project implements a production-grade caching API using FastAPI, MongoDB, and Beanie as the ODM. The API supports storing, retrieving, and deleting key-value pairs with a predefined maximum size.

### Features

- **POST /cache:** Store or update a cache item.
- **GET /cache/{key}:** Retrieve a cache item by key.
- **DELETE /cache/{key}:** Delete a cache item by key.
- Modular architecture following SOLID and OOP best practices.
- Asynchronous operations using FastAPI and Motor/Beanie.

### Setup

#### Prerequisites

- Python 3.8+
- MongoDB instance running (or a MongoDB Atlas cluster)

#### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd project
