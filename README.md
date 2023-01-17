# Prerequisites

- Efficient code editor (For eg. Visual studio Code)
- Install python IDLE,Node JS.
- Basic knowledge in html,tailwindcss,python.

# Packages

Inorder to run the project on machine the following packages should be pre-installed.


## Virtual Environment

It is necessary to create a virtual environment which in turn is used to work with Django project.

        pip install virtualenv
        
## Node JS

Node JS is installed to deal with tailwindcss.

        install node.js
        
Then navigate to the django environment by executing

        cd mysite
        
#### Note:mysite-name of the application

Then execute

        npm init -y
        npm install tailwindcss@2.2.16
        npm run build

## Pillow

Inorder to deal with the images used,install the pillow package

        pip install pillow
        
# Steps to create a django applicatoon

## Creating a virtual environment

A virtual environment can be created and activated by executibg the following commands

        virtualenv envname
        cd envname
        cd Scripts
        activate
        
## Creating a django project 

A django project is created by executing the command

        django-admin startproject mysite
        
#### Note:mysite-projectname

## Creating a django apllication 

A django application is created by executing the command

        python manage.py startapp myapp
        
#### Note:myapp-apllicationtname

## Creating a database

- Define the database in models.py file.
- Then perform migrations using the commands
        
        python manage.py makemigrations
        python manage.py migrate
        
## Running the application

The django apllication can run on local machine using the default server which comes along with the django package.

        python manage.py runserver
        
Copy paste the link provided by the command prompt in any of the browser.

# Demo Link

[click here to view the demo](https://drive.google.com/file/d/1mlal5y_2HEjWJtuRT4Zf1ewgnKjiVouA/view?usp=sharing)







