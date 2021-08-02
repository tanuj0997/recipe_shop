# Recipe APIs

## Tech Stack Used:

- Python (3.8)
- Django REST Framework
- SQLite3

## Execution Instructions

- Clone the repository
- Run `docker-compose up` in order to start the project in foreground, else add the `-d` flag to run it in daemon mode.
- Use the following [Postman](https://www.postman.com/downloads/) collection to execute the end-points as described in the spec:
  https://www.getpostman.com/collections/a587649fd729598ee52b

## Tests

In order to run the tests please follow the steps below:

- Run Docker in daemon as described in the previous section
- Run `docker exec -it recipe_shop_web_1 /bin/bash` in order to open the container running the project
- Run `python manage.py test` inside the container to run the tests

## Considerations

- It is assumed that the price always needs to be saved in cents and not converted to dollars for this task
- 2 tests (one unit test, one integration test) have been added to demonstrate the usual testing procedure followed
- All the operations have been done in a single container for the sake of the time limit. However, ideally the commands listed in `docker-compose.yml` are to be executed in separate containers
- A single cart is being used throughout the app since there was no mechanism to create a new cart. Hence there's a separate command to create a cart for the first time.
