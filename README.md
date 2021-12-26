# To start the server
````
uvicorn app.main:app
````
# below  cmd if  ot want to restart the server after every change
````
uvicorn app.main:app --reload
````
````
uvicorn app.mainORM:app --reload
````

# making connection with database postgress without ORM
https://www.psycopg.org/docs/

# with ORM i.e. sqlalchemy
````
pip install sqlalchemy
````

# for hashing of password
````
pip install passlib[bcrypt]
````

# for authhentication
````
pip install python-jose[cryptography]
````

# to over come the weekness of sqlalchemy(can not add the column), we use alambic
````
pip install alembic
````
# to create a folder alembic
````
alembic init alembic
````
# after this we need to import base from database to alembic env file
# and in .ini file update sqlalchemyurl path
````
alembic revision -m "create post table"
````

````
alembic upgrade revision_number
````

````
alembic downgrade revision_number
````

# CORS(cross origin resource sharing) allows to make requests from a web browser on one domain to a server on diff domain
# by default our APi will only allow web browser running on same domainas our server to make request to it.

# to include all the already downloaded packages in requirements.txt
````
pip freeze > requirements.txt
````
# after that if anyone wants to install all packages, just run requirements.txt
````
pip install -r requirements.txt
````

# to push the change
````
git add --all
````
````
git commit -m "added procfile"
````
````
git push origin main
````
````
git push heroku main
````
# if anything in alembic database file
````
heroku run alembic upgrade head
````

# loading application on ubuntu 
````
sudo apt update && sudo apt upgrade -y
````
````
sudo apt install python
````
````
sudo apt install python3-pip
````
````
sudo pip3 install virtualenv
````
# install postgres on ubuntu virtual machine
````
sudo apt install postgresql postgresql-contrib -y
````
# local - authentication - connecting ubuntu with postgres
# postgres has created a local user on ubuntu vm i.e. postgres. so first change the user from root to postgres
````
su - postgres
````
# now can login to database, here username = ppstgres
````
psql -U <provide username>
````
# now provide password to the user
````
\password postgres
````
# enter the password
# now if exit from postgres login 
````
\q
````
# to roor user
````
exit
````
# now move to installed packages folder
````
cd /etc/postgresql/<provide version of postgres>/main
````
# now open postgresql.conf file
````
sudo vi postgresql.conf
````
# go to connection and authentication in file and under connection settings write below one
# listen_address = '*'
# * if you want to connect from any machine or the ip address of specific
# now go to other file
````
sudo vi pg_hba.conf
````
# under heading database administrative change peer to md5
# under local if for unix change peer to md5
# under IPv4 change address to 0.0.0.0/0
# under IPv6 change address to ::/0, now save and exit file
# reastart 
````
systemctl restart postgresql
````
# create the new user other than root(security issue)
````
adduser vikas
````
# it will ask for password, provide password(new)
````
su - vikas
````
 