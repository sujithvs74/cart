CREATE DATABASE cart;

USE cart;

CREATE TABLE items(
   id INT NOT NULL,
   name VARCHAR(100) NOT NULL,
   price INT NOT NULL,
   PRIMARY KEY ( id )
);

USE mysql;

create user 'cart'@'%' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON cart.* TO 'cart'@'%';

FLUSH PRIVILEGES;