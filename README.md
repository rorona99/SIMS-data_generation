# SIMS-data_generation

This directory contains scripts and sample datasets for **Milestone #3** of the Inventory Management System project. The goal is to generate realistic data to populate the database and validate its functionality.

## Breakdown
- The generated data is used to:
  - Populate tables created in SQL scripts repository
  - Test relationships, queries, and the overall database structure.
- Scripts utilize Python's `Faker` library to create datasets for entities such as:
  - Suppliers
  - Products
  - Customers
  - Warehouses

## Related Resources
- SQL scripts to create and load the generated data into the database can be found in the `/sql_scripts` directory.
