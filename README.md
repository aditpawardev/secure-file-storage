Secure File Storage (Django + JavaScript)

This project started as a way for me to understand how real backend systems handle authentication and file access, and it slowly grew into a full-stack secure file storage application.

It allows users to log in, upload files, see only their own files, download them, and delete them — all protected using JWT authentication.

Why I built this

As a B.Tech Computer Science student, I wanted to go beyond basic CRUD apps and understand:

How authentication actually works in APIs

How to protect user-specific resources

How frontend and backend communicate in real projects

What problems appear when working across multiple machines

This project helped me learn all of that hands-on.

What the app does

Users log in using JWT authentication

Authenticated users can:

Upload files

View a list of their uploaded files

Download files securely

Delete their own files

Users cannot access files uploaded by others

All operations are handled through a REST API

Tech stack
Backend

Python

Django

Django REST Framework

JWT authentication (SimpleJWT)

Frontend

HTML

CSS

Vanilla JavaScript (Fetch API)

Environment & Tools

Ubuntu Linux

Git & GitHub

curl for API testing

Project structure
secure-file-storage/
├── backend/
│   ├── core/
│   ├── storage/
│   ├── frontend/
│   │   └── index.html
│   └── manage.py

API overview
Authentication

POST /api/auth/login/
Returns access and refresh JWT tokens

File operations (JWT required)

POST /api/files/upload/ – Upload a file

GET /api/files/ – List user files

GET /api/files/<id>/download/ – Download a file

DELETE /api/files/<id>/ – Delete a file

Running the project
Backend
python manage.py runserver 0.0.0.0:8000

Frontend
cd frontend
python3 -m http.server 5500


Open in browser:

http://localhost:5500

What I learned from this project

Implementing JWT authentication correctly

Protecting APIs using permissions

Handling file uploads and downloads securely

Debugging frontend issues caused by JavaScript errors and CORS

Working with two machines (local + server) and syncing code

Using Git and GitHub in a real workflow

This project taught me much more than tutorials ever did.

Possible improvements

Add user registration

Improve UI/UX

Add file size limits and validation

Deploy using Nginx and Gunicorn

Replace frontend with React

About me

Adit Pawar
B.Tech Computer Science student
GitHub: https://github.com/aditpawardev

Final note

This is not a copied tutorial project.
It was built step by step while learning, debugging, and fixing real issues — and that’s what makes it valuable to me.
