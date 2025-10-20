create table if not exists employees(
    id integer primary key autoincrement,
    first_name text,
    last_name text,
    salary integer,
    occupation text,
    phone_number text,
    username text,
    password text,
    role text
);