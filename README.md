# team_manager

## Description:
Team Management App - backend (rest_framework) of an app used by production company to manage its employees on a production floor.

* App is displaying lists of all USERS (employees) and PLACES (workstations where work is performed), both with CRUD operations.
* USERS have many-to-many relationship with PLACES through EXPERIENCE model (model with 'create' and 'update' operations).
* EXPERIENCE model has additional field 'level' (which describes the experence of an emplyee in a given workstation - for example in the range of 0-5).
* Displaying list of all USERS (or a single USER) gives information about his level of experience in assigned PLACES.
* Level of experience can be edited.

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
1. Create USERS (employees)
2. Create PLACES (workstations)
3. Connect USERS with PLACES

URLS - examples: <br />
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
        "leave_date": null
}` <br />
http://127.0.0.1:8000/user/1/update/ - update new User <br />
http://127.0.0.1:8000/user/1/delete/ - delete User <br />
<br />
<br />
http://127.0.0.1:8000/place - list of all Places <br />
http://127.0.0.1:8000/place/1 - single Place <br />
http://127.0.0.1:8000/place/add - add new Place <br />
request format: `{
        "name": "Milling 1",
        "description": "5-axis milling"
}` <br />
http://127.0.0.1:8000/place/1/update/ - update Place <br />
http://127.0.0.1:8000/place/1/delete - delete Place <br />
<br />    
<br />
http://127.0.0.1:8000/experience/add - add new Experience <br />
http://127.0.0.1:8000/experience/update - update Experience <br />
request format: `{
        "user": 1,
        "place": 1,
        "level": 5
}` <br />