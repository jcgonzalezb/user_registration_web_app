# User registration web application
> This project is an HTTP server REST API implementation


## Objectives

- Creating a user registration service that receives a name, email and city. 
- Allowing check the list of users created by the registration service. 

## Table of content

* [Architecture](#architecture)
	* [Technology Stack](#technology-stack)
	* [Database Diagram Model](#database-diagram-model)
* [Environment](#environment)
	* [File Descriptions](#file-descriptions)
	* [API Endpoints](#api-endpoints)
* [Installation](#installation)
* [Usage](#usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

##  Architecture
###  Technology Stack
![Web infrastructure stack image](documentation/images/Technology%20stack.jpg)

###  Database Diagram Model

![Log trading log ERR Diagram](documentation/images/DB_stock_log_V3.png)

##  Environment
This project was developed on Ubuntu 20.04 LTS using python 3.8.10 with flask framework, connecting to a MySQL Database.

### File Descriptions

- ```app.py```  contains the entry point of the API.
- ```config.py```  contains the configuration settings for the API.
- ```users.db```  contains the database configured for this project (data not included).
- ```models/``` contains classes used for this project.
- ```routes/``` contains endpoints implemented for the API.
- ```routes/home_blueprint.py``` show welcome message for the user and links to create users and to show a list of users.
- ```routes/new_user_blueprint.py``` implemented routes to create users.
- ```routes/user_list_blueprint.py``` implemented routes to check the list of users created.
- ```templates/``` contains html files used to show users and trades.
- ```forms/``` contains forms used fot this project.
- ```forms/form.py``` implements a form to create new users.
- ```documentation/``` contains files used for document endpoints of the API.
- ```documentation/collections``` directory contains files used for use the API.
- ```documentation/images``` contains images used in the readme.md file.


### API Endpoints

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

Now you are running the API and it is ready to create requests locally and test functionality, e.g.

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

7. To test the API, copy the IP address from your console, e.g. http://127.0.0.1:5000 and go to the Usage in this README file.

8. When you have done, terminate the app process with Ctrl+c and deactivate the venv.

```
$ deactivate
```
## Usage

Load the postman collection in the [collections](documentation/collections) folder into your postman account to test each endpoint. 

#### Example of use

This example shows how to update the name of a user.
1. Go to http://127.0.0.1:5000/login/, set in the authorization section the username (email) and password assigned to a user. Then, set the HTTP method to POST and make click on the send buttom. The server will return an access token you'll need to try the endpoints. At the end, make copy of the access token.

![Postman Login](documentation/images/update_user_1.png)

2. Go to http://127.0.0.1:5000/users/update, set in the authorization section the username (email) and password assigned to the same user, click on Headers to insert the token previouesly created and click on Body to insert the JSON body with the new name of the user. The app would not be allowed to update more user information other than the name.

3. SET the HTTP method to PATCH and and make click on the send buttom. The app will show the following mssage: "The user has been updated!". The user name has been updated successfully. To confirm the update, go to http://127.0.0.1:5000/users/profile.

![Postman Update](documentation/images/update_user_2.png)

![Postman Profile](documentation/images/update_user_3.png)


## Bugs

No known bugs at this time.


## Authors

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>

## License

Public Domain. No copy write protection.