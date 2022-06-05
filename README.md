# Space Runner

A platform for organising Maker, Hack, and other community spaces

## Getting started

We use Poetry to manage our dependencies.

Clone this repository, and then run `poetry install` to install everything you need.

Once all the dependencies are installed, `poetry run ./manage.py runserver` will start a local development server on http://localhost:8000 using a SQLite database.

Full instructions on how to deploy a production setup of this project can be found [in the documentation](https://space-runner.readthedocs.io).

# Quickstart for Heroku

1. Clone the repo
2. Ensure Heroku CLI is installed
3. Add the heroku remote to git with `heroku git remote -a <your app name>`
4. Set the variables in your Heroku console
5. Push the code to heroku using `git push heroku main`
