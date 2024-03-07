# ego-challenge

## How to run the project

### 1. Dependencies

You need a Python environment with `Django 5.0.3` and `Django REST Framework 3.14` installed.
I use `pipenv`, a tool that manages this.

If you have `pipenv` installed (only available on Linux) navigate to the repository folder and run the next commands:

> \$ `pipenv update`\
> \$ `pipenv shell`

This will create the virtual environment with the dependencies installed.

If you don't want (or can't) to use `pipenv`, the `requirements.txt` file sould help you set up the project using another tool.

### 2. Running the server

Once you set up the dependencies, just run the command:

> \$ `python ./project/manage.py runserver`

Open your browser and go to http://localhost:8080/

## Info

```
localhost:8080/ ──┬── user/
                  │
                  └── api/
```

<div style="color: mediumspringgreen;">
<span style="font-size: 1.6rem;">
( ! ) About API<br>
</span>
API has the core functionality, but doesn't implement it's own authentication and authorization system (typically JWT).<br>
Instead, for this challenge I use my own implementation of the Django Users model, adapted from a previous project.<br>
This way the API has a working permissions system, but without implementing an API for the users.<br>
<span style="font-size: 1.6rem;">
( ! ) About Settings<br>
</span>
The settings used for this project are not optimized for a production environment, some password validators were removed, static and media content work locally, etc.
</div>

## My development environment

- Python Virtual Env.: `pipenv`
- Python Dependencies: `pipenv`
- Editor: `Visual Studio Code`
- O.S.: `Manjaro Linux (arch)`
