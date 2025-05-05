import json


def fetch_products(app):
    product_data_filepath = app.config["PRODUCT_DATA_FILEPATH"]
    with open(product_data_filepath, encoding="utf-8") as file:
        products_data = json.load(file)
        return products_data
