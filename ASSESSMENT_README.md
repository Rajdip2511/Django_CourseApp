# Django Online Course Assessment Feature

This project implements a comprehensive assessment feature for an online course application built with Django.

## Features Implemented

### 1. Database Models
- **Question Model**: Stores exam questions with content, grade points, and course relationship
- **Choice Model**: Stores multiple choice options for each question with correctness indicator
- **Submission Model**: Tracks user exam submissions and selected choices

### 2. Admin Interface
- Enhanced Django admin with inline editing for Questions and Choices
- Easy management of course assessments through admin interface
- Registered all new models for administrative access

### 3. Exam Interface
- Interactive exam section in course detail page (visible only to authenticated users)
- Bootstrap-styled collapsible exam interface
- Multiple choice questions with checkbox selections
- Form submission to evaluate exam results

### 4. Result Evaluation
- Automated scoring system based on correct answer matching
- Pass/fail determination (passing score: 80+)
- Detailed result breakdown showing:
  - Correct answers (green)
  - Missed correct answers (yellow)
  - Wrong selections (red)
  - Unselected options (gray)

### 5. User Experience
- Modern, responsive Bootstrap UI
- Congratulations message for passing students
- Retake option for failed attempts
- Clear visual feedback on answer correctness

## Technical Implementation

### Models Structure
```python
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=50)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
```

### URL Patterns
- `/course/<id>/submit/` - Exam submission endpoint
- `/course/<course_id>/submission/<submission_id>/result/` - Results display

### Views
- `submit()` - Processes exam submissions and creates submission records
- `show_exam_result()` - Evaluates scores and renders results

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rajdip2511/Django_CourseApp.git
   cd Django_CourseApp
   ```

2. **Set up virtual environment**
   ```bash
   pip install virtualenv
   virtualenv djangoenv
   source djangoenv/bin/activate  # Linux/Mac
   # or
   .\djangoenv\Scripts\Activate.ps1  # Windows PowerShell
   ```

3. **Install dependencies**
   ```bash
   pip install Django==4.2.3 Pillow
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations onlinecourse
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Populate sample data**
   ```bash
   python populate_data.py
   ```

7. **Run the server**
   ```bash
   python manage.py runserver
   ```

## Sample Data

The project includes a population script that creates:
- Sample course: "Learning Django"
- Sample lesson: "What is Django"
- Sample questions with multiple choice options
- Admin user configuration

## Usage

1. **Access the application** at `http://localhost:8000`
2. **Login** with your credentials
3. **Enroll** in a course
4. **Take the exam** by clicking "Start Exam" button
5. **View results** after submission

## Admin Interface

Access the admin interface at `http://localhost:8000/admin` to:
- Create and manage courses
- Add questions and choices
- View submissions and results
- Manage users and enrollments

## Assessment Criteria

- **Passing Score**: 80/100
- **Question Types**: Multiple choice with single or multiple correct answers
- **Scoring**: Full credit only when all correct answers are selected
- **Retake**: Available for failed attempts

## Code Quality Features

- Clean, readable code with proper comments
- Responsive Bootstrap UI design
- Proper error handling
- Django best practices implementation
- Comprehensive model relationships
- Secure form handling with CSRF protection

## Future Enhancements

- Timer-based exams
- Question randomization
- Different question types (essay, true/false)
- Detailed analytics and reporting
- Email notifications for exam results
- Bulk question import functionality

## Contributors

- Senior Full-Stack Developer Implementation
- Bootstrap UI/UX Design
- Django Backend Architecture
- Database Design and Optimization 