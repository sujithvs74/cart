# Demo - Basket

## How to build application

### Prerequisites
1. Mysql server
2. Docker-compose and docker installed instance

### Database configuration
1. Create mysql database with sql file in repo
```sh
mysql -u username -p < db.sql
```
2. Update `mysql_host` in config.yaml

### Build docker image
Execute docker-compose from root of the repo
```sh
docker-compose up -d
```
This will start application as docker and it will be accessible with http://<instance-ip>:5000

### How to add items to basket
Do a POST call to `http://<instance-ip>:5000/add_cart` with below json as input.
```sh
{
  "id": 123,
  "name": "testing1",
  "price": 11
}
```
Also set header `Content-Type` as `application/json`

### How to view items in basket
Do a GET call to `http://<instance-ip>:5000/view_cart`, it will return all items in basket.