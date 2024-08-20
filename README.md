## PageRank Visualization
This project is a visualization of the PageRank algorithm. The PageRank algorithm is a link analysis algorithm used by Google Search to rank websites in their search engine results. The PageRank algorithm works by counting the number and quality of links to a page to determine a rough estimate of the website's importance. The underlying assumption is that more important websites are likely to receive more links from other websites.

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

#### Technologies used
- React
 - Material-UI
 - vis-network
- Django
 - Django REST framework
- Docker

#### Tests
To run the tests, you can run the following command:
```bash
make test  # this runs docker-compose exec server ./manage.py test
```