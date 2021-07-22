



## About The Project
Warbler is a simple clone of Twitter.

Deployed with Heroku: https://dylan-twitter-clone.herokuapp.com

* Python
* Flask
* HTML
* CSS
* Jinja2
* PostGresql
* SQLAlchemy



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps. Note that you will need `pip`, `ipython` and `postgresql` installed globally on your machine. 

### Installation

* Clone the repo
   ```sh
   git clone https://github.com/dferes/Warbler.git
   ```
* Set up Python virtual environment
  ```sh
  python -m venv env
  ```
* Initialize virtual environment
  ```sh
  source env/bin/activate
  ```
* Install packages/dependencies with pip
   ```sh
   pip install -r requirements.txt
   ```
* Set up environment variables
  ```sh
  export FLASK_ENV=production
  ```
* create database
  ```sh
  createdb warbler
  ```
* Open ipython (make sure you are in the root directory)
  ```sh
  ipython
  ```
* Seed the database 
  ```sh
  %run seed.py
  ```
* Start the server
   ```sh
   flask run
   ```
