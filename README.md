## [Front-end repository][front]
# Travel Planner
Travel planner is a web application where users can create a planner for their own trip. In a planner; the user can specify arrival and departure dates, select places to visit by searching from maps, and set time that they want to spend at each place. The planner will show time remaining in each day, and display the time that takes user to travel from one place to another.

Traivis CI : [![Build Status](https://travis-ci.com/narisasingngam/TravelPlanner.svg?branch=master)](https://travis-ci.com/narisasingngam/TravelPlanner)

Code Coverage : [![codecov](https://codecov.io/gh/narisasingngam/Travel-Planner/branch/master/graph/badge.svg)](https://codecov.io/gh/narisasingngam/Travel-Planner)


# Documents

+ Task Board - [Task Management][task]

+ Iteration Plan - [Documentation][doc]

+ Issue tracking - [Issue Tracker](https://github.com/narisasingngam/TravelPlanner/issues)

# Installation

+ Python (v.3 or newer)  -  [download](https://www.python.org/downloads/)

+ Node.js - [download](https://nodejs.org/en/)

+ Virtual Environment
    ```
    $ pip install virtualenv
    ```

# Step needed to configure the application for running

### For frontend

1. Clone the [frontend repository][front]
``` 
$ git clone https://github.com/ffaiip/TravelPlanner-App.git
 ``` 

2. Install dependencies
```
$ npm install
```
3.  Compile
```
$ npm run dev

- Run serve with localhost:8080
```

### For backend

1. Clone the backend repository.
``` 
$ git clone https://github.com/narisasingngam/TravelPlanner.git

$ cd TravelPlanner
 ```

2. Create your virtual environment
```
$ virtualenv env
```
3. Activate environment

```
For MacOs or Ubuntu

> $ source env/bin/activate

For Window

> $ env/Scripts/activate
 ```

4. Install dependencies with **pip**
``` 
$ pip install -r requirements.txt
 ```

5. If you want to use SQLite database
```
$ python manage.py migrate
```

6. For backend compiled

``` 
$ python manage.py runserver

- Run serve with localhost:8000
 ```

 # Members
| GitHub  | Name              | 
|--------|-----------------------------|
| @narisasingngam   | Narisa Singngam |
| @ffaiip | Kavinthip Pattanaphaophan |
| @jampttws | Tanasorn Tritawisup |



[doc]:https://docs.google.com/document/d/17YU4U-z9ftI0GzMlQQTGfNDjZDice1K9bn1NK7oGFBY/edit#
[task]:https://trello.com/b/wfRyjm44/work-plan
[front]:https://github.com/ffaiip/TravelPlanner-App
