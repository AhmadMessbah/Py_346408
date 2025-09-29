

house_list = [
    {"address":"tehran", "area":200, "price": 1800, "accommodation":"elevator, parking, kitchen"},
    {"address":"shiraz", "area":210, "price": 1500,"accommodation":"elevator, kitchen"},
    {"address":"ghom", "area":150, "price": 1300,"accommodation":"elevator, oven"},
    {"address":"rasht", "area":120, "price": 1200,"accommodation":", parking, tv"},
    {"address":"ardebil", "area":100, "price": 1100,"accommodation":"air_condition, security"},
    {"address":"varamin", "area":160,"price": 1450, "accommodation":" parking, kitchen"},
    {"address":"semnan", "area":140,"price": 1350, "accommodation":"pool parking, "},



]

def cheak(accommodation):
    return accommodation["parking"]

result = list(filter(cheak, house_list))
print(result)

def city(address):
    return address["parking"]
result = sorted(result, key=city)

def all_total(total, address):
    return total + address["price"]

for address in result:
    print("price")

6
------------------------------------------------------





create table products
(
    id       integer primary key autoincrement,
    address     text,
    area      integer,
    price    integer
);

insert into products (id, address, area, price) values (1, 'tehran', 3,1000,3000);
insert into products (id, address, area, price) values (2, 'zanjan', 4,2000,8000);
tlt
-------