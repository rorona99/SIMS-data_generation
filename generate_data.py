import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define number of records for each table
NUM_SUPPLIERS = 20
NUM_PRODUCTS = 30
NUM_SUPPLIER_CONTRACTS = 20
NUM_CUSTOMERS = 50
NUM_EMPLOYEES = 20
NUM_SALES_ORDERS = 40
NUM_PURCHASE_ORDERS = 25
NUM_RETURN_REFUNDS = 15
NUM_REVIEWS = 50
NUM_PAYMENTS = 40
NUM_LOCATIONS = 15
NUM_SHIPPING_INFO = 35
NUM_WAREHOUSES = 10
NUM_STOCK_AUDITS = 20
NUM_PROMOTIONS = 10
NUM_INVENTORY_ADJUSTMENTS = 20
NUM_SUPPLIER_PRODUCTS = 50
NUM_PRODUCT_STOCK_LOCATIONS = 30
NUM_PRODUCT_PURCHASE_ORDERS = 25
NUM_PRODUCT_SALES_ORDERS = 40

# Generate Supplier data
suppliers = []
for _ in range(NUM_SUPPLIERS):
    suppliers.append({
        "SupplierID": fake.unique.random_int(min=1, max=1000),
        "Name": fake.company(),
        "Address": fake.address(),
        "Location": fake.city()
    })
df_suppliers = pd.DataFrame(suppliers)

# Generate Product data
products = []
for _ in range(NUM_PRODUCTS):
    products.append({
        "ProductID": fake.unique.random_int(min=1, max=1000),
        "Name": fake.word(),
        "Type": random.choice(["Electronics", "Clothing", "Furniture", "Toys"]),
        "AvailableQuantity": random.randint(1, 100),
        "PurchasePrice": round(random.uniform(5, 500), 2),
        "RestockLeadTime": random.randint(1, 14),
        "SupplierID": random.choice(df_suppliers["SupplierID"])
    })
df_products = pd.DataFrame(products)

# Generate SupplierContract data
supplier_contracts = []
for _ in range(NUM_SUPPLIER_CONTRACTS):
    supplier_contracts.append({
        "ContractID": fake.unique.random_int(min=1, max=1000),
        "SupplierID": random.choice(df_suppliers["SupplierID"]),
        "ContractStartDate": fake.date_between(start_date="-5y", end_date="today"),
        "ContractEndDate": fake.date_between(start_date="today", end_date="+5y"),
        "Terms": fake.sentence()
    })
df_supplier_contracts = pd.DataFrame(supplier_contracts)

# Generate Customer data
customers = []
for _ in range(NUM_CUSTOMERS):
    customers.append({
        "CustomerID": fake.unique.random_int(min=1, max=1000),
        "Name": fake.name(),
        "ContactDetails": fake.phone_number()
    })
df_customers = pd.DataFrame(customers)

# Generate Employee data
employees = []
for _ in range(NUM_EMPLOYEES):
    employees.append({
        "EmployeeID": fake.unique.random_int(min=1, max=1000),
        "Name": fake.name(),
        "Role": random.choice(["Manager", "Clerk", "Supervisor"]),
        "ContactDetails": fake.phone_number(),
        "HireDate": fake.date_between(start_date="-5y", end_date="today")
    })
df_employees = pd.DataFrame(employees)

# Generate SalesOrder data
sales_orders = []
for _ in range(NUM_SALES_ORDERS):
    sales_orders.append({
        "SalesOrderID": fake.unique.random_int(min=1, max=1000),
        "OrderDate": fake.date_between(start_date="-1y", end_date="today"),
        "TotalAmount": round(random.uniform(20, 1000), 2),
        "CustomerID": random.choice(df_customers["CustomerID"])
    })
df_sales_orders = pd.DataFrame(sales_orders)

# Generate PurchaseOrder data
purchase_orders = []
for _ in range(NUM_PURCHASE_ORDERS):
    purchase_orders.append({
        "PurchaseOrderID": fake.unique.random_int(min=1, max=1000),
        "OrderDate": fake.date_between(start_date="-1y", end_date="today"),
        "SupplierID": random.choice(df_suppliers["SupplierID"])
    })
df_purchase_orders = pd.DataFrame(purchase_orders)

# Generate Return/Refund data
return_refunds = []
for _ in range(NUM_RETURN_REFUNDS):
    return_refunds.append({
        "ReturnID": fake.unique.random_int(min=1, max=1000),
        "ProductID": random.choice(df_products["ProductID"]),
        "CustomerID": random.choice(df_customers["CustomerID"]),
        "ReasonForReturn": fake.sentence(),
        "ReturnDate": fake.date_between(start_date="-1y", end_date="today")
    })
df_return_refunds = pd.DataFrame(return_refunds)

# Generate Review data
reviews = []
for _ in range(NUM_REVIEWS):
    reviews.append({
        "ReviewID": fake.unique.random_int(min=1, max=1000),
        "Rating": random.randint(1, 5),
        "Comment": fake.sentence(),
        "CustomerID": random.choice(df_customers["CustomerID"]),
        "ProductID": random.choice(df_products["ProductID"])
    })
