# {{cookiecutter.app}}

## Setup development environment

We keep things simple.

Sqlite is used in development so no hassle. The only system dependencies are
python3, pip and virtualenv.

1. create and activate virtualenv, upgrade pip:

    ```
    virtualenv -p `which python3` ~/.virtualenvs/{{cookiecutter.app}}
    ~/.virtualenvs/{{cookiecutter.app}}/bin/activate
    pip install -U pip
    ```

2. install dependencies:

    ```
    make install
    ```

3. verify everything's OK:

    ```
    make test
    ```

4. run!

    ```
    make run
    ```

Help yourself with `make` and `./manage.py --help`.
