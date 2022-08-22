# Hackerrank
This repo contain practice question from Hackerrank.


# SetUp

1. Check that the correct python version is showing up by opening python interpreter.
   ```bash
   python --version
   ```
   Try closing and reopening the terminal if it doesn't work the first time.
2. Setup up virtual environment and activate it.
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install pip-tools.
   ```bash
   pip install pip-tools
   ```
4. Install dependencies
   ```bash
    pip-sync requirements.txt
   ```

## To install new package

We will be using pip-tools for dependency management. This will help us to know how a specific package was installed in our venv. Do not run `pip install <package_name>` or `pip install -r requirements.txt` to install the packages. Please follow the steps to install and sync packages.

1. Add package name to `requirements.in`
2. Run `pip-compile requirements.in`. This will create two new files `requirements.txt`
3. Run `pip-sync requirements.txt` to install the updated packages in the requirements file.

