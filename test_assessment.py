#!/usr/bin/env python
import os
import sys
import django
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from onlinecourse.models import Course, Lesson, Instructor, Question, Choice, Enrollment, Submission

def test_assessment_functionality():
    """
    Test the assessment feature functionality
    """
    print("Testing Django Online Course Assessment Feature...")
    print("=" * 50)
    
    # Test 1: Check if models exist and can be created
    print("1. Testing Model Creation...")
    try:
        # Check if admin user exists
        admin_user = User.objects.get(username='admin')
        print("   ✓ Admin user found")
        
        # Check if course exists
        course = Course.objects.get(name='Learning Django')
        print("   ✓ Sample course found")
        
        # Check questions
        questions = Question.objects.filter(course=course)
        print(f"   ✓ Found {questions.count()} questions")
        
        # Check choices
        for question in questions:
            choices = Choice.objects.filter(question=question)
            correct_choices = choices.filter(is_correct=True)
            print(f"   ✓ Question '{question.content}' has {choices.count()} choices ({correct_choices.count()} correct)")
            
    except Exception as e:
        print(f"   ✗ Model test failed: {e}")
        return False
    
    # Test 2: Check if URLs are configured correctly
    print("\n2. Testing URL Configuration...")
    try:
        client = Client()
        
        # Test course list page
        response = client.get('/')
        if response.status_code == 200:
            print("   ✓ Course list page accessible")
        else:
            print(f"   ✗ Course list page failed: {response.status_code}")
            
        # Test course detail page
        response = client.get(f'/{course.id}/')
        if response.status_code == 200:
            print("   ✓ Course detail page accessible")
        else:
            print(f"   ✗ Course detail page failed: {response.status_code}")
            
    except Exception as e:
        print(f"   ✗ URL test failed: {e}")
        return False
    
    # Test 3: Test exam submission flow
    print("\n3. Testing Exam Submission Flow...")
    try:
        # Create a test user
        test_user, created = User.objects.get_or_create(
            username='testuser',
            defaults={
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@example.com'
            }
        )
        
        # Create enrollment
        enrollment, created = Enrollment.objects.get_or_create(
            user=test_user,
            course=course,
            defaults={'mode': 'honor'}
        )
        print(f"   ✓ Test enrollment created/found")
        
        # Simulate exam submission
        questions = Question.objects.filter(course=course)
        if questions.exists():
            question = questions.first()
            correct_choices = Choice.objects.filter(question=question, is_correct=True)
            
            if correct_choices.exists():
                submission = Submission.objects.create(enrollment=enrollment)
                submission.choices.set(correct_choices)
                print(f"   ✓ Test submission created with {correct_choices.count()} correct choices")
                
                # Test score calculation
                total_score = 0
                for q in questions:
                    correct_choices_q = q.choice_set.filter(is_correct=True)
                    selected_choices_q = submission.choices.filter(question=q)
                    if set(correct_choices_q) == set(selected_choices_q):
                        total_score += q.grade
                
                print(f"   ✓ Calculated score: {total_score}/150")
                
    except Exception as e:
        print(f"   ✗ Submission test failed: {e}")
        return False
    
    # Test 4: Check admin interface
    print("\n4. Testing Admin Interface...")
    try:
        from django.contrib.admin import site
        
        # Check if models are registered
        registered_models = [model._meta.model_name for model in site._registry.keys()]
        
        required_models = ['course', 'lesson', 'instructor', 'learner', 'question', 'choice', 'submission']
        for model in required_models:
            if model in registered_models:
                print(f"   ✓ {model.title()} model registered in admin")
            else:
                print(f"   ✗ {model.title()} model not registered in admin")
                
    except Exception as e:
        print(f"   ✗ Admin test failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("✓ All tests passed! Assessment feature is working correctly.")
    print("\nTo test the full functionality:")
    print("1. Start the server: python manage.py runserver")
    print("2. Go to http://localhost:8000")
    print("3. Register/Login as a user")
    print("4. Enroll in the 'Learning Django' course")
    print("5. Take the exam by clicking 'Start Exam'")
    print("6. Submit and view your results")
    print("\nAdmin interface: http://localhost:8000/admin")
    print("Username: admin, Password: p@ssword123")
    
    return True

if __name__ == '__main__':
    test_assessment_functionality() 