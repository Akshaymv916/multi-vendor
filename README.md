# Advanced Multi-Vendor E-Commerce API

## Overview
This project is a multi-vendor e-commerce API built using Django Rest Framework (DRF) with JWT authentication. It allows multiple vendors to sell products while customers can place orders. The API includes features such as vendor management, product management, and order processing.

## Features

### Authentication
- JWT-based authentication using email and password.
- Custom permission: Only vendors can create/update products.

### Vendor Management
- `POST /api/vendor/register/` → Register as a vendor.
- `GET /api/vendor/profile/` → Get vendor details (only for logged-in vendors).

### Product Management
- `POST /api/products/` → Add a product (only for vendors).
- `PUT /api/products/{id}/` → Update a product (only by the vendor who created it).
- `DELETE /api/products/{id}/` → Delete a product (only by the vendor who created it).

### Order Management
- `POST /api/orders/orders/` → Create an order.
- `GET /api/orders/orders/{id}/` → Get order details.
- `POST /api/orders/orders/{id}/update-status/` → Update order status (only admin can update).
- When an order is placed, the stock of each product is reduced accordingly.
- Order confirmation email is sent to the customer.

