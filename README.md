# Sri Challenge

## Assignment
The goal of this exercise is to retrieve timestamp and temperature from an API weather station information
and insert it into a PostgreSql database everytime you run certain script


## How to run the project
* Create a virtualenv: `python -m venv virtualenv` and activate it `. virtualenv/bin/activate`
* Install dependencies: `pip install -r requirements.txt`
* Config config.py based on your PostgreSql database
* run in a command line: 'python table_creation.py'
* to get yesterday data and insert it: 'python yesterday_info.py'
* to get custom date data and insert it: 'python custom_info.py' and insert both start and end datetime
* to get all current records in the database, run: 'python get_records.py'
