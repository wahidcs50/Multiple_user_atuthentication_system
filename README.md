# Multiple User Authentication System with Django and Djoser

This project demonstrates how to implement multiple user authentication in a Django application using Djoser.

## Overview

Django is a powerful web framework for building web applications, and Djoser is a Django REST framework providing authentication and user management capabilities out of the box. By combining these tools, we can easily implement authentication systems with support for multiple user types.

This project showcases the following features:

- Authentication endpoints for user registration, login, logout, and password reset.
- Custom user models for different user types (e.g., customers, admins, managers).
- Role-based access control (RBAC) to restrict access to certain views or APIs based on user roles.
- Integration of Djoser with Django's built-in authentication system.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

- Register new users by accessing the registration endpoint (`/auth/users/`).
- Log in with registered users using the login endpoint (`/auth/token/login/`).
- Authenticate with the registered user using the login endpoint.
-  Access user profile information and update user details using appropriate endpoints.
-   Implement custom authentication logic, user types, or additional functionality as needed.
