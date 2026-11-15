# Django Docker App

## Project Description
This is a Django web application developed using Docker. It contains two applications: Home and Menu.

## Technologies Used
- Python
- Django 5.2
- Docker
- Docker Compose
- Git and GitHub
- GitHub Actions

## Project Structure
- `config/` - Main Django project configuration
- `home/` - Home application
- `menu/` - Menu application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Instructions to build the Docker image
- `compose.yaml` - Docker services configuration

## Setup Instructions

1. Clone the repository:
   `git clone https://github.com/shahryar32512/django-docker-app.git`

2. Move into the project directory:
   `cd django-docker-app`

3. Create a `.env` file in the project root and add your own secret key:
   `SECRET_KEY=your-secret-key`

4. Build the Docker image:
   `docker compose build`

5. Start the Django development server:
   `docker compose run --rm --service-ports web python manage.py runserver 0.0.0.0:8000`

## Useful Commands

Run Django tests:
`docker compose run --rm web python manage.py test`

Check Django configuration:
`docker compose run --rm web python manage.py check`

## Health Check

Open the following URL in your browser:

`http://localhost:8000/health/`

Expected response: `OK`

## Settings

- Development settings: `config.settings.development`
- Production settings: `config.settings.production`
- Common settings: `config.settings.base`

## Continuous Integration

GitHub Actions automatically runs Django tests when code is pushed or a Pull Request is created for the configured branches.