# automate_the_boring_web
Web automation using selenium with python.
```
Steps:
-------------------------------------------------------------------------------
1. lets make a new directory somewhere in your computer. You know, just to make 
things clean. Run:

$ mkdir web_automation && cd web_automation

2. Assure you have python3, pip and venv. There is tons of resource to install 
those. Go get your tigers

3. now run this command bellow to make a virtualenv for your project.

$ python3 -m venv web_automation_env1

4. Activate your venv

$ . web_automation_env1/bin/activate

5. Lets get into our venv 
 
$ cd web_automation_env1

6. Install all dependencies from our requirements.txt file

$ pip3 install -r requirements.txt

7. create credentials.py and these 2 variables as we need to automate login in
our targeted web application

user_email: str = 'your email'
user_password: str = 'your password'

8. Now lets run our app using this command

python3 run.py

```


```
Project Tree
-------------------------------------------------------------------------------
.
├── credentials.py
├── login
│   ├── __init__.py
│   └── login.py
├── main
│   ├── app.py
│   ├── __init__.py
│   ├── urls.py
│   └── web_driver.py
├── order
│   ├── __init__.py
│   └── order.py
├── README.md
├── requirments.txt
└── run.py

-------------------------------------------------------------------------------
```
```
Features:
1. Login
```