Personal Portfolio (Django)

A personal portfolio website built with Django. Visitors can browse projects, read and leave testimonies, and send inquiries. The owner signs in to a private dashboard to manage projects and tech stacks, and anything added there shows up on the public portfolio.

Features

Public site

Home, About, Skillset, and Let's Connect (contact) pages
Project catalog and project detail pages, with the tech stacks used
Testimonies: a list page (class-based view), a detail page, and a form to leave one
Contact form that saves inquiries to the database (viewable in the Django admin)
The newest testimonies are also shown on the home page

**Owner dashboard (superuser only)**

Sign-in page that only accepts superuser accounts
Table of all projects (name, description cut to 50 characters, tech stacks, link)
Table of all tech stacks (name, projects it was used in, date added)
Create a project (name, description, tech stack as radio buttons, link): every field is required
Create a tech stack: the name is required and duplicates are rejected, even with different capitalization
Sign out button
Requirements
Python (a version supported by Django 6.1)
Git
Packages listed in requirements.txt (Django and python-dotenv)
Setup (fresh clone)

The repository does not include a database or a virtual environment, so you create both yourself. The migration files are included, so run migrate only. Do not run makemigrations.

1. Clone the repository

git clone <your-repo-url>
cd <repo-folder>

2. Create and activate a virtual environment

Windows (PowerShell):

py -m venv .venv
.\.venv\Scripts\Activate.ps1

If PowerShell blocks the script, run Set-ExecutionPolicy -Scope CurrentUser RemoteSigned once and try again.

macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install the packages

python -m pip install -r requirements.txt

4. Create your .env file

Copy the example file:

Windows (PowerShell): Copy-Item .env.example .env

macOS / Linux: cp .env.example .env

Generate a secret key and paste it into .env as the value of SECRET_KEY (see the next section):

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

5. Create the database

python manage.py migrate

6. Create the owner (superuser) account

python manage.py createsuperuser

7. Run the server

python manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

**Owner sign-in**

There is intentionally no sign-in button in the front end. To sign in, go to the address directly:

/dashboard/login/
Only superuser accounts can sign in. A regular account is rejected even if the username and password are correct.
After a successful sign-in you are redirected to /dashboard/.
Visiting any dashboard page while signed out redirects you to the sign-in page.
To try the restriction, create a regular user in /admin/ (leave "Staff status" and "Superuser status" unchecked) and attempt to sign in with it.
First-time content

A fresh database is empty. To fill in the site:

Sign in at /dashboard/login/.
In /admin/, add one Personal Info record. The Catalog page uses it for the name, summary, and contact details.
In the dashboard, add your tech stacks first (Tech Stacks → + Add Tech Stack), then your projects (Projects → + Add Project).
New projects appear on the public Catalog and on their own detail pages right away.
