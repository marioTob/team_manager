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
http://127.0.0.1:8000/user/1 - single User <br />
http://127.0.0.1:8000/user/add - add new User <br />
request format: `{
        "first_name": "Bruce",
        "last_name": "Banner",
        "mobile": "0048123456789",
        "mail": "green@av.com",
        "position": "scientist",
        "hire_date": "2010-05-14",
        "leave_date": null,
        "updated": ""
}` <br />
http://127.0.0.1:8000/user/1/delete/ - add new User <br />

http://127.0.0.1:8000/place - list of all Places <br />
http://127.0.0.1:8000/place/1 - single Place <br />
http://127.0.0.1:8000/place/add - add new Place <br />
request format: `{
        "name": "Milling 1",
        "description": "5-axis milling",
        "updated": ""
}` <br />
http://127.0.0.1:8000/place/1/delete - add new User <br />
    
