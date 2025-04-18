## Endpoints

### Customers

- **POST /users**: Create a new user
  - *Request Body*:
     ```json
    {
      "name": "FirstName",
      "last_name": "LastName",
      "middle_name": "MiddleName",
      "birth_year": 1990
    }
    ```
  - *Response*: JSON with the created user
    ```json
    {
      "id": 1,
      "name": "FirstName",
      "last_name": "LastName",
      "middle_name": "MiddleName",
      "birth_year": 1990,
      "is_author": false
    }
    ```

- **POST /users**: Create a new author
  - *Request Body*:
    ```json
    {
      "name": "AuthorFirstName",
      "last_name": "AuthorLastName",
      "middle_name": "AuthorMiddleName",
      "birth_year": 1990,
      "is_author": true
    }
    ```
  - *Response*: JSON with the created author
    ```json
    {
      "id": 2,
      "name": "AuthorFirstName",
      "last_name": "AuthorLastName",
      "middle_name": "AuthorMiddleName",
      "birth_year": 1990,
      "is_author": true
    }
    ```

- **PUT /users/{user_id}**: Update user data by ID
  - *Path Parameter*: `user_id` - ID of the user to update
  - *Request Body*: JSON with updated user data (optional fields)
    ```json
    {
      "name": "NewName",
      "last_name": "NewLastName",
      "middle_name": "NewMiddleName",
      "birth_year": 1995,
      "is_author": false
    }
    ```
  - *Response*: JSON with updated user data
    ```json
    {
      "id": 1,
      "name": "NewName",
      "last_name": "NewLastName",
      "middle_name": "NewMiddleName",
      "birth_year": 1995,
      "is_author": false
    }
    ```

- **GET /users/{user_id}**: Get a user by ID
  - *Path Parameter*: `user_id` - ID of the user
  - *Response*: JSON with user data
    ```json
    {
      "id": 1,
      "name": "NewName",
      "last_name": "NewLastName",
      "middle_name": "NewMiddleName",
      "birth_year": 1995,
      "is_author": false
    }
    ```

- **GET /users**: Get all users with pagination
  - *Query Parameters*:
    - `is_author` (optional, default=false): true to get only authors, false otherwise.
    - `skip` (optional, default=0): Number of records to skip.
    - `limit` (optional, default=50): Maximum number of records to return.
  - *Response*: JSON list of users or authors
    ```json
    [
      {
        "id": 1,
        "name": "NewName",
        "last_name": "NewLastName",
        "middle_name": "NewMiddleName",
        "birth_year": 1995,
        "is_author": false
      }
    ]
    ```

### Books

- **POST /books**: Create a new book
  - *Request Body*:
    ```json
    {
      "title": "It",
      "author_id": "1",
      "genre": "Horror",
      "year": 1985,
      "status": true
    }
    ```
  - *Response*: JSON with the created book
    ```json
    {
      "id": 1,
      "title": "It",
      "author_id": "1",
      "genre": "Horror",
      "year": 1985,
      "status": true
    }
    ```

- **PUT /books/{book_id}**: Update book data by ID
  - *Path Parameter*: `book_id` - ID of the book
  - *Request Body*: JSON with updated book data (optional fields)
    ```json
    {
      "title": "New Title",
      "author_id": "1",
      "genre": "New Genre",
      "year": 1986,
      "status": false
    }
    ```
  - *Response*: JSON with updated book data
    ```json
    {
      "id": 1,
      "title": "New Title",
      "author_id": "1",
      "genre": "New Genre",
      "year": 1986,
      "status": false
    }
    ```

- **GET /books/{book_id}**: Get a book by ID
  - *Path Parameter*: `book_id` - ID of the book
  - *Response*: JSON with book data
    ```json
    {
      "id": 1,
      "title": "New Title",
      "author_id": "1",
      "genre": "New Genre",
      "year": 1986,
      "status": false
    }
    ```

- **GET /books**: Get all books with pagination
  - *Query Parameters*:
    - `skip` (optional, default=0): Number of records to skip.
    - `limit` (optional, default=10): Maximum number of records to return.
  - *Response*: JSON list of books
    ```json
    [
      {
        "id": 1,
        "title": "New Title",
        "author_id": "1",
        "genre": "New Genre",
        "year": 1986,
        "status": false
      }
    ]
    ```

### Loans

- **POST /loans**: Create a new book loan
  - *Request Body*:
    ```json
    {
      "id": 1,
      "book_id": 1,
      "user_id": 1,
      "loan_date": "2024-06-01"
    }
    ```
  - *Response*: JSON with created loan
    ```json
    {
      "id": 1,
      "book_id": 1,
      "user_id": 1,
      "loan_date": "2024-06-01",
      "return_date": null
    }
    ```

- **PUT /loans/{book_id}**: Return a book by ID
  - *Path Parameter*: `book_id` - ID of the book
  - *Request Body*: JSON with the book ID and return date (optional field)
    ```json
    {
      "book_id": 1,
      "return_date": "2024-06-13"
    }
    ```
  - *Response*: JSON with updated loan data
    ```json
    {
      "id": 1,
      "book_id": 1,
      "user_id": 1,
      "loan_date": "2024-06-01",
      "return_date": "2024-06-13"
    }
    ```

- **GET /loans**: Get all loans with pagination
  - *Query Parameters*:
    - `skip` (optional, default=0): Number of records to skip.
    - `limit` (optional, default=50): Maximum number of records to return.
  - *Response*: JSON list of loans
    ```json
    [
      {
        "id": 1,
        "book_id": 1,
        "user_id": 1,
        "loan_date": "2024-06-01",
        "return_date": "2024-06-13"
      }
    ]
    ```