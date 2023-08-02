# demo_pref
Very first demo for Pref with Python3.9, Django4 and SQLite

1. python3.9 or 3.7^
2. source venv/bin/activate  # if python interpreter in a virtual environment
3. pip install -r requirements.txt  # install all requirement lib
4. python manage.py makemigrations   # create migrate file 
5. python manage.py migrate  # migrate 
6. python manage.py runserver

==> Look up http://localhost:8000 by default
<img width="1270" alt="Screenshot 2023-08-03 at 01 01 18" src="https://github.com/luckyjd/demo_pref/assets/21038766/6f0ee3bb-5474-434c-b99f-f3dab5a92bba">

# DB design
<img width="803" alt="Screenshot 2023-08-02 at 23 12 23" src="https://github.com/luckyjd/demo_pref/assets/21038766/c7085463-2037-43cd-973e-34a683bd50de">

# Create test data 
- Create User: http://localhost:8000/api/user/
- Create Post: http://localhost:8000/api/post/
- Create Comment: http://localhost:8000/api/comment/

