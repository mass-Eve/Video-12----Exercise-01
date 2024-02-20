import requests


def fetch_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()

    if (data['success'] and 'data' in data ):
        prod_data = data['data']['data']

        # prod1_data = prod_data[0]

        return prod_data

    else:
        raise Exception("Failed to get products details")

def main():
    try:
        products_data = fetch_products()
        
        for i in range(10):
            print('*'*70)
            print(f"This is product {i+1}:")
            prod_category = f"{products_data[i]['category']}"
            prod_price = f"{products_data[i]['price']}"
            print(f"\tProduct Category : {prod_category}")
            print(f"\tProduct Price : {prod_price}")

    except Exception as e:
        print(str(e))
    finally:
        print("Done ......")

if __name__ == "__main__":
    main()