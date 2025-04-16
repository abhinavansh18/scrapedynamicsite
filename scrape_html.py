from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()

genericMedicines = [
    "Paracetamol", "Calpol", "Cetcip", "Zedex", "Zincovit",
    "Dolo", "Multivitamin", "ORS", "Vitamin C", "Torex"
]

file = 0
for idx, med in enumerate(genericMedicines):
    driver.get(f"https://www.apollopharmacy.in/search-medicines/{med}")

    elems = driver.find_elements(By.CLASS_NAME, "ProductCard_productCardGrid__NHfRH   ")
    print(f"{len(elems)} items found for {med}")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{med}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

    time.sleep(2)

driver.close()
