# Hubbii Project

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [Directory Structure](#directory-structure)
6. [Contributing](#contributing)
7. [License](#license)
8. [Authors](#authors)

---

## Introduction
Hubbii is an innovative project portfolio platform designed to empower professionals and students by allowing them to showcase their projects, certifications, and current ideas. The platform focuses on seamless navigation, real-time collaboration, and secure management of user data. Hubbii serves as a comprehensive solution for creating and sharing professional portfolios with ease.

---

## Features
- **User Authentication:** Secure login and registration with email verification.
- **Portfolio Management:** CRUD operations for managing user portfolios.
- **File Uploads:** Support for project images, videos, and documents.
- **Responsive Dashboard:** User-friendly and interactive dashboard for managing projects and tracking progress.
- **Real-Time Notifications:** Alerts for portfolio updates and interactions.
- **Third-Party Integrations:** Email services for OTP verification and file storage.
- **Search and Filters:** Advanced search options to find projects based on categories and tags.

---

## Technologies Used
### Backend
- Django (Python)
- Django REST Framework (DRF)
- PostgreSQL

### Frontend
- HTML5, CSS3, JavaScript (ES6)
- ReactJS

### Others
- AWS S3 for file storage
- Redis and Celery for asynchronous tasks
- Docker for containerization

---

## Setup Instructions
### Prerequisites
- Python 3.9+
- Node.js and npm
- PostgreSQL
- Redis
- Docker (optional)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hubbii.git
   cd hubbii
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables in `.env`:
   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgresql://user:password@localhost:5432/hubbii_db
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

---

## Directory Structure
```
hubbii/
├── backend/
│   ├── hubbii/
│   ├── users/
│   ├── projects/
│   └── templates/
├── frontend/
│   ├── public/
│   └── src/
├── .env
├── requirements.txt
└── README.md
```

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Authors
### Team Hubbii
1. **Miracle Amajama**: Backend Developer  
   Role: Focuses on designing and implementing the database architecture, managing user authentication and authorization systems, and integrating third-party services for file uploads and email verification.

2. **Yunusa Abdullahi**: Frontend Developer  
   Role: Designs and develops user-friendly interfaces for the landing page and login/register pages, ensuring seamless UI/UX experiences and responsiveness.

3. **Kingsley Okoronkwo**: Backend Developer  
   Role: Specializes in building scalable APIs, ensuring the platform's performance and security, and developing key features such as CRUD operations and real-time notifications.

4. **Ajobiewe Joseph**: Frontend Developer  
   Role: Builds and optimizes the dashboard and project detail pages, implementing interactive features and ensuring smooth navigation throughout the platform.

