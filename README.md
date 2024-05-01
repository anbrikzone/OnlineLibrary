# Online Library

## Description

The **Online Library** is a web application built with the **Django REST Framework**. It provides a catalog of books where users can leave reviews and ratings. The application uses **Simple JWT tokens** for secure authentication.

## Features

- **User Authentication**: Secure user authentication using Simple JWT tokens.
- **Permissions**: The API has object permissions between creators of reviews and ordinary users
- **Book Catalog**: A comprehensive catalog of books available for users to browse.
- **Reviews and Ratings**: Users can leave reviews and ratings for the books they've read.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/onlinelibrary.git
    ```
2. Install the requirements:
    ```
    pip install -r requirements.txt
    ```
3. Run migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
4. Start the server:
    ```
    python manage.py runserver
    ```

## Usage

To use the API endpoints, you will need to authenticate using Simple JWT tokens. Once authenticated, you can use the various endpoints to browse books, leave a review, or rate a book.

## Contributing

Contributions are welcome! Please read the contributing guidelines before getting started.

## License

This project is licensed under the terms of the MIT license. See the LICENSE file for details.