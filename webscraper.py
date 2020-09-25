from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


# opens up connections and stores the web page
myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'
uClient = uReq(myUrl)
page_HTML = uClient.read()
uClient.close()

# html parser
page_soup = soup(page_HTML, 'html.parser')

# Extracting the data from a particular part of website URL
containers = page_soup.findAll("div", {"class": "item-container"})

# creating a file
filename = "products.csv"
f = open(filename, "w")

# crating a header for the file and writting it into the file
headers = "brand,product_name,shipping\n"
f.write("headers")


# Looping through the data
for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product: " + product_name)
    print("shipping cost: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|")+"," + shipping + "\n")

f.close()
