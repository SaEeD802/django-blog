# Django Blog Project

This project is a simple blog that utilizes the Django framework for its backend. Class-Based Views have been used for implementing the web pages in this blog.

## Features

- Users can like posts and share them on LinkedIn and WhatsApp.

## Installation

1. Make sure you have set up and activated your `venv`.

2. Install the required libraries from the `requirements.txt` file:



```py
pip install -r requirements.txt
```

3. Run the necessary migrations:

```py
py manage.py makemigrations
py manage.py migrate
```

4. Launch the development server with the following command:

```py
py manage.py runserver
```



## Apps

The project includes three apps with the following names:

- `home`
- `accoun`
- `blog`

## Packages

Additionally, the following packages have been used for specific functionalities:

- `django_cleanup.apps.CleanupConfig`
- `django_render_partial`
- `django_social_share`
- `widget_tweaks`

</br>

**Note:** Make sure your `venv` is active and you've completed all the necessary steps to run the project.


