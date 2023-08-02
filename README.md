# demo_pref
Very first demo for Pref with Python3.9, Django4 and SQLite

1. python3.9 or 3.7^
2. source venv/bin/activate  # if python interpreter in a virtual environment
3. pip install -r requirements.txt  # install all requirement lib
4. python manage.py makemigrations   # create migrate file 
5. python manage.py migrate  # migrate 
6. python manage.py runserver

==> Look up http://localhost:8000 by default


# DB design
![Screenshot 2023-08-02 at 23.10.34.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fls%2Fc4c871t51dvdb5cwwvpvwn840000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_q9HTMn%2FScreenshot%202023-08-02%20at%2023.10.34.png)

# Create test data 
- Create User: http://localhost:8000/api/user/
- Create Post: http://localhost:8000/api/post/
- Create Comment: http://localhost:8000/api/comment/
