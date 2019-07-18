
# microblog

## Requirements 
```
First you need to install: 
python3.6, python3.6-dev, virtualenv
```
 
## Setup virtual environment

###Creating virtual environment, after cloning:
```
- cd blog
- virtualenv -p $(which python3.6) env
- source env/bin/activate
- pip install -r requirements
```

## Database

### Setup PostgreSQL 

#### Install PostgreSQL
```
sudo apt install postgresql postgresql-contrib
```

#### Enter interactive session:
```
sudo -u postgres psql
```

#### Create user and database:
```
CREATE DATABASE blog;
CREATE USER python_dev WITH PASSWORD 'password';
```

#### Give the right of access to the data for user:
```
ALTER ROLE python_dev SET client_encoding TO 'utf8';
ALTER ROLE python_dev SET default_transaction_isolation TO 'read committed';
ALTER ROLE python_dev SET timezone TO 'UTC';
ALTER USER python_dev CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE blog TO python_dev;
```

##### To exit the postgres console:
```
\q
```
