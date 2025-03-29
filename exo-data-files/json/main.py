import json

def ligne_separation(caractere):
    print(f"{caractere}" * 30)

with open("data.json", "r") as input:
    data = json.load(input)

nom = data['user']['name']
email = data['user']['email']
order = data['user']['orders'][-1]

print(f"Nom : {nom}")
print(f"E-mail : {email}")
ligne_separation("-")
print("Dernière commande:")
print(f"  Order ID: {order['order_id']}")
print(f"  Date: {order['date']}")
print(f"  Total: {order['total']} €")
print("  Produits commandés:")
for item in order['items']:
    print(f"    - {item['name']}: {item['quantity']} x {item['price']} €")

ligne_separation("-")

new_order = {
   "order_id": "A002",
    "date": "2025-03-07",
    "total": 159.99,
    "items": [
        {
            "product_id": "P003",
            "name": "Product 3",
            "price": 79.99,
            "quantity": 1
        },
        {
            "product_id": "P004",
            "name": "Product 4",
            "price": 80.00,
            "quantity": 1
        }
    ] 
}

data["user"]["orders"].append(new_order)

with open('result.json', 'w') as result:
    json.dump(data, result, indent=4)
print("La nouvelle commande a bien été enregistrée !")