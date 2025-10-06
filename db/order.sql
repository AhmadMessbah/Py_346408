create table if not exists orders (
    id integer primary key autoincrement ,
    customer text ,
    employee text ,
    order_item_list text ,
    order_status text,
    payment_method text,
    payment_status text,
    datetime text
) ;
