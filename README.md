# Django Blog Frontend Assignment

A Django blog application built to meet the assignment frontend requirements using Bootstrap and Django templates.

## Key Features
- Base layout with navbar, footer, and responsive content
- Home page showing cards with title, image, short content, and Read More button
- Login and signup pages with Bootstrap styling
- Create Post page with `multipart/form-data` image upload support
- Detail page displaying full blog content, image, author name, and date
- Conditional navbar: Login/Signup for guests, Create Post/Logout for logged-in users

## Setup
1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Notes
- Static files are loaded from `static/blog/css/styles.css`.
- Media uploads are saved in the `media/` folder.
- Use the admin interface to create superusers, if needed.
