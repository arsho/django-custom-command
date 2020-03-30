## Django Custom Command Example with Django Docs Polls Application
This is the code repository of the following tutorial: [https://arshovon.com/blog/django-custom-command/](https://arshovon.com/blog/django-custom-command/)

I have used Django Docs Example Polls Application to demonstrate Django Custom Command.

### Directory Structure

```
.
├── mysite
│   ├── manage.py
│   ├── mysite
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── polls
│       ├── admin.py
│       ├── apps.py
│       ├── __init__.py
│       ├── management
│       │   └── commands
│       │       ├── command_utils.py
│       │       ├── insert_dummy_questions.py
│       │       └── questions.csv
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   └── __init__.py
│       ├── models.py
│       ├── templates
│       │   └── polls
│       │       ├── detail.html
│       │       ├── index.html
│       │       └── results.html
│       ├── tests.py
│       ├── urls.py
│       └── views.py
└── requirements.txt
```

### Installing Requirements
- Python version: 3.6+
- Create virtual environment:
    ```
    python3 -m venv venv
    ```
- Activate virtual environment:
    ```
    source venv/bin/activate
    ```
- Install required packages:
    ```
    pip install -r requirements.txt
    ```
### Database Migration
- Create migration:
    ```
    python manage.py makemigrations
    ```
- Migrate migrations:
    ```
    python manage.py migrate
    ```
- Create super user:
    ```
    python manage.py createsuperuser
    ```

### Run the project
- Run the project from the root directory of Django project:
    ```
    python manage.py runserver
    ```

### Run Django Custom Command
- Run Django custom command `help` context:
    ```
    python manage.py insert_dummy_questions --help
    ```
    
    ![alt Django Custom Command Help context](/screenshots/django_custom_command_help.png?style=center)

- Run Django custom command:

    ```
    python manage.py insert_dummy_questions questions.csv
    ```

    ![alt Django Custom Command](/screenshots/running_custom_django_command.png?style=center)

- After running Django custom command the CSV file data is inserted into database:

![alt Polls page](/screenshots/polls_custom_django_command.png?style=center)  


### Reference
- [Writing Django Custom Management Command](https://arshovon.com/blog/django-custom-command/)
- [Custom commands in Django](https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
- [Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
