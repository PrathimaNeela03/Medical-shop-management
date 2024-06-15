class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, customer_id, name, contact):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact

class Supplier:
    def __init__(self, supplier_id, name, contact):
        self.supplier_id = supplier_id
        self.name = name
        self.contact = contact
# Inventory operations
def add_product(products):
    product_id = input("Enter product ID: ")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    products.append(Product(product_id, name, price, quantity))
    print("Product added successfully.")

def view_products(products):
    for product in products:
        print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

# Sales operations
def record_sale(products, sales):
    product_id = input("Enter product ID: ")
    quantity = int(input("Enter quantity sold: "))
    for product in products:
        if product.product_id == product_id:
            if product.quantity >= quantity:
                product.quantity -= quantity
                sales.append((product_id, quantity, product.price * quantity))
                print("Sale recorded successfully.")
                return
            else:
                print("Not enough stock.")
                return
    print("Product not found.")

def view_sales(sales):
    for sale in sales:
        print(f"Product ID: {sale[0]}, Quantity Sold: {sale[1]}, Total Price: {sale[2]}")

# Customer operations
def add_customer(customers):
    customer_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    contact = input("Enter customer contact: ")
    customers.append(Customer(customer_id, name, contact))
    print("Customer added successfully.")

def view_customers(customers):
    for customer in customers:
        print(f"ID: {customer.customer_id}, Name: {customer.name}, Contact: {customer.contact}")

# Supplier operations
def add_supplier(suppliers):
    supplier_id = input("Enter supplier ID: ")
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    suppliers.append(Supplier(supplier_id, name, contact))
    print("Supplier added successfully.")

def view_suppliers(suppliers):
    for supplier in suppliers:
        print(f"ID: {supplier.supplier_id}, Name: {supplier.name}, Contact: {supplier.contact}")

# Reports
def generate_inventory_report(products):
    print("Inventory Report")
    view_products(products)

def generate_sales_report(sales):
    print("Sales Report")
    view_sales(sales)
def main():
    products = []
    sales = []
    customers = []
    suppliers = []

    while True:
        print("\nMedical Shop Management System")
        print("1. Add Product")
        print("2. View Products")
        print("3. Record Sale")
        print("4. View Sales")
        print("5. Add Customer")
        print("6. View Customers")
        print("7. Add Supplier")
        print("8. View Suppliers")
        print("9. Generate Inventory Report")
        print("10. Generate Sales Report")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product(products)
        elif choice == '2':
            view_products(products)
        elif choice == '3':
            record_sale(products, sales)
        elif choice == '4':
            view_sales(sales)
        elif choice == '5':
            add_customer(customers)
        elif choice == '6':
            view_customers(customers)
        elif choice == '7':
            add_supplier(suppliers)
        elif choice == '8':
            view_suppliers(suppliers)
        elif choice == '9':
            generate_inventory_report(products)
        elif choice == '10':
            generate_sales_report(sales)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()