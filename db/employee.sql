create table if not exists employees(
    employee_id integer primary key autoincrement,
    first_name text,
    last_name text,
    salary text,
    occupation text,
    phone_number integer,
    username text,
    password text
);
