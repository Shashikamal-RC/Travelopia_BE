# Travelopia Backend APIs

## Please follow below steps to setup backend server

    1. Make sure you have Python and Pip is running in your machine.
    2. install pipenv using below command
                pip install pipenv
    3. Navigate inside the application where you can locate Pipfile.
    4. Run the following command to create a virtual environment.
                pipenv shell
    5. Navigate inside the project folder where you can find setting.py file.
        Under the same folder create .env file and update following database
        configurations variables.
            DB_NAME=db_name
            DB_USERNAME=db_username
            DB_PASSWORD=db_password
            DB_HOST=db_host
            DB_PORT=db_port
        NOTE: Currently application is configured for MySQL server.
    6. After updating the configurations create a database with the given name.
    7. Run the following commands to create tables.
            python manage.py makemigations
            python manage.py migrate
    8. Now the database setup is completed.
    9. You can start the application by running following command
            python manage.py runserver