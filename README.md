# Project Updates

## What Was Added
* **Add Project:** A dedicated page for adding new projects using a Django Form and a function-based create view.
* **Testimonies:** Visitors can leave a testimony using a Django Form. Testimonies are listed on their own page (class-based ListView), each has a detail page (function-based view), and the newest ones also appear on the home page.
* **Inquiries:** A contact form where visitors can send an inquiry (name, contact number, email, address, and message). It uses an HTML form and a function-based create view, and submissions are saved to the database.

## How to Access
* **Add Project:** Click **Catalog** in the main navigation, then press **+ Add Project** (or go to `/projects/add/`).
* **Testimonies:** Click **Testimonies** in the main navigation. You can also see the latest testimonies on the **Home** page, where **Leave a Testimony** and **See all testimonies** lead to the full pages.
* **Inquiries:** Click **Let's Connect** in the main navigation to open the contact form. Submitted inquiries can be viewed in the Django admin at `/admin/`.

## Running the Project
Run `python manage.py runserver` and open `http://127.0.0.1:8000/` in your browser.
