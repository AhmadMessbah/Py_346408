create table if not exists samples(
    id integer primary key autoincrement,
    name text,
    account text,
    balance integer,
    description text
);