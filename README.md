## PageRank Visualization
This project is a visualization of the PageRank algorithm. The PageRank algorithm is a link analysis algorithm used by Google Search to rank websites in their search engine results. The PageRank algorithm works by counting the number and quality of links to a page to determine a rough estimate of the website's importance. The underlying assumption is that more important websites are likely to receive more links from other websites.

## Design Documentation
#### Overview
This project implements a basic PageRank algorithm using Django. Below are the key design decisions, resulting tradeoffs, and limitations of the implementation.

#### Design Decisions
###### Migration to Pure Pythonic PageRank Algorithm:
1. The pagerank algorithm does not gel well with Django's ORM as it requires a lot of computation and Django's ORM is not optimized for massive IO operations.
2. Hence the core algorithm was moved to a simpler framework-agnostic Pythonic implementation.
2. This change significantly reduced the computation time from 6 seconds to under 50 milliseconds for a graph with around 10 nodes and various edges.

Tradeoff: While the pure Pythonic approach is faster, it may require more careful management of dependencies and environment configurations.

###### Use of Docker:
Utilized Docker for development and deployment as it ensures consistent environments across different platforms, making development and deployment more reliable.
Tradeoff: Docker adds an additional layer of complexity and requires familiarity with containerization concepts.

###### Backend Database - PostgreSQL:
PostgreSQL is robust and scalable, making it suitable for handling large datasets and complex queries.
Tradeoff: PostgreSQL may require more resources and setup compared to simpler databases like SQLite.

###### Framework Choice - Django:

Decision: Selected Django as the web framework.
Reason: Familiarity with Django allowed for faster development and leveraging its built-in features.
Tradeoff: Django might be overkill for simpler applications and could introduce unnecessary overhead.

#### Limitations
###### Scalability: 
While PostgreSQL and Docker provide a scalable foundation, the current implementation may need further optimization for extremely large datasets or high-traffic scenarios.

###### Testing
1. The current implementation adds some tests that are framework-agnostic such as those for the Pagerank algorithm 
2. But there are tests that require Django to run. The model tests can get very cumbersome to run when the codebase grows and ideally a library such as `pytest_django` should be used to run model-based tests

###### Complexity 
The use of Docker and PostgreSQL adds complexity to the setup and deployment process, which might be challenging for developers unfamiliar with these technologies.

###### Algorithm Flexibility
The pure Pythonic implementation of the PageRank algorithm is efficient but may require additional work to integrate with other systems or frameworks.

#### Running the application
To run the application, you need to have Docker installed on your machine. If you don't have Docker installed, you can download it from [here](https://www.docker.com/products/docker-desktop).

Once you have Docker installed, you can run the following command to start the application:
```bash
make build  # this runs docker-compose build
```
```bash
make run  # this runs docker-compose up
```
```bash
make migrate  # this runs docker-compose exec server python ./manage.py migrate
```

After running the above commands, you can access the application by visiting [http://localhost:3000](http://localhost:3000) in your browser.

#### Tests
To run the tests, you can run the following command:
```bash
make test  # this runs docker-compose exec server ./manage.py test
```
#### Technologies used
- React
    - Material-UI
    - vis-network
- Django
    - Django REST framework
- Docker

