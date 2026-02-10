# 🧠 TitanLake — Modelagem Transacional da API

CoreCommerce é uma plataforma simulada criada para demonstrar uma arquitetura moderna de dados com API transacional para vendas de Hardware
---

# 📊 Diagrama de Entidades

```mermaid
erDiagram

STORE ||--o{ INVENTORY : has
STORE ||--o{ SALE : generates
CUSTOMER ||--o{ SALE : makes
SALE ||--o{ SALE_ITEM : contains
PRODUCT ||--o{ SALE_ITEM : sold_in
PRODUCT ||--o{ INVENTORY : stocked_in

STORE {
    string store_id PK
    string store_name
    string store_type
    string cnpj
    string email
    string phone
    string address
    string city
    string state
    string zipcode
    float latitude
    float longitude
    datetime created_at
}

CUSTOMER {
    string customer_id PK
    string first_name
    string last_name
    string cpf
    string email
    string phone
    datetime birth_date
    datetime created_at
}

PRODUCT {
    string product_id PK
    string sku
    string product_name
    string category
    string brand
    string model
    float base_price
    float cost_price
    datetime created_at
}

SALE {
    string sale_id PK
    string store_id FK
    string customer_id FK
    datetime sale_date
    float gross_amount
    float discount_amount
    float net_amount
    string payment_method
    int installments
    string status
    datetime created_at
}

SALE_ITEM {
    string sale_item_id PK
    string sale_id FK
    string product_id FK
    int quantity
    float unit_price
    float discount
    float total_price
}

INVENTORY {
    string inventory_id PK
    string store_id FK
    string product_id FK
    int stock_quantity
    datetime last_update
}
