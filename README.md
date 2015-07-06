# Boneyard Server Heroku App 


[![Build Status](https://travis-ci.org/jskulski/boneyard-server.svg)](https://travis-ci.org/jskulski/boneyard-server)


# Run Development Server

```
python Boneyard/FlaskApp.py
```

Visit localhost:5000

# Run Gunicorn Server (production)

(Gunicorn must be installed.)

```
gunicorn Boneyard.FlaskApp:app
```

# Run Test Suite

(Must install py.test)

```
$ py.test 

====================================== test session starts =======================================
platform linux2 -- Python 2.7.6 -- py-1.4.28 -- pytest-2.7.1
rootdir: /home/jskulski/Code/jskulski/boneyard-server, inifile: pytest.ini
collected 3 items

test/flask_acceptance_test.py ...

==================================== 3 passed in 0.13 seconds ====================================
```



