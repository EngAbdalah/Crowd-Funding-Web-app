# Sadaqa Crowd Funding API Documentation

## Overview
This document provides comprehensive documentation for all CRUD (Create, Read, Update, Delete) operations available in the Sadaqa Crowd Funding Web Application API.

## Base URL
```
http://127.0.0.1:8000
```

## Authentication
The API uses Django's session-based authentication. Most endpoints require authentication except for public read operations and user registration.

## Response Format
All API responses are in JSON format with appropriate HTTP status codes.

---

## User Management API

### Authentication Endpoints

#### Register User
- **URL**: `/users/api/auth/register/`
- **Method**: `POST`
- **Permission**: Public
- **Request Body**:
```json
{
    "username": "string",
    "email": "string",
    "password": "string",
    "password_confirm": "string",
    "first_name": "string",
    "last_name": "string",
    "phone": "+201234567890",
    "birthdate": "1990-01-01",
    "country": "EG"
}
```
- **Response**: `201 Created` with user data

#### Login User
- **URL**: `/users/api/auth/login/`
- **Method**: `POST`
- **Permission**: Public
- **Request Body**:
```json
{
    "username": "string",
    "password": "string"
}
```
- **Response**: `200 OK` with user data

#### Logout User
- **URL**: `/users/api/auth/logout/`
- **Method**: `POST`
- **Permission**: Authenticated
- **Response**: `200 OK`

### User CRUD Endpoints

#### List Users (Admin Only)
- **URL**: `/users/api/users/`
- **Method**: `GET`
- **Permission**: Admin
- **Response**: `200 OK` with list of users

#### Get User Profile
- **URL**: `/users/api/users/profile/`
- **Method**: `GET`
- **Permission**: Authenticated
- **Response**: `200 OK` with current user data

#### Get Specific User
- **URL**: `/users/api/users/{id}/`
- **Method**: `GET`
- **Permission**: Authenticated (own profile) or Admin
- **Response**: `200 OK` with user data

#### Update User Profile
- **URL**: `/users/api/users/profile/update/`
- **Method**: `PUT/PATCH`
- **Permission**: Authenticated
- **Request Body**:
```json
{
    "first_name": "string",
    "last_name": "string",
    "email": "string",
    "phone": "+201234567890",
    "birthdate": "1990-01-01",
    "country": "EG"
}
```
- **Response**: `200 OK` with updated user data

#### Change Password
- **URL**: `/users/api/users/change-password/`
- **Method**: `POST`
- **Permission**: Authenticated
- **Request Body**:
```json
{
    "old_password": "string",
    "new_password": "string",
    "new_password_confirm": "string"
}
```
- **Response**: `200 OK`

#### Deactivate User Account
- **URL**: `/users/api/users/delete/`
- **Method**: `DELETE`
- **Permission**: Authenticated
- **Response**: `200 OK`

---

## Projects Management API

### Project Endpoints

#### List Projects
- **URL**: `/api/projects/`
- **Method**: `GET`
- **Permission**: Public
- **Response**: `200 OK` with list of projects

#### Create Project
- **URL**: `/api/projects/create/`
- **Method**: `POST`
- **Permission**: Authenticated
- **Request Body**:
```json
{
    "title": "string",
    "details": "string",
    "total_target": "5000.00",
    "start_date": "2024-01-01T00:00:00Z",
    "end_date": "2024-12-31T23:59:59Z",
    "category": 1,
    "status": "draft"
}
```
- **Response**: `201 Created` with project data

#### Get Project Details
- **URL**: `/api/projects/{id}/`
- **Method**: `GET`
- **Permission**: Public
- **Response**: `200 OK` with project data

#### Update Project
- **URL**: `/api/projects/{id}/update/`
- **Method**: `PUT/PATCH`
- **Permission**: Authenticated (project owner)
- **Request Body**: Same as create project
- **Response**: `200 OK` with updated project data

#### Delete Project
- **URL**: `/api/projects/{id}/delete/`
- **Method**: `DELETE`
- **Permission**: Authenticated (project owner)
- **Response**: `204 No Content`

### Category Endpoints

