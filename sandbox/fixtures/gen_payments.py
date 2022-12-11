import stripe
import csv

stripe.api_key = "sk_test_51MD62dBP34txZVvU3d6L6Lxyl64jt2ND30QEU17I5VZnnTKHos9Erh1YUfp2IJsimpKeiZLFGeNFwgyd8bBbI3GH00EvvV41y2"

def parse_csv(csv_file):
    with open(csv_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter = 0
        for row in csv_reader:
            price = int(float(row[7]) * 100)
            stripe.Product.create(name=row[3], default_price_data={
                                                                "currency": "eur",
                                                                "unit_amount_decimal": price
                                                            })
            counter += 1
            print(f'Product created: {row[3]} - {price}')
        print(f'Created {counter} products')

# DO NOT EXECUTE THIS SCRIPT, THERE IS NO COPY CHECK, IT WILL RECREATE EXISTING PRODUCTS
#parse_csv(name of the csv file)