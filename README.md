# Learning Logs
Learning Log helps you keep track of your learning, for any topic you're learning about. This application is based on a project from "Python Crash Course" by Eric Matthes.
## Prerequisites and installation
Requires Python to be installed. Tested on Python versions 3.8.10 and 3.9. Other version might work as well.  
Clone repository to your computer and change directory to *learnin_logs*:  
```
git clone https://github.com/Na-na13/learning_logs  
cd learning_logs
```
Create the virtual environment and activate it:
```
python3 -m venv ll_env
source ll_env/bin/activate
```
Install required dependencies. Upgrading pip first is recommended:  
```
pip install --upgrade pip
pip install -r requirements.txt
```  
Apply migrations to set up the database:  
```
python3 manage.py migrate
```
Run the development server:
```
python3 manage.py runserver
```
The application is accessible at http://127.0.0.1:8000/. The default port for the application is 8000.
