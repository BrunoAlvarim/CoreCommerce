import os
import shutil
import time
from create_db import create_db
from insert.insert_customer import main as post_costumer

base_url = 'http://127.0.0.1:8000/api'


def main():

    create_db()
    post_costumer(total_clientes = 100,base_url=base_url)


main()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_PATH = os.path.join(BASE_DIR, "db")


if os.path.exists(FOLDER_PATH):
    shutil.rmtree(FOLDER_PATH)
    print("a")