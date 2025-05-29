# 📦 Requirements.txt Update Summary

## Overview
Updated the `requirements.txt` file to include all packages used in the Sadaqa Django crowd funding project, including the newly added Django REST Framework and other dependencies.

## ✅ Packages Included

### **Core Framework**
- **Django==5.2.1** - Main Django framework

### **API Development**
- **djangorestframework==3.15.2** - Django REST Framework for API endpoints
  - *Added during CRUD implementation*
  - Required for all API functionality

### **Authentication & Social Login**
- **django-allauth==0.61.1** - Comprehensive authentication system
  - Handles email/password authentication
  - Social media login support (Facebook, Google, etc.)

### **Field Extensions**
- **django-phonenumber-field==7.3.0** - Phone number field validation
- **phonenumbers==8.13.30** - Phone number parsing and formatting
- **django-countries==7.5.1** - Country field with dropdown support

### **Media & Images**
- **Pillow==10.2.0** - Image processing library
  - Required for ImageField in models
  - Handles profile pictures and project images

### **Database**
- **psycopg2-binary==2.9.9** - PostgreSQL database adapter
  - Binary distribution for easier installation
  - Required for PostgreSQL database connection

### **Configuration**
- **python-dotenv==1.0.1** - Environment variables management
  - Loads environment variables from .env files
  - Useful for configuration management

## 🚀 Optional Production Dependencies

The following packages are commented out but recommended for production:

### **Web Server**
- **gunicorn==21.2.0** - WSGI HTTP Server for production deployment

### **Static Files**
- **whitenoise==6.6.0** - Static file serving for production

### **API Enhancement**
- **django-cors-headers==4.3.1** - CORS handling for API requests

### **Background Tasks**
- **celery==5.3.4** - Task queue for background jobs
- **redis==5.0.1** - Cache and message broker for Celery

## 📋 Installation Instructions

### **Install All Dependencies**
```bash
pip install -r requirements.txt
```

### **Install with Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Upgrade Dependencies**
```bash
pip install --upgrade -r requirements.txt
```

## 🔧 Package Purposes in Project

### **Django (5.2.1)**
- Core framework for the web application
- Provides ORM, admin interface, authentication

### **Django REST Framework (3.15.2)**
- Powers all API endpoints (/api/*)
- Provides serializers, viewsets, permissions
- Enables CRUD operations for projects, categories, users

### **Django Allauth (0.61.1)**
- User registration and login system
- Social authentication (Facebook login)
- Email verification and password reset

### **Phone Number Field (7.3.0)**
- CustomUser model phone field validation
- International phone number support
- Used in user registration and profiles

### **Django Countries (7.5.1)**
- Country selection in user profiles
- Provides country dropdown with flags
- Used in CustomUser model

### **Pillow (10.2.0)**
- Profile picture uploads (CustomUser.pic)
- Project image uploads (ProjectPic model)
- Image resizing and processing

### **psycopg2-binary (2.9.9)**
- PostgreSQL database connection
- Required for production database
- Binary version for easier installation

### **python-dotenv (1.0.1)**
- Environment variable management
- Loads settings from .env files
- Keeps sensitive data secure

## 🎯 Version Compatibility

All package versions are tested and compatible with:
- **Python 3.8+**
- **Django 5.2.1**
- **PostgreSQL 12+**

## 🚀 Production Considerations

For production deployment, consider uncommenting and installing:

1. **gunicorn** - Production WSGI server
2. **whitenoise** - Static file serving
3. **django-cors-headers** - API CORS handling
4. **celery + redis** - Background task processing

## 📝 Notes

- All versions are pinned for reproducible builds
- Comments explain the purpose of each package
- Optional production packages are included but commented
- Regular updates should be tested in development first

## 🔄 Updating Requirements

To update the requirements file with current installed packages:

```bash
pip freeze > requirements.txt
```

To check for outdated packages:
```bash
pip list --outdated
```

The updated `requirements.txt` now includes all necessary packages for the complete Sadaqa crowd funding platform with API functionality.
