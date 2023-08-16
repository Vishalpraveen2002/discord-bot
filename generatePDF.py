import random


def generate_receipt(customer_name, item, price):
    order_number = random.randint(0, 100000)
    with open("receipt_{}.txt".format(order_number), "w") as receipt_file:
        receipt_file.write("-------------------------------------------\n")
        receipt_file.write("Receipt for Order #{}\n".format(order_number))
        receipt_file.write("Customer Name: {}\n".format(customer_name))
        receipt_file.write("Item: {}\n".format(item))
        receipt_file.write("Price: {}\n".format(price))
        receipt_file.write("Thank you for your purchase!")
