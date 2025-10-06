-- Seed data for e-commerce analytics
INSERT INTO customers (name, email) VALUES
('Alice Smith', 'alice@example.com'),
('Bob Jones', 'bob@example.com'),
('Carol Lee', 'carol@example.com'),
('David Kim', 'david@example.com'),
('Eva Brown', 'eva@example.com');

INSERT INTO orders (customer_id, status, currency, payment_method) VALUES
(1, 'PLACED', 'USD', 'card'),
(2, 'PAID', 'USD', 'paypal'),
(3, 'SHIPPED', 'USD', 'card'),
(4, 'PLACED', 'USD', 'card'),
(5, 'PAID', 'USD', 'paypal'),
(1, 'SHIPPED', 'USD', 'card'),
(2, 'PLACED', 'USD', 'card'),
(3, 'PAID', 'USD', 'paypal'),
(4, 'SHIPPED', 'USD', 'card'),
(5, 'PLACED', 'USD', 'card');

INSERT INTO order_items (order_id, sku, qty, unit_price) VALUES
(1, 'SKU1', 2, 10.0),
(1, 'SKU2', 1, 20.0),
(2, 'SKU1', 1, 10.0),
(2, 'SKU3', 3, 5.0),
(3, 'SKU2', 2, 20.0),
(3, 'SKU4', 1, 15.0),
(4, 'SKU1', 1, 10.0),
(4, 'SKU5', 2, 8.0),
(5, 'SKU3', 2, 5.0),
(5, 'SKU2', 1, 20.0),
(6, 'SKU4', 2, 15.0),
(6, 'SKU5', 1, 8.0),
(7, 'SKU1', 1, 10.0),
(7, 'SKU2', 2, 20.0),
(8, 'SKU3', 1, 5.0),
(8, 'SKU4', 2, 15.0),
(9, 'SKU5', 1, 8.0),
(9, 'SKU2', 1, 20.0),
(10, 'SKU1', 2, 10.0),
(10, 'SKU3', 1, 5.0);
