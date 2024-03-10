
# Bloging 

## Overview

Django Blog Site is a web application built using the Django framework that allows users to create, publish, and manage blog posts. It provides a user-friendly interface for both administrators and visitors to interact with the blog content.

## Features

- Admin Dashboard: Provide an admin interface for managing blog posts, categories, tags, and users.
- Create and Publish Posts: Enable users to create, edit, and publish blog posts with rich text formatting.
- Search Functionality: Implement a search feature to allow users to search for specific blog posts.
- Responsive Design: Ensure the website is mobile-friendly and accessible on various devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/1-Sanchit-1/Blogs
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py makemigrates
   python manage.py migrate
   ```

4. Create a superuser (admin account):

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the blog site at [http://localhost:8000/](http://localhost:8000/).

## Usage

1. Create blog posts, categories, and tags using the admin interface.
2. Visit the home page to view and interact with the blog posts.
3. Use the search functionality to find specific blog posts.

## Contributing

Contributions are welcome! If you'd like to contribute to the Django Blog Site, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new pull request.


## Contact

For questions or inquiries, please contact [lcb2021031@iiil.ac.in](mailto:lcb2021031@iiil.ac.in).

