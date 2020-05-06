# brewcompute
Brew-in-a-bag focused homebrew equations. 

### DEV INSTALL

This code is written for Python 3. 

Be careful to use the Python 3 version of virtualenv if you wish to edit, test and run the code. 

Once virtualenv is activated, install requirements with pip3. 

The following shows how: 

```
~/brewcompute$ python3 -m venv venv_popos
~/brewcompute$ . venv_popos/bin/activate
~/brewcompute$ which pip3
/home/ibowman/brewcompute/venv_popos/bin/pip3
~/brewcompute$ pip3 install -r requirements.txt
Collecting flake8 (from -r requirements.txt (line 1))
...
```

### TESTING 

With the virtual environment active, all tests can be run with `bash run_tests.sh`: 

```
~/brewcompute$ bash run_tests.sh
CHECKING SYNTAX
OK

RUNNING UNIT TESTS with python -m unittest discover src/
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
