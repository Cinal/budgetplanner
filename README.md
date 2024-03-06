# budgetplanner


TODO:
- auth
- paggintation
- unit tests
- integration tests


Stack:
- Python 3.12
- Django 5
- PostgreSQL

## Requirements

- Docker
- docker-compose
- make

## Installation

Clone the repository:

Run:
make help

make build
make up
make restart

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
Wykorzystanie poetry i skonfigurowanie
testy moga pownny byc odpalany w odzielnym obrazie, nie implementowalem tego.
- info o dokumetacji - open api
- data migracji update zrobic
info its run pn http://localhost:8080/



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
