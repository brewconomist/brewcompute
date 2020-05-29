# brewcompute
Brew-in-a-bag focused homebrew calculations. 

### INSTALLATION

Brewcompute is written for Python 3. 

Be careful to use the Python 3 version of virtualenv if you wish to edit, test and run the code. 

Once virtualenv is activated, install requirements with pip3. 

The following shows how: 

```
~$ git clone https://github.com/brewconomist/brewcompute.git
Cloning into 'brewcompute'...
remote: Enumerating objects: 33, done.
remote: Counting objects: 100% (33/33), done.
remote: Compressing objects: 100% (29/29), done.
remote: Total 33 (delta 13), reused 11 (delta 1), pack-reused 0
Unpacking objects: 100% (33/33), done.
~$ cd brewcompute
~/brewcompute$ python3 -m venv_osname
~/brewcompute$ . venv_osname/bin/activate
~/brewcompute$ which pip3
/home/ibowman/brewcompute/venv_osname/bin/pip3
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
