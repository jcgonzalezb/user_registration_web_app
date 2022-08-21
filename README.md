# User registration web application
> This project is a web application to create a user registration service and to show the users created.

## Objectives

- Creating a user registration service that receives a name, email and city. 
- Allowing check the list of users created by the registration service. 

## Table of content

* [Architecture](#architecture)
	* [Technology Stack](#technology-stack)
	* [Database Diagram Model](#database-diagram-model)
* [Environment](#environment)
	* [File Descriptions](#file-descriptions)
	* [Web Application Endpoints](#web-application-endpoints)
* [Installation](#installation)
* [Usage](#usage)
* [Bugs](#bugs)
* [Author](#author)
* [License](#license)

##  Architecture
###  Technology Stack
![Web infrastructure stack image](documentation/images/tech_project.png)

###  Database Diagram Model

![Log trading log ERR Diagram](documentation/images/db.png)

##  Environment
This project was developed on Ubuntu 20.04 LTS using python 3.10.4 with flask framework, connecting to a SQLite Database.

### File Descriptions

- ```app.py```  contains the entry point of the web application.
- ```config.py```  contains the configuration settings for the web application.
- ```users.db```  contains the database configured for this project (data not included).
- ```models/``` contains classes used for this project.
- ```routes/``` contains endpoints implemented for the web application.
- ```routes/home_blueprint.py``` show welcome message for the user and links to create users and to show a list of users.
- ```routes/new_user_blueprint.py``` implemented routes to create users.
- ```routes/user_list_blueprint.py``` implemented routes to check the list of users created.
- ```templates/``` contains html files used to show users and trades.
- ```forms/``` contains forms used fot this project.
- ```forms/form.py``` implements a form to create new users.
- ```documentation/``` contains files used for endpoints of the web application.
- ```documentation/images``` contains images used in the readme.md file and the web application.


### Web Application Endpoints

This is the list of available endpoints for this project.

|Method          |Path                           |Description                  |
|----------------|-------------------------------|-----------------------------|
|GET             |```/```                        |Welcome message to the user.  |
|POST            |```/new_user```                |Create a new user. Redirects to a confirmation page. |
|GET             |```/user_list```             	 |Show a list of all users created. | 

## Installation

1. Clone this repository
```
$   git clone "https://github.com/jcgonzalezb/user_registration_web_app.git"
```

2. Access the 'user_registration_web_app' directory:

```
$   cd user_registration_web_app
```

3. As a good practice, I suggest you create a virtual environment, e.g.

```
$   python3 -m venv myenv
```

4. Activate the new environment

```
$   source myenv/bin/activate
```

5. Install the requirements
```
$   pip install -r requirements.txt
```


6. Run the program

```
$   python3 app.py
```

Now you are running the web application and it is ready to create requests locally and test functionality, e.g.

```
 * Serving Flask app 'config' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 262-635-844
```

7. To test the web application, copy the IP address from your console, e.g. http://127.0.0.1:5000 and go to the Usage in this README file.

8. When you have done, terminate the app process with Ctrl+c and deactivate the venv.

```
$ deactivate
```
## Usage

When you start the web application and copy the IP address from your console, the home page is shown. There you will see a welcome message and to links to two different endpoints.

#### Example of use

1. Go to http://127.0.0.1:5000/. There you will see a welcome message and to links to two different endpoints. The first endpoint is create a new user (Crear nuevo usuario). The second one is list of users created (Lista de usuarios creados). For this particular example, we are creating a new user and then we are going to check the list of users created.

![Home page](documentation/images/home.png)

2. Make click on the create a new user (Crear nuevo usuario) link. A form will be shown and you can fill it with the name, email and city of the user. Once the form complete, make click on create user (Crear usario)buttom. If the information is correct, you will see a form confirming that the user was created successfully. From there you have to continue to the home page.

![new user](documentation/images/new_user.png)
![new user_2](documentation/images/new_user2.png)
![new user_3](documentation/images/new_user3.png)


If the form is not complete or the name or the email are already created, the web application will show you warnings and will let you know what should be done. You cannot proceed further until the form has been created correctly. If you do not want to continue, just click on the go to the home page (Ir a la pagina principal) link.

![error user](documentation/images/error_new_user.png)


3. The next step is checking the list of users, which in this case will be the user previously created. On the home page, make click on the list of users created (Lista de usuarios creados) link. The web application will show you the list of users created.

![list users](documentation/images/list_users.png)

If you want to go back to the home page, just click on the go to the home page (Ir a la pagina principal) link.


## Construction of this project






## Bugs

No known bugs at this time.


## Authors

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>

## License

Public Domain. No copy write protection.