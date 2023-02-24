# DjangoWebApp

**Overview:

A simple Django web app created in the style of a band fan club site.

Users can register as new users and log in.

Logged in users can take part in polls to vote where the band will play live next.**

This program was created as an exercise in working with Django, databases and HTML/CSS.

## Contents

* 1. Installation
* 2. Features
* 3. Usage

## 1. Installation

This project makes use of a Dockerfile to allow interested parties to run the web app.

The Dockerfile will execute the web app's various requirements, as seen in requirements.txt

These include the use of a virtual environment to allow the user to execute the web app.

For information on how to use Docker to deploy this web app, please refer to the following guide: 

https://www.devteam.space/blog/how-to-deploy-a-web-app-with-docker-containers/


## 2. Features

Once running, the web app will present the user with a web site in the style of a UK band's
fan website.

The website includes the following:
o Home page with general band information
o Media page with embedded tracks from the band
o Polls page to allow users to vote on the location of the band's next live performance
o User-auth page to facilitate login
o An admin portal to allow admins to manage users and create polls

The included HTML and CSS files render the web app in a manner fitting the band's trademark gritty aesthetic.

The user must be logged in (either as admin, or through registering a new user through the web app) to
use the poll aspect of the web app.

## 3. Usage

On first use, it is recommended to create and log in as the admin user.

**On creating an admin user: admins can be created through the use of the following command in the command 
window (and following the prompts thereafter):**

    $ python manage.py createsuperuser

Additional users can be registered through the 'register new user' link included at the bottom of all
pages, which makes use of the user-auth features of the web app.
