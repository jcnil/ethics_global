# API ETICS GLOBAL

## About The Project
Microservice allow encript and desencripted text 

### Built With
* Language: Python 3.9.18
* Framework: FastApi
* ODM: mongoengine 0.23.1

```
challenge_ethics_global/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── serializer.py
│   │       └── views.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── handlers.py
│   │   ├── helpers.py
│   │   ├── models.py
│   │   ├── process.py
│   │   └── querysets.py
│   │
│   └── meta/
│       ├── __init__.py
│       └── views.py
│
├── config/
│   ├── __init__.py
│   ├── db.py
│   └── urls.py
│
├── docker/
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── README.md
└── requirements.txt
└── .env.example
```

## Getting Started

This is an example of how you may follow instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
* [MongoDB Installation](https://docs.mongodb.com/manual/installation/)

Once you have MongoDB installed, and if you are going to run the project on local, please check that mongo
is running in your pc with the next command, or maybe you should validate if you have installed docker and mongo dockerized:

```sh
sudo systemctl status mongod
```

### Installation 

1. Install the virtual environment
```sh
$ python3 -p python3 venv
```
Activate the virtual environment with:
```sh
$ source venv/bin/activate
```
2. Install project requirements
```sh
$ pip3 install -r requirements.txt
```
Configuration
=============

## Set database config

Env vars of external service:

ENV VAR                 |   VALUES                                              |
---                     |   ---                                                 |
MONGO_URI               |   Mongo URI                                           |

## Set AWS config

Env vars of external service:

ENV VAR                 |   VALUES                                              |
---                     |   ---                                                 |
AWS_DEFAULT_REGION      | region of configure in you profile AWS e.g. us-west-2 |              
AWS_ACCESS_KEY_ID       | access key id of you AWS account                      |
AWS_SECRET_ACCESS_KEY   | secret access key in you AWS account                  |

### Execution

### uvicorn Server
```sh
$ uvicorn config:app --host=0.0.0.0 --port=5000 --reload --log-level=info
```

Develop
=======

## Run Flake8

```sh
flake8 --exclude venv/ --max-line-length 120
```

or 

```sh
python -m flake8 --exclude venv/ --max-line-length 120
```

### Run Test
Execute
```sh
coverage run -m pytest
```
See more in `htmlcov/index.html` with your browser

Contact
=======
* **José Nicolielly** - - [jcnil](https://github.com/jcnil/ethics_global)