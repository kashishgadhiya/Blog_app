
# Blog App

This is a Django-based blog application that allows users to create, read, update, and delete blog posts. The application features user authentication and a responsive design using Bootstrap.

## Features

- **User Registration and Authentication**: Allows users to register, log in, and manage their accounts.
- **CRUD Operations for Blog Posts**: Users can create, read, update, and delete their blog posts.
- **Responsive Design**: Built using Bootstrap for a mobile-friendly and responsive layout.
- **Image Upload**: Users can upload images with their blog posts.

## Project Structure

The project consists of the following main components:

mylearning/            # The main Django project directory
myapp/                 # The Django app containing the blog functionality
templates/             # Directory for HTML templates
static/                # Directory for static files (CSS, JavaScript, images)
media/                 # Directory for user-uploaded files
```

## Setup

Follow these steps to set up the application on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/kashishgadhiya/Blog_app
```

### 2. Create a virtual environment and activate it

- Create the virtual environment:

```bash
python -m venv venv
```

- Activate the virtual environment:

  - On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

  - On Windows:

  ```bash
  venv\Scripts\activate
  ```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Apply the database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password.

### 6. Run the development server

```bash
python manage.py runserver
```

The application will be accessible at:

```
http://127.0.0.1:8000/
```

## Usage

- **Home Page**: Visit the home page to see a list of blog posts.
- **User Authentication**: Register a new account or log in to an existing one.
- **Create/Manage Blog Posts**: After logging in, you can create new blog posts, edit existing posts, or delete them.
- **Admin Interface**: You can also manage users and blog posts via the admin interface at `/admin/`.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

