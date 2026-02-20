Social Media API

A RESTful backend API for a social media platform built using Django and Django REST Framework.

This project implements core social media functionalities including user management, posts, follow system, and a personalized feed.

🚀 Features
✅ Custom User Model
✅ User Registration & Management
✅ Create, Read, Update, Delete Posts
✅ Follow / Unfollow Users
✅ Personalized Feed (Posts from Followed Users)
✅ Pagination on Feed
✅ Permission Control (Users can only edit/delete their own posts)
✅ Admin Panel Support

🏗 Project Structure
social_media_api/
│
├── social_media_api/ # Project configuration
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── core/ # Main application
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── manage.py
└── requirements.txt

🧠 Database Models::
1️⃣ CustomUser
Extends Django’s AbstractUser.

Additional fields:
bio
profile_picture

2️⃣ Post
Represents user posts.

Fields:
content
image
author (ForeignKey to User)
created_at
updated_at
Posts are ordered by newest first.

3️⃣ Follow
Represents follow relationships between users.
Fields:
follower
following

Constraints:
Users cannot follow themselves
Duplicate follow relationships are prevented

🔌 API Endpoints
Base URL:
http://127.0.0.1:8000/api/
👤 Users
GET /api/users/
POST /api/users/
GET /api/users/{id}/
PUT /api/users/{id}/
DELETE /api/users/{id}/
📝 Posts
GET /api/posts/
POST /api/posts/
GET /api/posts/{id}/
PUT /api/posts/{id}/
DELETE /api/posts/{id}/

Permissions:
Only authenticated users can create posts
Users can only update/delete their own posts

🔄 Follow System
GET /api/follows/
POST /api/follows/
DELETE /api/follows/{id}/
📰 Feed
GET /api/feed/

Returns:
Posts from users that the current user follows
Ordered by newest first

Paginated results

📄 Pagination
Feed endpoint uses page number pagination.

Example:

/api/feed/?page=2
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone <your-repo-link>
cd social_media_api
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run Server
python manage.py runserver
Server will run at:
http://127.0.0.1:8000/
🔐 Authentication

Currently uses Django’s built-in authentication system.
Future improvements:
JWT Authentication
Token-based authentication

🛠 Technologies Used
Python
Django
Django REST Framework
SQLite (development database)

📈 Future Improvements
🔐 JWT Authentication
❤️ Likes system
💬 Comments system
🔎 Search functionality
🚀 Deployment (PythonAnywhere / Heroku)
🌐 Frontend integration (React or simple templates)

🎯 Learning Outcomes
Through this project, I gained hands-on experience in:
Django project architecture
Custom user model configuration
Model relationships (ForeignKey, constraints)

RESTful API design
Permissions & authentication
Pagination
Debugging migrations and routing errors

👨‍💻 Author::
Developed as part of a Backend Capstone Project.
