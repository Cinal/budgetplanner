# BudgetPlanner

Stack:
- Python 3.12
- Django 4s
- PostgreSQL

## Requirements
- Docker
- docker-compose
- make

## How to run project
Run:
make build
make up

Check url:
 http://localhost:8080/


How check other commands:

```
 make help

Commands:
  make 
  build            Build project.
  up               Run project.
  down             Stop project.
  restart          Restart.
  clean            Cleanup.
  django           Django shell
  migrate          Run migrations on db
  collectstatic    create django statics fiels
  cacheclear       Django cache clear
  shell            Shell
  db-shell         Psql client
  init             Setup initial project data
  ```

<img src="https://github.com/Cinal/budgetplanner/blob/master/docs/makefile.png"/>
<img src="https://github.com/Cinal/budgetplanner/blob/master/docs/make_tests.png"/>
<img src="https://github.com/Cinal/budgetplanner/blob/master/docs/insomnia.png"/>


DONE:
- docker & docker-compose
- makefile scripts
- run unit tests
- pagination
- auth
- Insomnia API collectiondo


## Family budget - coding task description

### Description
The application should allow for creating several users. Each user can create a list of any
number of budgets and share it with any number of users. The budget consists of income
and expenses. They are grouped into categories. It is required to create a REST or
GraphQL API and a database. The project should contain authorisation, tests, fixtures,
filtering and pagination.

### Technologies
Any. Whatever would be best in your opinion (including JS frameworks).

### Requirements
Entire project should be available as an open source project on GitHub. Please commit
your work on a regular basis (rather than one huge commit). The project should contain a
README file with information on how to install the application in a local environment.

### Deploy
Please use Docker for orchestration (docker-compose).