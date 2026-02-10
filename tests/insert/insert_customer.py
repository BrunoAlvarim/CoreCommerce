import os
import sqlite3
import random
import string
from datetime import datetime, timedelta
import httpx


# ==============================
# Configurações
# ==============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../db/test_mass.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ==============================
# Cidade -> Estado (dados reais)
# ==============================

CITY_STATE = {
    "São Paulo": "SP",
    "Rio de Janeiro": "RJ",
    "Belo Horizonte": "MG",
    "Curitiba": "PR",
    "Porto Alegre": "RS"
}


# ==============================
# SQLite
# ==============================

def salvar_cliente_sqlite(cpf):
    cursor.execute("""
        INSERT OR IGNORE INTO customer (cpf)
        VALUES (?)
    """, (cpf,))


# ==============================
# Geradores Fake
# ==============================

def create_first_name():
    return ''.join(random.choices(string.ascii_letters, k=8)).capitalize()


def create_last_name():
    return ''.join(random.choices(string.ascii_letters, k=10)).capitalize()


def create_cpf():

    return ''.join([str(random.randint(0, 9)) for _ in range(8)])


def create_email(first_name, last_name):
    domains = ["teste.com", "email.com", "demo.com", "gmail.com", "outlook.com"]
    return f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"


def create_phone():
    return f"+55{random.randint(10,99)}9{random.randint(10000000,99999999)}"


def create_city_state():
    city = random.choice(list(CITY_STATE.keys()))
    return city, CITY_STATE[city]


def create_birth_date(min_age=18, max_age=80, allow_null=True):
    if allow_null and random.random() < 0.2:
        return None

    today = datetime.today()

    start_date = today - timedelta(days=365.25 * max_age)
    end_date = today - timedelta(days=365.25 * min_age)

    random_date = start_date + (end_date - start_date) * random.random()

    return random_date.strftime("%Y-%m-%d")

def post_customer():

    first_name = create_first_name()
    last_name = create_last_name()
    city, state = create_city_state()

    return {
        "first_name": first_name,
        "last_name": last_name,
        "cpf": create_cpf(),
        "email": create_email(first_name, last_name),
        "phone": create_phone(),
        "city": city,
        "state": state,
        "birth_date": create_birth_date()
    }
def main(total_clientes, base_url):

    url = f"{base_url}/customer/"
    with httpx.Client(timeout=10) as client:

        for i in range(total_clientes):

            customer = post_customer()
            cpf = customer["cpf"]

            try:

                response = client.post(url, json=customer)

                if response.status_code in (200, 201):

                    salvar_cliente_sqlite(cpf)
                    print(f"Cliente {i+1} criado")

                else:
                    print(f"Erro {response.status_code}: {response.text}")

            except Exception as e:
                print("Falha na requisição:", e)

    conn.commit()
    conn.close()

    print("\nFinalizado com sucesso!")


# ==============================

# if __name__ == "__main__":
#     main(TOTAL_CLIENTES, "http://localhost:8000/api")
