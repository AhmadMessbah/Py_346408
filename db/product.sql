create table if not exists products(
    id integer primary key autoincrement,
    name text,
    brand text,
    model text,
    serial text,
    category text,
    unit text,
    expiration_date text
);