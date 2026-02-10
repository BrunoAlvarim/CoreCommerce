# 🧠 TitanLake — Modelagem Transacional da API

CoreCommerce é uma plataforma simulada criada para demonstrar uma arquitetura moderna de dados com API transacional para vendas de Hardware
---

# 📊 Diagrama de Entidades

```mermaid
erDiagram

STORE ||--o{ SALE : realiza
CUSTOMER ||--o{ SALE : compra
SALE ||--o{ SALE_ITEM : possui
PRODUCT ||--o{ SALE_ITEM : compoe
STORE ||--o{ INVENTORY : controla
PRODUCT ||--o{ INVENTORY : estocado

STORE {
    uuid store_id PK
    string store_name
    string store_type
    string cnpj
    string email
    string phone
    string address
    string city
    string state
    string zipcode
    decimal latitude
    decimal longitude
    timestamp created_at
    boolean active
}

CUSTOMER {
    uuid customer_id PK
    string first_name
    string last_name
    string cpf
    string email
    string phone
    date birth_date
    timestamp created_at
    boolean active
}

PRODUCT {
    uuid product_id PK
    string sku
    string product_name
    string category
    string brand
    string model
    decimal base_price
    decimal cost_price
    int warranty_months
    timestamp created_at
    boolean active
}

SALE {
    uuid sale_id PK
    uuid store_id FK
    uuid customer_id FK
    timestamp sale_date
    decimal gross_amount
    decimal discount_amount
    decimal net_amount
    string payment_method
    int installments
    string status
}

SALE_ITEM {
    uuid sale_item_id PK
    uuid sale_id FK
    uuid product_id FK
    int quantity
    decimal unit_price
    decimal discount_amount
    decimal total_price
    decimal final_price
}

INVENTORY {
    uuid inventory_id PK
    uuid store_id FK
    uuid product_id FK
    int quantity
    timestamp last_update
}
