SELECT name, city, rate
FROM customer, discount_code
WHERE customer.discount_code = discount_code.discount_code ;