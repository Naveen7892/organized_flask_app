@echo off

set SECRET_KEY=organized_flask_app_secret
set DATABASE_URI=sqlite:///organized_flask_app.db

set FLASK_APP=app:create_app
set FLASK_ENV=development

cmd /k ".venv\Scripts\activate"