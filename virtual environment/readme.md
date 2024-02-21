# Virtual Environments In Python

*Install the virtual environment package*
```cmd
pip install virtualenv
```

*To create a virtual environment*
```cmd
python -m venv <name of virtual environment>
```

*To activate*
```cmd
Set-ExecutionPolicy Unrestricted -Scope Process

.\<venv-name>\Scripts\activate
```

*To create a requirements.txt file*
```cmd
pip list > requirements.txt
```

*To install all the packages mentioned in a requirements.txt file*
```cmd
pip install -r requirements.txt
```

*To deactivate*
```cmd
deactivate
```