create table if not exists customers(
    id integer primary key autoincrement,
    first_name text,
    last_name text,
    phone integer,
    address text
);