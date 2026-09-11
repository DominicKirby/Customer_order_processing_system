# Customer Order Processing System

### Introduction and Explanation
This is a project to better understand file handling, including creating, transforming, and analysing a given *.csv* and *.json*.

The file requires only *csv* and *json* installed to run.

The *main.py* file sets up various functions to load in the data, compare the two files via customer lookup, process a single order to combine information from both the *csv* and *json* files, create an ordered total revenue created by any customer table and the most expensive customer, most expensive city and the spending in each city, the best selling product(s) and the amount of each product sold, and a concise but complete report on these functions. Further within *text_menu.py* there is a interactive menu to access all this information without directly accessing the *main.py* file. And for purposes of the client there is also a *processed_orders.json* and *report.json* in an output folder for checking and further analysis.

### The functions used and respective notes for each
```python 
def load_customers(filename: str = "customers.json"):
    """Loads in the customers.json file"""

def load_order(filename: str = "orders.csv"):
    """Loads in the orders.csv file"""

def customer_lookup(id:int, string):
    """Allows the user to lookup customer name or city based on input of ID number"""

def process_orders(orders):
    """Combines the customers.json and orders.csv file into 1 file which includes order_id, customer_name, city, product, quantity, price, and total for each order"""

def calculate_revenue_by_customer(processed_orders):
    """Works through each customer and finds the total money spent in the processed_orders"""

def calculate_revenue_by_city(processed_orders):
    """Works through the choices of customer and makes a set of unique cities to cycle through, then sums the total for each city in processed_orders"""

def calculate_units_by_product(processed_orders):
    """Works through customers to create a unique set of products, then works through the products list and sums the quantity to find the most popular product"""

def revenue_by_customer_ordered(processed_orders):
    """Sorts the customer revenue dictionary into descending order of revenue spent"""

def build_report(processed_orders):
    """Combines all the found information into one concise report"""

def save_json(data, filename):
    """Saves data into a json file title "filename""""

```