df_reviews = pd.DataFrame(reviews)

# Generate Payment data
payments = []
for _ in range(NUM_PAYMENTS):
    payments.append({
        "PaymentID": fake.unique.random_int(min=1, max=1000),
        "PaymentMethod": random.choice(["Credit Card", "PayPal", "Bank Transfer"]),
        "AmountPaid": round(random.uniform(20, 1000), 2),
        "PaymentDate": fake.date_between(start_date="-1y", end_date="today"),
        "SalesOrderID": random.choice(df_sales_orders["SalesOrderID"])
    })
df_payments = pd.DataFrame(payments)

# Generate StockLocation data
stock_locations = []
for _ in range(NUM_LOCATIONS):
    stock_locations.append({
        "LocationID": fake.unique.random_int(min=1, max=1000),
        "Address": fake.address()
    })
df_stock_locations = pd.DataFrame(stock_locations)

# Generate ShippingInformation data
shipping_info = []
for _ in range(NUM_SHIPPING_INFO):
    shipping_info.append({
        "ShippingID": fake.unique.random_int(min=1, max=1000),
        "Carrier": random.choice(["UPS", "FedEx", "DHL"]),
        "TrackingNumber": fake.ean13(),
        "ShippingDate": fake.date_between(start_date="-1y", end_date="today"),
        "ExpectedDeliveryDate": fake.date_between(start_date="today", end_date="+30d"),
        "SalesOrderID": random.choice(df_sales_orders["SalesOrderID"])
    })
df_shipping_info = pd.DataFrame(shipping_info)

# Generate Warehouse data
warehouses = []
for _ in range(NUM_WAREHOUSES):
    warehouses.append({
        "WarehouseID": fake.unique.random_int(min=1, max=1000),
        "Name": fake.company(),
        "Location": fake.city(),
        "Capacity": random.randint(1000, 10000)
    })
df_warehouses = pd.DataFrame(warehouses)

# Generate StockAudit data
stock_audits = []
for _ in range(NUM_STOCK_AUDITS):
    stock_audits.append({
        "AuditID": fake.unique.random_int(min=1, max=1000),
        "AuditDate": fake.date_between(start_date="-1y", end_date="today"),
        "Findings": fake.sentence(),
        "WarehouseID": random.choice(df_warehouses["WarehouseID"]),
        "EmployeeID": random.choice(df_employees["EmployeeID"])
    })
df_stock_audits = pd.DataFrame(stock_audits)

# Generate SalesPromotion data
promotions = []
for _ in range(NUM_PROMOTIONS):
    promotions.append({
        "PromotionID": fake.unique.random_int(min=1, max=1000),
        "Description": fake.sentence(),
        "StartDate": fake.date_between(start_date="-1y", end_date="today"),
        "EndDate": fake.date_between(start_date="today", end_date="+30d")
    })
df_promotions = pd.DataFrame(promotions)

# Generate InventoryAdjustment data
inventory_adjustments = []
for _ in range(NUM_INVENTORY_ADJUSTMENTS):
    inventory_adjustments.append({
        "AdjustmentID": fake.unique.random_int(min=1, max=1000),
        "ProductID": random.choice(df_products["ProductID"]),
        "EmployeeID": random.choice(df_employees["EmployeeID"]),
        "AdjustmentDate": fake.date_between(start_date="-1y", end_date="today"),
        "AdjustmentQuantity": random.randint(-50, 50),
        "Reason": fake.sentence()
    })
df_inventory_adjustments = pd.DataFrame(inventory_adjustments)

# Generate associative tables
supplier_products = []
for _ in range(NUM_SUPPLIER_PRODUCTS):
    supplier_products.append({
        "SupplierID": random.choice(df_suppliers["SupplierID"]),
        "ProductID": random.choice(df_products["ProductID"])
    })
df_supplier_products = pd.DataFrame(supplier_products).drop_duplicates()

product_stock_locations = []
for _ in range(NUM_PRODUCT_STOCK_LOCATIONS):
    product_stock_locations.append({
        "ProductID": random.choice(df_products["ProductID"]),
        "LocationID": random.choice(df_stock_locations["LocationID"])
    })
df_product_stock_locations = pd.DataFrame(product_stock_locations).drop_duplicates()

product_purchase_orders = []
for _ in range(NUM_PRODUCT_PURCHASE_ORDERS):
    product_purchase_orders.append({
        "ProductID": random.choice(df_products["ProductID"]),
        "PurchaseOrderID": random.choice(df_purchase_orders["PurchaseOrderID"])
    })
df_product_purchase_orders = pd.DataFrame(product_purchase_orders).drop_duplicates()

product_sales_orders = []
for _ in range(NUM_PRODUCT_SALES_ORDERS):
    product_sales_orders.append({
        "ProductID": random.choice(df_products["ProductID"]),
        "SalesOrderID": random.choice(df_sales_orders["SalesOrderID"])
    })
df_product_sales_orders = pd.DataFrame(product_sales_orders).drop_duplicates()
