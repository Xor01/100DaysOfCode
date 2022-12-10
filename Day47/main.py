from bs4 import BeautifulSoup
from requests import get
import smtplib
import lxml
from os import environ

# URL: "https://www.amazon.sa/-/en/generation-Smart-speaker-Arabic-English/dp/B093QN7JTB/258-8707003-6595655?content-id=
# amzn1.sym.4a7a2f6e-f896-4ec9-82fa-c9b2d5d0b2a3&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
}


def get_price(product_url, headers_dic):
    # Get page data
    res = get(url=product_url, headers=headers_dic)
    soup = BeautifulSoup(res.content, 'lxml')

    # Extract product price
    try:
        price_whole = soup.find(name="span", class_="a-price-whole").get_text()
        price_fraction = soup.find(name="span", class_="a-price-fraction").get_text()
        total_price = float(price_whole + price_fraction)
    except AttributeError:
        total_price = None

    # Extract product name
    try:
        product_name = soup.find(name="span", id="productTitle").get_text()
    except AttributeError:
        product_name = "Could not reach"

    print(f"Product Name: {product_name.strip()}")
    print(f"Product Price: {total_price}")
    return [product_name.strip(), total_price]


def send_email(product_details, product_url):
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=environ['email'], password=environ['password'])
            connection.sendmail(
                from_addr=environ['email'],
                to_addrs=environ['email'],
                msg=f"Subject: Lower Price Alert\n\nProduct Name{product_details[0]}\nPrice: {product_details[1]}\n"
                    f"URL:{product_url}"
            )

    except smtplib.SMTPAuthenticationError:
        print("Authentication Error: check your credentials.")


def main():
    url = input("Enter Product URL: ")
    low_price = float(input("Enter a price to to send when product's lower is lower: "))
    product_details = get_price(url, headers)
    if product_details[1] and product_details[1] < low_price:
        # send_email(product_details, url)
        print("Yes")


if __name__ == '__main__':
    main()
