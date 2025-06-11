#!/usr/bin/env python
import os
import sys
import django
from datetime import date

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth.models import User
from onlinecourse.models import Course, Lesson, Instructor, Question, Choice

def populate_data():
    # Get admin user
    try:
        admin_user = User.objects.get(username='admin')
    except User.DoesNotExist:
        print("Admin user not found. Please create a superuser first.")
        return
    
    # Create or get instructor
    instructor, created = Instructor.objects.get_or_create(
        user=admin_user,
        defaults={
            'full_time': True,
            'total_learners': 0
        }
    )
    
    # Create course
    course, created = Course.objects.get_or_create(
        name='Learning Django',
        defaults={
            'description': 'Django is an extremely popular and fully featured server-side web framework, written in Python',
            'pub_date': date.today(),
            'total_enrollment': 0
        }
    )
    
    if created:
        course.instructors.add(instructor)
        course.save()
        print(f"Created course: {course.name}")
    
    # Create lesson
    lesson, created = Lesson.objects.get_or_create(
        title='What is Django',
        course=course,
        defaults={
            'order': 0,
            'content': 'Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.'
        }
    )
    
    if created:
        print(f"Created lesson: {lesson.title}")
    
    # Create question
    question, created = Question.objects.get_or_create(
        course=course,
        content='Is Django a Python framework?',
        defaults={
            'grade': 100
        }
    )
    
    if created:
        print(f"Created question: {question.content}")
        
        # Create choices for the question
        choice1 = Choice.objects.create(
            question=question,
            content='Yes',
            is_correct=True
        )
        
        choice2 = Choice.objects.create(
            question=question,
            content='No',
            is_correct=False
        )
        
        print(f"Created choices for question")
    
    # Create another question for better testing
    question2, created = Question.objects.get_or_create(
        course=course,
        content='Which of the following are Django features?',
        defaults={
            'grade': 50
        }
    )
    
    if created:
        print(f"Created question: {question2.content}")
        
        # Create multiple choices for the second question
        choice1 = Choice.objects.create(
            question=question2,
            content='ORM (Object-Relational Mapping)',
            is_correct=True
        )
        
        choice2 = Choice.objects.create(
            question=question2,
            content='Admin Interface',
            is_correct=True
        )
        
        choice3 = Choice.objects.create(
            question=question2,
            content='Template Engine',
            is_correct=True
        )
        
        choice4 = Choice.objects.create(
            question=question2,
            content='Machine Learning',
            is_correct=False
        )
        
        print(f"Created multiple choices for question 2")
    
    print("Database populated successfully!")

if __name__ == '__main__':
    populate_data() 