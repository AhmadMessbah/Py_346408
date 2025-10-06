create table if not exists customers(
    customer_id integer primary key autoincrement,
    first_name text,
    last_name text,
    phone integer,
    address text
);