#### List Categories
- **URL**: `/api/categories/`
- **Method**: `GET`
- **Permission**: Public
- **Response**: `200 OK` with list of categories

#### Create Category
- **URL**: `/api/categories/create/`
- **Method**: `POST`
- **Permission**: Authenticated
- **Request Body**:
```json
{
    "name": "string",
    "desc": "string"
}
```
- **Response**: `201 Created` with category data

#### Get Category Details
- **URL**: `/api/categories/{id}/`
- **Method**: `GET`
- **Permission**: Public
- **Response**: `200 OK` with category data

#### Update Category
- **URL**: `/api/categories/{id}/update/`
- **Method**: `PUT/PATCH`
- **Permission**: Authenticated
- **Request Body**: Same as create category
- **Response**: `200 OK` with updated category data

#### Delete Category
- **URL**: `/api/categories/{id}/delete/`
- **Method**: `DELETE`
- **Permission**: Authenticated
- **Response**: `204 No Content`

### Project Tag Endpoints

#### List Project Tags
- **URL**: `/api/project-tags/`
- **Method**: `GET`
- **Permission**: Public
- **Query Parameters**: `project_id` (optional)
- **Response**: `200 OK` with list of tags

#### Create Project Tag
- **URL**: `/api/project-tags/create/`
- **Method**: `POST`
- **Permission**: Authenticated
- **Request Body**:
```json
{
    "project": 1,
    "tagname": "string"
}
```
- **Response**: `201 Created` with tag data

#### Get Project Tag Details
- **URL**: `/api/project-tags/{id}/`
- **Method**: `GET`
- **Permission**: Public
- **Response**: `200 OK` with tag data

#### Update Project Tag
- **URL**: `/api/project-tags/{id}/update/`
- **Method**: `PUT/PATCH`
- **Permission**: Authenticated
- **Request Body**: Same as create tag
- **Response**: `200 OK` with updated tag data

#### Delete Project Tag
- **URL**: `/api/project-tags/{id}/delete/`
- **Method**: `DELETE`
- **Permission**: Authenticated
- **Response**: `204 No Content`

### Project Picture Endpoints

#### List Project Pictures
- **URL**: `/api/project-pics/`
- **Method**: `GET`
- **Permission**: Public
- **Query Parameters**: `project_id` (optional)
- **Response**: `200 OK` with list of pictures

#### Create Project Picture
- **URL**: `/api/project-pics/create/`
- **Method**: `POST`
- **Permission**: Authenticated
- **Request Body**: Form data with `project` and `pic` fields
- **Response**: `201 Created` with picture data

#### Get Project Picture Details
- **URL**: `/api/project-pics/{id}/`
- **Method**: `GET`
- **Permission**: Public
- **Response**: `200 OK` with picture data

#### Update Project Picture
- **URL**: `/api/project-pics/{id}/update/`
- **Method**: `PUT/PATCH`
- **Permission**: Authenticated
- **Request Body**: Form data with updated fields
- **Response**: `200 OK` with updated picture data

#### Delete Project Picture
- **URL**: `/api/project-pics/{id}/delete/`
- **Method**: `DELETE`
- **Permission**: Authenticated
- **Response**: `204 No Content`

---

## Error Responses

### Common Error Codes
- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Permission denied
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

### Error Response Format
```json
{
    "error": "Error message description",
    "details": "Additional error details (optional)"
}
```

---

## Database Indexes

The following indexes have been optimized for CRUD operations:

### Project Model Indexes
- `user`, `category`, `status`, `created_at`, `start_date`, `end_date`, `is_cancelled`
- Composite indexes: `(status, created_at)`, `(user, status)`, `(category, status)`

### User Model Indexes
- `email`, `phone`, `country`, `is_active`, `date_joined`
- Composite indexes: `(is_active, date_joined)`

### Category Model Indexes
- `name`

### ProjectTag Model Indexes
- `project`, `tagname`
- Composite indexes: `(project, tagname)`
- Unique constraint: `(project, tagname)`

### ProjectPic Model Indexes
- `project`

---

## Testing

Run the comprehensive test suite:
```bash
python test_crud_operations.py
```

This will test all CRUD operations for all models and provide detailed feedback on the API functionality.
