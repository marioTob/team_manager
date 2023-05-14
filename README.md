# team_manager

## Description:
Team Management App - backend (rest framework) of an app that can be used by production companies to manage its employees on a production floor.

App is displaying list of all USERS (employees) and PLACES (workstations where work is performed), both with CRUD options.

## Setting environment:
1. **Clone Repository from GitHub** <br />
2. **Crete and Activate Virtual Environment** <br />
3. **Install:** <br />
    `pip install Django` <br />
    `pip install djangorestframework` <br />
    
## App setup:
1. **Prepare migrations** <br />
    `python manage.py makemigrations` <br />
2. **Migrate** <br />
    `python manage.py migrate` <br />
3. **Create superuser** <br />
    `python manage.py createsuperuser` <br />
4. **Run server** <br />
    `python manage.py runserver` <br />
    
## Test:
URLS: <br />
http://127.0.0.1:8000/user - list of all Users <br />
http://127.0.0.1:8000/user/add - add new User <br />
http://127.0.0.1:8000/place - list of all Places <br />

Request format for create/update USER model:  <br />
`{ <br />
        "first_name": "Bruce", <br />
        "last_name": "Banner", <br />
        "mobile": "0048123456789", <br />
        "mail": "green@av.com", <br />
        "position": "scientist", <br />
        "hire_date": "2010-05-14", <br />
        "leave_date": null, <br /> 
        "updated": "2023-05-14T19:21:07.130056Z" <br />
}` <br />

Request format for create/update PLACE model:  <br />
    
