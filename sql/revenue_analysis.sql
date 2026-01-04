CREATE DATABASE revenue_analysis;
USE revenue_analysis;

CREATE TABLE sales (
  order_id INT,
  product VARCHAR(100),
  category VARCHAR(50),
  price DECIMAL(10,2),
  cost DECIMAL(10,2),
  discount DECIMAL(10,2),
  quantity INT,
  return_flag INT,
  region VARCHAR(50),
  order_date DATE
);

-- Sample analysis queries
SELECT SUM(price * quantity) AS total_revenue FROM sales;

SELECT SUM((price - cost - discount) * quantity) AS total_profit FROM sales;

SELECT product,
SUM((price - cost - discount) * quantity) AS profit
FROM sales
GROUP BY product
ORDER BY profit ASC;
