CREATE DATABASE IF NOT EXISTS bi_sales CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bi_sales;

CREATE TABLE IF NOT EXISTS dim_customer (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  region VARCHAR(60) NOT NULL,
  customer_segment VARCHAR(40),
  signup_date DATE
);

CREATE TABLE IF NOT EXISTS dim_product (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100) NOT NULL,
  category VARCHAR(60) NOT NULL,
  unit_price DECIMAL(12,2) NOT NULL,
  unit_cost DECIMAL(12,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales (
  sale_id INT PRIMARY KEY,
  sale_date DATE NOT NULL,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  region VARCHAR(60) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(12,2) NOT NULL,
  discount_rate DECIMAL(5,2) DEFAULT 0,
  revenue DECIMAL(14,2) NOT NULL,
  cost DECIMAL(14,2) NOT NULL,
  profit DECIMAL(14,2) NOT NULL,
  CONSTRAINT fk_sales_customer FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
  CONSTRAINT fk_sales_product FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
  INDEX idx_sales_date (sale_date),
  INDEX idx_sales_region (region)
);

CREATE TABLE IF NOT EXISTS fact_expense (
  expense_id INT PRIMARY KEY,
  expense_date DATE NOT NULL,
  region VARCHAR(60) NOT NULL,
  expense_type VARCHAR(60) NOT NULL,
  amount DECIMAL(14,2) NOT NULL,
  INDEX idx_expense_date (expense_date)
);

CREATE TABLE IF NOT EXISTS fact_target (
  target_year SMALLINT NOT NULL,
  target_month TINYINT NOT NULL,
  region VARCHAR(60) NOT NULL,
  sales_target DECIMAL(14,2) NOT NULL,
  PRIMARY KEY (target_year, target_month, region)
);
