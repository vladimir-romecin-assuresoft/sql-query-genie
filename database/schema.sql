CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total REAL,
    created_at TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);