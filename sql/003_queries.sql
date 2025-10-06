-- Analytical queries for e-commerce analytics
-- a) Daily GMV (gross merchandise value)
SELECT DATE(o.created_at) AS day, SUM(oi.qty * oi.unit_price) AS daily_gmv
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY day
ORDER BY day DESC;

-- b) Top 5 SKUs by revenue
SELECT sku, SUM(qty * unit_price) AS revenue
FROM order_items
GROUP BY sku
ORDER BY revenue DESC
LIMIT 5;

-- c) Conversion funnel (PLACED → PAID → SHIPPED)
SELECT status, COUNT(*) AS count
FROM orders
WHERE status IN ('PLACED', 'PAID', 'SHIPPED')
GROUP BY status;

-- d) Refund rate per payment method
SELECT payment_method, 
       SUM(CASE WHEN status = 'REFUNDED' THEN 1 ELSE 0 END) * 1.0 / COUNT(*) AS refund_rate
FROM orders
GROUP BY payment_method;
