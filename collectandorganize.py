from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'name': [], 'discounted_price': [], 'mrp':[] ,'product_link': [], 'image_url':[], }
itr=0
max_med=70
for file in os.listdir("data"):
        if itr>=max_med:
            break
        try:
            with open(f"data/{file}") as f:
                html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')
            product = soup.find("div", class_="ProductCard_productCardGrid__NHfRH")
            name_tag = product.find_all("h2")[0] 
            name = name_tag.get_text(strip=True)
            link_tag = product.find("a", class_="cardAnchorStyle")
            product_link = "https://www.apollopharmacy.in" + link_tag['href']
            img_tag = product.find("img")
            image_url = img_tag['src'] if img_tag else "N/A"
            price_tag = product.find("p", class_="LR ER on_ Tb RR")
            discounted_price = price_tag.get_text(strip=True) if price_tag else "N/A"
            mrp_tag = product.find("span", class_="pn_")
            mrp = mrp_tag.get_text(strip=True) if mrp_tag else "N/A"
           
            d['name'].append(name)
            d['discounted_price'].append(discounted_price)
            d['product_link'].append(product_link)
            d['mrp'].append(mrp)
            d['image_url'].append(image_url)
            itr+=1
        except Exception as e:
         print(e)
df=pd.DataFrame(data=d)
df.to_csv("data.csv")
df.to_json("data.json")