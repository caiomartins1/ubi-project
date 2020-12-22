# PWA Project

# Project setup

Follow this steps to run the project on your machine.

1. Clone the repository

```bash
  cd your_workspace
  git clone https://github.com/caiomartins1/ubi-project.git
  cd ubi-project
```

2. Start the backend

```bash
  # Make sure you are in the ubi-project root directory
  cd backend

  # Create a new virtual enviroment
  python3 -v venv venv

  # Activate your venv
  source venv/bin/activate

  # Change directory to django app folder
  cd ubi_project

  # Install project dependencies in your venv
  pip install -r requirements.txt

  # Setup .ENV variables
    # Rename ubi_project/ubi_project/.env.example to ubi_project/ubi_project/.env
    # Fill the variables with your postgresql credentials

  # Run the migrations
  python manage.py migrate

  # Ready to go! Start server
  python manage.py runserver

```
