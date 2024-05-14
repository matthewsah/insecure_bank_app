CREATE TABLE IF NOT EXISTS Customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
);

CREATE TABLE IF NOT EXISTS Account (
		account_id INT AUTO_INCREMENT PRIMARY KEY,
		customer_id int,
		account_name VARCHAR(50) NOT NULL,
		balance INT,
		account_type VARCHAR(100) NOT NULL,
		CONSTRAINT FK_CustomerAccount FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);