import csv
import json

def load_customers(filename: str):
    with open (filename) as file:
        return json.load(file)

def load_order(filename: str):
    with open (filename) as file:
        reader = csv.DictReader(file)
        return [{k.strip(): v.strip() for k, v in row.items()} for row in reader]


def customer_lookup(id:int, string):
    global customers_json
    if string == "customer_id":
        for customer in customers_json:
            if customer["customer_id"] == id:
                return customer["name"]
    elif string == "city":
        for customer in customers_json:
            if customer["customer_id"] == id:
                return customer["city"]
    else:
        return print("incorrect_input")

def process_orders(orders):
    new_list = []
    for row in orders:
        new_entry ={
            "order_id": row["order_id"],
            "customer_name": customer_lookup(int(row["customer_id"]), "customer_id"),
            "city": customer_lookup(int(row["customer_id"]), "city"),
            "product" : row["product"],
            "quantity": row["quantity"],
            "price": row["price"],
            "total": int(row["price"]) * int(row["quantity"])
         }
        new_list.append(new_entry)
    return new_list

def calculate_revenue_by_customer(processed_orders):
    revenue_by_customer = {}
    for customer in customers_json:
        personal_revenue = 0
        for order in processed_orders:
            if customer["name"] == order["customer_name"]:
                personal_revenue += order["total"]
        revenue_by_customer[customer["name"]] =  personal_revenue
    return revenue_by_customer

def calculate_revenue_by_city(processed_orders):
    revenue_by_city = {}
    for customer in customers_json:
        city_revenue = 0
        for order in processed_orders:
            if customer["city"] == order["city"]:
                city_revenue += order["total"]
        revenue_by_city[customer["city"]] =  city_revenue
    return revenue_by_city

def calculate_units_by_product(processed_orders):
    product_set = set()

    for row in processed_orders:
        product_set.add(row["product"])

    units_by_product = {}

    for product in product_set:
        product_total = 0
        for order in processed_orders:
            if order["product"] == product:
                product_total += int(order["quantity"])
        units_by_product[product] = product_total

    return units_by_product

def revenue_by_customer_ordered(processed_orders):
    revenue_by_customer = calculate_revenue_by_customer(processed_orders)

    customer_list = list(revenue_by_customer.items())

    values_list = []
    names_list = []

    for customer in customer_list:
        values_list.append(customer[1])

    values_list.sort(reverse=True)

    for i in range(len(values_list)):
        for customer in customer_list:
            if customer[1] == values_list[i]:
                names_list.append(customer[0])


    ordered_revenue_dict = {}

    for i in range(len(names_list)):
        ordered_revenue_dict[names_list[i]] = values_list[i]

    return ordered_revenue_dict

def build_report(processed_orders):
    report = {}
    total_revenue = 0
    revenue_by_customer = calculate_revenue_by_customer(processed_orders)
    revenue_by_city = calculate_revenue_by_city(processed_orders)
    units_by_product = calculate_units_by_product(processed_orders)
    ordered_revenue_dict = revenue_by_customer_ordered(processed_orders)

    for row in processed_orders:
        total_revenue += row["total"]

    report["total_revenue"] = total_revenue

    average_order_value = total_revenue / len(processed_orders)

    top_customer = max(revenue_by_customer, key=revenue_by_customer.get)

    top_city = max(revenue_by_city, key=revenue_by_city.get)

    highest_quantity = max(units_by_product.values())
    top_products = [name for name, product in units_by_product.items() if product == highest_quantity]



    report["total_revenue"] = total_revenue
    report["top_customer"] = top_customer
    report["top_city"] = top_city
    report["top_products"] = top_products
    report["average_order_value"] = average_order_value
    report["ordered_revenue_dict"] = ordered_revenue_dict
    return report


customers_json = load_customers("customers.json")

orders_csv = load_order("orders.csv")

processed_orders = process_orders(orders_csv)

customer_set = set()

for row in processed_orders:
    customer_set.add(row["customer_name"])

number_of_customers = len(customer_set)

report = build_report(processed_orders)

def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

save_json(processed_orders, "output/processed_orders.json")

save_json(report, "output/report.json")


