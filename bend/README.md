## Installation Instructions

1. Make sur docker engine and docker-compose are installed on your dev machine,
2. Clone the repository
3. CD into the project code
4. copy or move '.env.example' into '.env'
5. Generate a secret key and assign the value to 'SECRET_KEY' variable
6. Assign the relevant values to your database connections params and make sure you assign the value of 'db' to your 'DB_HOST' variable.
7. Run 'docker-compose build'
8. Run 'docker-compose up -d'
9. Run 'docker-compose exec polling python3 manage.py migrate'
10. Run 'docker-compose exec polling python3 manage.py createsuperuser'


## Other development instruction
