import json
import os
import xml.etree.ElementTree as ET
import yaml as y

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_json_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json_file(filename, data):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def parse_xml_file(filename):
    path = os.path.join(BASE_DIR, filename)
    tree = ET.parse(path)
    root = tree.getroot()
    return {child.tag: child.text for child in root}


def load_yaml_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "r", encoding="utf-8") as file:
        return y.safe_load(file)


def main():
    json_products = load_json_file("product.json")
    print("JSON products:")
    for product in json_products:
        print(product)

    xml_product = parse_xml_file("product.xml")
    print("\nXML product:")
    print(xml_product)

    yaml_data = load_yaml_file("product.yml")
    print("\nYAML product data:")
    print(yaml_data)

    user_info = {"name": "Shriyaans", "age": 22}
    output = {
        "user": user_info,
        "json_products": json_products,
        "xml_product": xml_product,
        "yaml_product": yaml_data,
    }
    save_json_file("store.json", output)
    print("\nSaved combined data to store.json")


if __name__ == "__main__":
    main()
