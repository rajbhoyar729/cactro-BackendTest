
# Cactro Backend Test - Customizable Caching API

This project implements a **production-grade caching API** using **FastAPI**, **MongoDB**, and **Beanie ODM**. The API allows storing, retrieving, and deleting key-value pairs with a predefined maximum cache size. It is designed to be scalable, modular, and easy to deploy.

---

## Features

- **POST `/cache`**: Store or update a key-value pair in the cache.
- **GET `/cache/{key}`**: Retrieve a value by its key.
- **DELETE `/cache/{key}`**: Delete a key-value pair from the cache.
- **Predefined Cache Size**: Configurable maximum cache size to prevent overloading.
- **Asynchronous Operations**: Built with FastAPI and Beanie for high performance.
- **Modular Architecture**: Follows SOLID and OOP principles for maintainability.
- **Interactive API Documentation**: Automatically generated Swagger UI and ReDoc.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.8+**
- **MongoDB** (local instance or MongoDB Atlas)
- **pip** (Python package manager)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/rajbhoyar729/cactro-BackendTest.git
   cd cactro-BackendTest
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   Create a `.env` file in the root directory and add the following:
   ```env
   MONGODB_URI=mongodb://localhost:27017/cache_db  # For local MongoDB
   MAX_CACHE_SIZE=10  # Set your desired cache size
   ```

   For **MongoDB Atlas**, use:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@cluster0.example.mongodb.net/cache_db?retryWrites=true&w=majority
   ```

---

## Running the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   - **Local Server**: http://127.0.0.1:8000


---

## API Endpoints

### 1. **Store or Update a Key-Value Pair**
- **Endpoint**: `POST /cache`
- **Request Body**:
  ```json
  {
    "key": "your_key",
    "value": "your_value"
  }
  ```
- **Response**:
  ```json
  {
    "key": "your_key",
    "value": "your_value"
  }
  ```

### 2. **Retrieve a Value by Key**
- **Endpoint**: `GET /cache/{key}`
- **Response**:
  ```json
  {
    "value": "your_value"
  }
  ```

### 3. **Delete a Key-Value Pair**
- **Endpoint**: `DELETE /cache/{key}`
- **Response**:
  ```json
  {
    "message": "Key deleted successfully"
  }
  ```

---

## Configuration

### Environment Variables
- **`MONGODB_URI`**: MongoDB connection string.
- **`MAX_CACHE_SIZE`**: Maximum number of items allowed in the cache (default: 10).

### Adjusting Cache Size
Modify the `MAX_CACHE_SIZE` value in the `.env` file:
```env
MAX_CACHE_SIZE=15
```




---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please reach out to [Raj Bhoyar](mailto:rajbhoyar729@gmail.com).

