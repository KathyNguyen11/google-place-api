## Technologies used

* **[Python3](https://www.python.org/downloads/)**: Refer version < 3.9
* **[Flask](flask.pocoo.org/)**
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)**
* **[Marshmallow](https://marshmallow.readthedocs.io/en/stable/index.html)** : Used for schema validation
* Minor dependencies can be found in the requirements.txt file on the root folder.

## Installation / Usage

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can
  get python3 [here](https://www.python.org). You can use pyenv to install specific version [link](https://github.com/pyenv/pyenv#installation)
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Then Git clone this repo to your local machine


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd google-place-api
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```

* #### Install your requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```

* #### Running It
  On your terminal, run the server using this one simple command:
    ```
    (venv)$ flask run
    ```
  You can test get phone number by using Postman via this URL:
    ```
    http://localhost:5000/getphonenumber/?address={input_address}
    ```
  You can run all unit test with this command:
    ```
    pytest
    ```
  If you want to run specific test case in one file use this command:
    ```
  pytest tests/test_get_phone_number.py -k test_get_formatted_phone_number_successfully
    ```