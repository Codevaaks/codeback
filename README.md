# codeback
Codevaak's code back.

## Setup
### dotenv
There's a dotenv here. You'll need to set it up with the following values:
```
DJANGO_SECRET_KEY='REPLACE'
DEBUG_MODE=boolean
DB_PASS=String
```
Alternatively, if you are part of the Codevaaks team, go ahead and just use the private `.env` that's stored in a repository.

### Prerequisties
  - Install `python3` and `pipenv`.
  - If you're running this locally, you'll need PostgreSQL installed. Go ahead and install that. 
  Next, you'll need make a database and a user. The database should be called `cv-db`, and this user should be called `cvuser`, with the password that you specified in your `.env`.
### Running
  1. Run `pipenv install`. This should install all of the prerequisite packages for you.
  2. Run `pipenv run`. This executes a script that you can find in `Pipfile`.
## Note
* Make sure you're installing new packages and files using `pipenv install` and NOT `pip`.
* Make sure you're running off of pipenv. If your pipenv for some odd reason happens to have `python-dotenv` installed, make sure you uninstall it!