***************
Django Workshop
***************

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

Repository containing materials for the workshop given from Friday, may 8th 2020 to Sunday, may 10th 2020.
The purpose of this workshop is to give an introduction to Django development.
We'll be using best practices from the Django and more generally Python communities.

We will cover areas such as:

* User Registration via django-allauth
* DjangoRestFramework: A powerful tool to build Web APIs
* GeoDjango: A framework for storing and working with geographic data
* Running tests with pytest
* Deployment to Heroku


Workshop Requirements:
######################

* Install Python version >= 3.8
* Install Cookiecutter
* Install Docker
* Having a postGIS docker container running on the machine

Getting Python >=3.8 on your machine:
*************************************

You can get Python from the official website.

https://www.python.org/downloads/

For those under Mac OS trying to install Python with the "Brew" package manager:

To this day, if you run the command::

$ brew install python

you would get a Python version prior to 3.8.

How to proceed with "brew"::

$ brew install python@3.8

Then::

$ brew info python@3.8

Expected output::

 python@3.8 is keg-only, which means it was not symlinked into /usr/local,
 because this is an alternate version of another formula.
 If you need to have python@3.8 first in your PATH run::
 $ echo 'export PATH="/usr/local/opt/python@3.8/bin:$PATH"' >> ~/.bash_profile

Copy/Past the above command in you shell to add Python 3.8 to your path.

Check that Python and Pip (Python package manager) are installed right.

Go to your shell and try the following commands::

$ python3 --version
$ Expected output : Python 3.8.2

Run::

$ pip3 --version
$ pip 20.0.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)

Getting cookiecutter:
*********************

Cookiecutter is a command-line utility that creates projects from cookiecutters project templates.

Install it with the following command::

$ Pip3 install "cookiecutter>=1.7.0"

Official documentation: https://cookiecutter.readthedocs.io/en/1.7.2/

Installing Docker:
******************

Preferred installation way: Get Docker from the official website.

https://docs.docker.com/get-docker/

For those under Mac OS trying to install docker with the "Brew" package manager:

See https://www.robinwieruch.de/docker-macos

Running the PostGIS container:
******************************

PostGIS provides spatial objects for the PostgreSQL database, allowing storage and query of information about location and mapping.

You can install PostgreSQL on your machine, create a database, and install the PostGIS extension.

The preferred way for this workshop is to create a database with Docker and the kartoza postgis image that you can get from Docker Hub.

Official documentation at: https://hub.docker.com/r/kartoza/postgis

The container will have PostgreSQL and PostGIS already installed and configured.

You’ll get a PostgreSQL server listening on the 5432 port.

Run the command::

$ docker run --name=postgiscontainer -d -e POSTGRES_USER=fred -e POSTGRES_PASS=1234 -e POSTGRES_DBNAME=pgis -p 5432:5432 kartoza/postgis:11.0-2.5

To check if the container is running and listening on 5432->5432/tcp::

$ docker ps


Project Setup:
###################

Create a working directory::

$ mkdir python_projects

Then::

$ cd python_projects

Next step: Download cookiecutter-django project template boilerplate::

$ cookiecutter https://github.com/pydanny/cookiecutter-django

You will be asked by the installation script to enter some values.
Just press 'enter' when you want to accept the default values.

  .. code-block:: RST

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 550, done.
    remote: Compressing objects: 100% (310/310), done.
    remote: Total 550 (delta 283), reused 479 (delta 222)
    Receiving objects: 100% (550/550), 127.66 KiB | 58 KiB/s, done.
    Resolving deltas: 100% (283/283), done.
    project_name [Project Name]: Django Workshop
    project_slug [django_workshop]:
    description [Behold My Awesome Project!]: An awesome Django workshop!
    author_name [Daniel Roy Greenfeld]: Frédéric Darré
    domain_name [example.com]:
    email [you@example.com]: fdarre@exemple.com
    version [0.1.0]: 0.0.1
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - GPLv3
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]:
    timezone [UTC]:
    windows [n]:
    use_pycharm [n]:
    use_docker [n]:
    Select postgresql_version:
    1 - 11.3
    2 - 10.8
    3 - 9.6
    4 - 9.5
    5 - 9.4
    Choose from 1, 2, 3, 4, 5 [1]:
    Select js_task_runner:
    1 - None
    2 - Gulp
    Choose from 1, 2 [1]:
    Select cloud_provider:
    1 - AWS
    2 - GCP
    3 - None
    Choose from 1, 2, 3 [1]: 3
    Select mail_service:
    1 - Mailgun
    2 - Amazon SES
    3 - Mailjet
    4 - Mandrill
    5 - Postmark
    6 - Sendgrid
    7 - SendinBlue
    8 - SparkPost
    9 - Other SMTP
    Choose from 1, 2, 3, 4, 5, 6, 7, 8, 9 [1]:
    use_async [n]:
    use_drf [n]: y
    custom_bootstrap_compilation [n]:
    use_compressor [n]:
    use_celery [n]:
    use_mailhog [n]:
    use_sentry [n]:
    use_whitenoise [n]: y
    use_heroku [n]: y
    Select ci_tool:
    1 - None
    2 - Travis
    3 - Gitlab
    Choose from 1, 2, 3 [1]:
    keep_local_envs_in_vcs [y]:
    debug[n]:

For clarity, rename the generated folder::

/python_projects/django_workshop

to::

/python_projects/django_workshop_repository

Open the django_workshop_repository/ folder and create a virtualenv:

The venv directory should be located outside of your project folder::

$ python3.8 -m venv /path/to/venv/

You can now open the newly generated project in your favorite IDE :

Activate the virtualenv you have just created::

$ source /path/to/venv/bin/activate

Enter the database credentials in the settings/base.py

From:

.. code-block:: JSON

    DATABASES = {
        "default": env.db("DATABASE_URL", default="postgres:///django_tutorial")
    }

To:

.. code-block:: JSON

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'pgis',
            'USER': 'fred',
            'PASSWORD': '1234',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

Next step, install the project dependencies for local devlopment::

$ pip3 install -r requirements/local.txt

Run the migrations::

$ python3 manage.py migrate

If you get an error message:

Make sure that your docker container is running, listening to the right port and
that your database credentials are corrects.


Django application documentation:
#################################

Settings
********

See settings_ documentation.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
**************

Setting Up Your Users

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
***********

Running type checks with mypy::

  $ mypy django_tutorial

Test coverage
*************

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html


Running tests with py.test::

  $ pytest

Live reloading and Sass CSS compilation
***************************************

See `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Deployment
**********

The following details how to deploy this application.

Heroku
******

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html





