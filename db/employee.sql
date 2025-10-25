create table if not exists employees(
    id integer primary key autoincrement,
    first_name text,
    last_name text,
    salary integer,
    occupation text,
    phone_number text,
    username text unique ,
    password text,
    role text
);