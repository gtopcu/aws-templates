-- Product Table
-- id, name, price, description, category
CREATE TABLE IF NOT EXISTS product (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  description TEXT,
  category VARCHAR(255)

 -- Sales Table
 -- id, product_id, quantity, price, date
CREATE TABLE IF NOT EXISTS sales (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  date DATETIME NOT NULL 

-- SQL query product table to find products for each category
SELECT * FROM product WHERE category = 'category_name';

-- SQL query product table to find the number of products for each category
SELECT category, COUNT(*) FROM product GROUP BY category;

-- SQL join to get the total sales for each product
SELECT p.name, SUM(s.quantity) AS total_sales
FROM product p
JOIN sales s ON p.id = s.product_id
GROUP BY p.name;
