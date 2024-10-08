# Django-Ecommerce-Store

.venv/Scripts/activate
pip install -r requirements.txt

# Access Django Admin :
django-admin startproject core .  
python manage.py startapp store 

# Migration :
python manage.py makemigrations

Migrations for 'store':
  store\migrations\0001_initial.py
    + Create model Category
    + Create model Product

python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, store
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  Applying store.0001_initial... OK

# Add New User :
python manage.py createsuperuser

# Run Server :
python manage.py runserver

# Run Tests :
python manage.py test

# Generate test report : 
coverage report 
coverage run --omit='*/.venv/*' manage.py test
coverage report 
coverage html 
