CREATE TABLE products(
  id INTEGER NOT NULL PRIMARY KEY,
  title VARCHAR(255),
  descr VARCHAR(2000),
  product_image VARCHAR(500),
  price FLOAT,
  likes INTEGER
);

INSERT INTO products(title, descr, product_image, price, likes) VALUES
('Product 1', 'This is a description of the first product.', 'Item-1.PNG', 1.00, 53),
('Product 2', 'This is a description of the second product.', 'Item-2.PNG', 2.00, 71),
('Product 3', 'This is a description of the third product.', 'Item-3.PNG', 3.00, 190),
('Product 4', 'This is a description of the fourth product.', 'Item-4.PNG', 4.00, 310),
('Product 5', 'This is a description of the fifth product.', 'Item-5.PNG', 8.00, 1530),
('Product 6', 'This is a description of the sixth product.', 'Item-6.PNG', 2.00, 10),
('Product 7', 'This is a description of the seventh product.', 'Item-7.PNG', 3.00, 105),
('Product 8', 'This is a description of the eighth product.', 'Item-8.PNG', 6.00, 5610),
('Product 9', 'This is a description of the ninth product.', 'Item-9.PNG', 1.00, 1099),
('Product 10', 'This is a description of the tenth product.', 'Item-10.PNG', 1.00, 100);

CREATE TABLE totalusers(
  id INTEGER NOT NULL PRIMARY KEY,
  user VARCHAR(255)
);

CREATE TABLE actions(
  actid INTEGER NOT NULL PRIMARY KEY,
  id INTEGER,
  user VARCHAR(255),
  FOREIGN KEY (user) REFERENCES totalusers(user),
  FOREIGN KEY (id) REFERENCES products(id)
);



-- sqlite3 productsdb.sqlite ".read schema.sql"