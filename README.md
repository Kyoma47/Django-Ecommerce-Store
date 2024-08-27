# Django-Ecommerce-Store

.venv/Scripts/activate
pip install -r requirements.txt

# Access Django Admin :
django-admin startproject core .  
python manage.py startapp store 
python manage.py makemigrations

Migrations for 'store':
  store\migrations\0001_initial.py
    + Create model Category
    + Create model Product