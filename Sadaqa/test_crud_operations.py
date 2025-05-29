#!/usr/bin/env python
"""
Test script for CRUD operations in the Sadaqa Django project.
This script tests all the API endpoints for complete CRUD functionality.
"""

import os
import sys
import django
import requests
import json
from datetime import datetime, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sadaqa.settings')
django.setup()

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from projects.models import Category, Project, ProjectTag, ProjectPic
from users.models import CustomUser

User = get_user_model()

class CRUDTestRunner:
    def __init__(self):
        self.client = Client()
        self.base_url = 'http://127.0.0.1:8000'
        self.test_user = None
        self.test_category = None
        self.test_project = None
        
    def setup_test_data(self):
        """Create test data for CRUD operations"""
        print("Setting up test data...")
        
        # Create test user
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            phone='+201234567890',
            birthdate='1990-01-01',
            country='EG'
        )
        
        # Create test category
        self.test_category = Category.objects.create(
            name='Test Category',
            desc='Test category description'
        )
        
        print("✅ Test data created successfully")
    
    def cleanup_test_data(self):
        """Clean up test data"""
        print("Cleaning up test data...")
        if self.test_user:
            self.test_user.delete()
        if self.test_category:
            self.test_category.delete()
        print("✅ Test data cleaned up")
    
    def test_user_crud(self):
        """Test User CRUD operations"""
        print("\n🧪 Testing User CRUD Operations...")
        
        # Test User Registration
        print("Testing user registration...")
        registration_data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'password_confirm': 'newpass123',
            'first_name': 'New',
            'last_name': 'User',
            'phone': '+201987654321',
            'birthdate': '1995-05-15',
            'country': 'EG'
        }
        
        response = self.client.post('/users/api/auth/register/', registration_data)
        if response.status_code == 201:
            print("✅ User registration successful")
        else:
            print(f"❌ User registration failed: {response.status_code}")
            print(response.content.decode())
        
        # Test User Login
        print("Testing user login...")
        login_data = {
            'username': 'newuser',
            'password': 'newpass123'
        }
        
        response = self.client.post('/users/api/auth/login/', login_data)
        if response.status_code == 200:
            print("✅ User login successful")
        else:
            print(f"❌ User login failed: {response.status_code}")
        
        # Test User Profile
        print("Testing user profile retrieval...")
        response = self.client.get('/users/api/users/profile/')
        if response.status_code == 200:
            print("✅ User profile retrieval successful")
        else:
            print(f"❌ User profile retrieval failed: {response.status_code}")
    
    def test_category_crud(self):
        """Test Category CRUD operations"""
        print("\n🧪 Testing Category CRUD Operations...")
        
        # Login as test user first
        self.client.login(username='testuser', password='testpass123')
        
        # Test Category List
        print("Testing category list...")
        response = self.client.get('/api/categories/')
        if response.status_code == 200:
            print("✅ Category list successful")
        else:
            print(f"❌ Category list failed: {response.status_code}")
        
        # Test Category Create
        print("Testing category creation...")
        category_data = {
            'name': 'New Test Category',
            'desc': 'New test category description'
        }
        
        response = self.client.post('/api/categories/create/', category_data)
        if response.status_code == 201:
            print("✅ Category creation successful")
            category_id = response.json()['id']
            
            # Test Category Detail
            print("Testing category detail...")
            response = self.client.get(f'/api/categories/{category_id}/')
            if response.status_code == 200:
                print("✅ Category detail successful")
            else:
                print(f"❌ Category detail failed: {response.status_code}")
            
            # Test Category Update
            print("Testing category update...")
            update_data = {
                'name': 'Updated Test Category',
                'desc': 'Updated description'
            }
            response = self.client.put(f'/api/categories/{category_id}/update/', 
                                     json.dumps(update_data), 
                                     content_type='application/json')
            if response.status_code == 200:
                print("✅ Category update successful")
            else:
                print(f"❌ Category update failed: {response.status_code}")
            
            # Test Category Delete
            print("Testing category deletion...")
            response = self.client.delete(f'/api/categories/{category_id}/delete/')
            if response.status_code == 204:
                print("✅ Category deletion successful")
            else:
                print(f"❌ Category deletion failed: {response.status_code}")
        else:
            print(f"❌ Category creation failed: {response.status_code}")
            print(response.content.decode())
    
    def test_project_crud(self):
        """Test Project CRUD operations"""
        print("\n🧪 Testing Project CRUD Operations...")
        
        # Login as test user first
        self.client.login(username='testuser', password='testpass123')
        
        # Test Project List
        print("Testing project list...")
        response = self.client.get('/api/projects/')
        if response.status_code == 200:
            print("✅ Project list successful")
        else:
            print(f"❌ Project list failed: {response.status_code}")
        
        # Test Project Create
        print("Testing project creation...")
        start_date = (datetime.now() + timedelta(days=1)).isoformat()
        end_date = (datetime.now() + timedelta(days=30)).isoformat()
        
        project_data = {
            'title': 'Test Project',
            'details': 'Test project description',
            'total_target': '5000.00',
            'start_date': start_date,
            'end_date': end_date,
            'category': self.test_category.id,
            'status': 'draft'
        }
        
        response = self.client.post('/api/projects/create/', project_data)
        if response.status_code == 201:
            print("✅ Project creation successful")
            project_id = response.json()['id']
            
            # Test Project Detail
            print("Testing project detail...")
            response = self.client.get(f'/api/projects/{project_id}/')
            if response.status_code == 200:
                print("✅ Project detail successful")
            else:
                print(f"❌ Project detail failed: {response.status_code}")
            
            # Test Project Update
            print("Testing project update...")
            update_data = {
                'title': 'Updated Test Project',
                'details': 'Updated project description',
                'total_target': '7500.00',
                'start_date': start_date,
                'end_date': end_date,
                'category': self.test_category.id,
                'status': 'active'
            }
            response = self.client.put(f'/api/projects/{project_id}/update/', 
                                     json.dumps(update_data), 
                                     content_type='application/json')
            if response.status_code == 200:
                print("✅ Project update successful")
            else:
                print(f"❌ Project update failed: {response.status_code}")
                print(response.content.decode())
            
            # Test Project Delete
            print("Testing project deletion...")
            response = self.client.delete(f'/api/projects/{project_id}/delete/')
            if response.status_code == 204:
                print("✅ Project deletion successful")
            else:
                print(f"❌ Project deletion failed: {response.status_code}")
        else:
            print(f"❌ Project creation failed: {response.status_code}")
            print(response.content.decode())
    
    def run_all_tests(self):
        """Run all CRUD tests"""
        print("🚀 Starting CRUD Operations Test Suite")
        print("=" * 50)
        
        try:
            self.setup_test_data()
            self.test_user_crud()
            self.test_category_crud()
            self.test_project_crud()
            
            print("\n" + "=" * 50)
            print("✅ All CRUD tests completed!")
            
        except Exception as e:
            print(f"\n❌ Test suite failed with error: {str(e)}")
            import traceback
            traceback.print_exc()
        
        finally:
            self.cleanup_test_data()

if __name__ == '__main__':
    test_runner = CRUDTestRunner()
    test_runner.run_all_tests()
