CREATE DATABASE ecommerce;

USE ecommerce;


-- =====================================================
-- 1. CATEGORIES
-- =====================================================

CREATE TABLE categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    Description VARCHAR(255)
);


-- =====================================================
-- 2. CUSTOMERS
-- =====================================================

CREATE TABLE customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Email VARCHAR(150) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    ContactName VARCHAR(100),
    Address VARCHAR(255),
    City VARCHAR(100),
    PostalCode VARCHAR(20),
    Country VARCHAR(100)
);


-- =====================================================
-- 3. ADMINS
-- =====================================================

CREATE TABLE admins (
    AdminID INT AUTO_INCREMENT PRIMARY KEY,
    AdminName VARCHAR(100) NOT NULL,
    Email VARCHAR(150) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL
);


-- =====================================================
-- 4. PRODUCTS
-- =====================================================

CREATE TABLE products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(150) NOT NULL,

    CategoryID INT NOT NULL,

    Unit VARCHAR(100),
    Price DECIMAL(10,2) NOT NULL,
    Stock INT NOT NULL DEFAULT 0,

    CONSTRAINT fk_product_category
        FOREIGN KEY (CategoryID)
        REFERENCES categories(CategoryID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_product_price
        CHECK (Price >= 0),

    CONSTRAINT chk_product_stock
        CHECK (Stock >= 0)
);


-- =====================================================
-- 5. ORDERS
-- =====================================================

CREATE TABLE orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,

    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT CURRENT_TIMESTAMP,

    TotalAmount DECIMAL(10,2) NOT NULL DEFAULT 0.00,

    Status VARCHAR(30) NOT NULL DEFAULT 'PLACED',

    CONSTRAINT fk_order_customer
        FOREIGN KEY (CustomerID)
        REFERENCES customers(CustomerID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_order_total
        CHECK (TotalAmount >= 0)
);


-- =====================================================
-- 6. ORDER DETAILS
-- =====================================================

CREATE TABLE order_details (
    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,

    OrderID INT NOT NULL,
    ProductID INT NOT NULL,

    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_orderdetail_order
        FOREIGN KEY (OrderID)
        REFERENCES orders(OrderID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_orderdetail_product
        FOREIGN KEY (ProductID)
        REFERENCES products(ProductID)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT chk_orderdetail_quantity
        CHECK (Quantity > 0),

    CONSTRAINT chk_orderdetail_price
        CHECK (UnitPrice >= 0)
);