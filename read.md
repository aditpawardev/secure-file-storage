Secure File Storage (Django + JavaScript)

This project is a secure file storage system built using Django REST Framework for the backend and Vanilla JavaScript for the frontend.

The main goal of this project was to understand how authentication, authorization, and file handling work in real-world backend systems, rather than just building a basic CRUD app.

Motivation

As a B.Tech Computer Science student, I wanted to build something that goes beyond tutorials and exposes real engineering problems.

I was especially interested in learning how APIs handle user authentication, how access to resources is restricted, and how frontend applications securely interact with backend services.

This project helped me explore all of these concepts in a practical way.

What this application does

The application allows users to log in using JWT-based authentication.

Once authenticated, a user can upload files to the server, view a list of only their own uploaded files, download those files securely, and delete them when needed.

All file operations are protected so that a user cannot access or modify another user’s files.

Key features

JWT-based authentication

Secure file upload

User-specific file listing

Secure file download

File deletion with owner-only access

RESTful API design

Simple frontend for interacting with the API

Technology stack
Backend

The backend is built using Python and Django, with Django REST Framework used to expose APIs.
JWT authentication is implemented using SimpleJWT.

Frontend

The frontend is a lightweight interface built using HTML, CSS, and Vanilla JavaScript.
It communicates with the backend using the Fetch API.

Tools and environment

The project was developed and tested on Ubuntu Linux.
Git and GitHub were used for version control, and curl was used for testing API endpoints.

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
Used to obtain JWT access and refresh tokens.

File operations (authentication required)

POST /api/files/upload/ – Upload a file

GET /api/files/ – List files uploaded by the logged-in user

GET /api/files/<id>/download/ – Download a specific file

DELETE /api/files/<id>/ – Delete a specific file

Running the project locally
Backend
python manage.py runserver 0.0.0.0:8000

Frontend
cd frontend
python3 -m http.server 5500


The frontend can then be accessed at:

http://localhost:5500

What I learned from this project

This project helped me understand how JWT authentication works in practice.

I learned how to secure APIs using permissions and how to protect user-specific resources.

I also gained experience debugging real-world issues such as CORS errors, frontend JavaScript crashes, and syncing code across multiple machines.

Overall, this project taught me much more than following step-by-step tutorials.

Possible future improvements

Add user registration

Improve frontend UI/UX

Add file validation and size limits

Deploy the application using Gunicorn and Nginx

Replace the frontend with a React-based UI

About me

Adit Pawar
B.Tech Computer Science student
GitHub: https://github.com/aditpawardev

Final note

This project was built incrementally while learning and debugging real problems.

It represents my understanding of backend development, authentication, and frontend-backend integration at this stage of my learning journey.
