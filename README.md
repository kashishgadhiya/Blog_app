# Blog App

This is a Django-based blog application that allows users to create, read, update, and delete blog posts. It includes user authentication and a responsive design using Bootstrap.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Responsive design using Bootstrap
- Image upload for blog posts

## Project Structure

The project consists of the following main components:

- `mylearning/`: The main Django project directory
- `myapp/`: The Django app containing the blog functionality
- `templates/`: Directory for HTML templates
- `static/`: Directory for static files (CSS, JavaScript, images)
- `media/`: Directory for user-uploaded files

## Setup

1. Clone the repository:
git clone https://github.com/kashishgadhiya/Blog_app

2. Create a virtual environment and activate it:
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate


3. Install the required packages:
   pip install -r requirements.txt


4. Apply the database migrations:
   python manage.py migrate


5. Create a superuser:
   python manage.py createsuperuser


6. Run the development server:
   python manage.py runserver

7. Access the application at `http://127.0.0.1:8000/`

## Usage

- Visit the home page to see a list of blog posts
- Register a new account or log in to an existing one
- Create new blog posts, edit your existing posts, or delete them
- Use the admin interface (`/admin/`) to manage users and posts

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

