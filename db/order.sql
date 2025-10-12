create table if not exists orders (
    id integer primary key autoincrement ,
    order_type text,
    customer_id integer ,
    employee_id integer ,
    date_time text,
    payment_id integer,
    warehouse_transaction_id integer,
    tax integer,
    total_discount integer,
    total_amount integer
) ;
