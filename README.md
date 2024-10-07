# Job Recommendation Service

A Django-based REST API service that provides job recommendations based on user profiles and preferences. The service uses a sophisticated matching algorithm to suggest the most relevant job opportunities to users based on their skills, experience level, and preferences.

## Features

- **User Profile Management**: Create and manage user profiles with skills and experience levels
- **Job Posting Management**: Full CRUD operations for job postings
- **Preference-based Matching**: Advanced recommendation algorithm considering multiple factors:
  - Skills matching (40% weight)
  - Experience level compatibility (20% weight)
  - Location preferences (20% weight)
  - Job type alignment (10% weight)
  - Role matching (10% weight)
- **RESTful API**: Complete API endpoints for all operations
- **PostgreSQL Integration**: Utilizes PostgreSQL's ArrayField for efficient data storage
- **Admin Interface**: Built-in Django admin interface for easy data management

## Technology Stack

- Python 3.8+
- Django 4.2+
- Django REST Framework
- PostgreSQL
- psycopg2-binary

## Project Structure

```
job_recommender/
├── manage.py
├── job_recommender/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── jobs/
    ├── __init__.py
    ├── models.py        # Database models
    ├── serializers.py   # API serializers
    ├── views.py         # API views and endpoints
    ├── urls.py          # URL routing
    └── recommendation.py # Recommendation logic
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/job-recommender.git
cd job-recommender
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a PostgreSQL database and update settings:

Edit `job_recommender/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'job_recommender',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### User Profiles

- `GET /api/users/`: List all user profiles
- `POST /api/users/`: Create a new user profile
- `GET /api/users/{id}/`: Retrieve a specific user profile
- `PUT /api/users/{id}/`: Update a user profile
- `DELETE /api/users/{id}/`: Delete a user profile
- `GET /api/users/{id}/recommendations/`: Get job recommendations for a user

### Jobs

- `GET /api/jobs/`: List all jobs
- `POST /api/jobs/`: Create a new job posting
- `GET /api/jobs/{id}/`: Retrieve a specific job
- `PUT /api/jobs/{id}/`: Update a job posting
- `DELETE /api/jobs/{id}/`: Delete a job posting

## Data Models

### UserProfile
```python
{
    "name": "string",
    "skills": ["string"],
    "experience_level": "string" // Junior, Intermediate, Senior
    "preferences": {
        "desired_roles": ["string"],
        "locations": ["string"],
        "job_type": "string", // Full-Time, Part-Time, Contract
        "min_salary": "integer",
        "remote_only": "boolean"
    }
}
```

### Job
```python
{
    "title": "string",
    "company": "string",
    "required_skills": ["string"],
    "location": "string",
    "job_type": "string", // Full-Time, Part-Time, Contract
    "experience_level": "string", // Junior, Intermediate, Senior
    "description": "string",
    "salary_range_min": "integer",
    "salary_range_max": "integer",
    "is_remote": "boolean"
}
```

## Recommendation Algorithm

The service uses a weighted scoring system to match users with jobs:

1. **Skills Match (40%)**
   - Calculates the overlap between user skills and job required skills
   - Score = (matching skills / total required skills) * 0.4

2. **Experience Level Match (20%)**
   - Exact match = 0.2
   - No match = 0

3. **Location Match (20%)**
   - Location in user's preferred locations = 0.2
   - Location not in preferences = 0

4. **Job Type Match (10%)**
   - Exact match = 0.1
   - No match = 0

5. **Desired Role Match (10%)**
   - Job title matches desired roles = 0.1
   - No match = 0

Jobs are filtered based on user preferences before scoring, and only the top 10 recommendations are returned by default.

## Usage Examples

### Creating a User Profile

```bash
curl -X POST http://localhost:8000/api/users/ \
-H "Content-Type: application/json" \
-d '{
    "name": "John Doe",
    "skills": ["Python", "Django", "REST APIs"],
    "experience_level": "Intermediate",
    "preferences": {
        "desired_roles": ["Backend Developer", "Software Engineer"],
        "locations": ["Remote", "New York"],
        "job_type": "Full-Time",
        "remote_only": true
    }
}'
```

### Getting Recommendations

```bash
curl http://localhost:8000/api/users/1/recommendations/
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
The project follows PEP 8 style guide. To check code style:
```bash
flake8 .
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.# PeopleBoxExcercise
