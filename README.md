# Closest Points Django Application

This Django application provides an API that receives a set of points on a grid as semicolon-separated values and finds the points that are closest to each other. The application stores the received set of points and their closest points in a database.

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework

## Installation

1. Clone the repository:

    git clone https://github.com/Frankieamenya/closest-points-project.git


2. Change into the project directory:

    cd closest-points-project

3. Create a virtual environment (optional but recommended):

    python -m venv venv
4. Activate the virtual environment:

- On Windows:


venv\Scripts\activate
-On macOS/Linux:

source venv/bin/activate

-Install the required packages:

pip install -r requirements.txt


## Configuration

1. Open the `closest_points_project/settings.py` file and make sure the following configurations are set correctly:
- Database settings (MySQL localhost)
- Allowed hosts (`ALLOWED_HOSTS`)
- Secret key (`SECRET_KEY`)

2. Apply database migrations:
   python manage.py migrate

## Usage
1. Run the development server:

    python manage.py runserver

2. Access the API endpoint:

    http://localhost:8000/api/find-closest-points/
3. Send a POST request to the API with the points in the request body. For example:

    curl -X POST -H "Content-Type: application/json" -d '{"points": "2,2;-1,30;20,11;4,5"}' http://localhost:8000/api/find-closest-points/

The response will contain the closest points in the following format:

    json

    {
    "closest_points": [[2, 2], [4, 5]]
    }

## Admin Interface
The application also provides an admin interface for viewing the values stored in the database.

1. Create a superuser:

    python manage.py createsuperuser

2. Start the development server (if not already running):

    python manage.py runserver

3. Access the admin interface:

   http://localhost:8000/admin/

4. Log in with the superuser credentials.

You can now view and manage the Point objects in the database using the admin interface.

## Running Tests
To run unit tests, execute the following command:
    python manage.py test

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to modify and use this project according to your needs.

