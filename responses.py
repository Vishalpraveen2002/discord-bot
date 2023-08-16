import sqlite3
import pandas as pd
from openpyxl import load_workbook as lwb
import re
import generatePDF
import numpy as np

def get_response(msg, message: str):
    p_message: str = message.lower()
    p = str(msg.author)
    connection = sqlite3.connect("Project.db")
    c = connection.cursor()
    c.execute("select username from customers")
    if (f'{p}',) in c.fetchall():
        connection.close()

        if p_message == 'hello':
            x = str(msg.author).split('#')[0]
            return np.array([f"Hey {x}!\nWhat would you like to order",
                    'https://stylesatlife.com/wp-content/uploads/2022/10/best-menu-card-design.jpg.webp']), True

        if p_message == '!help':
            return np.array(['`Please send "Hello" to this bot to get the menu.\nPLease enter the item number to order.`']), False

        data = pd.read_excel("Food.xlsx")
        wb = lwb("Food.xlsx")
        ws = wb.worksheets[0]
        try:
            if int(p_message) in range(1, 6):
                u = int(p_message)
                if data.values[u - 1][1] > 0:
                    ws["B" + str(u + 1)] = data.values[u - 1][1] - 1
                    wb.save("Food.xlsx")
                    # receipt file part
                    generatePDF.generate_receipt(str(p.split('#')[0]), data.values[u - 1][0], data.values[u - 1][2])
                    return np.array([f"Order successfully placed\nPlease Pay Rs.{data.values[u - 1][2]}"]), True
                else:
                    return ["Out of stock"], True
        except:
            return ['I didn\'t understand what you wrote. Try typing "!help".'], False

    elif re.search("1bm[0-9][0-9][a-z][a-z][0-9][0-9][0-9]", p_message):
        connection = sqlite3.connect("Project.db")
        c = connection.cursor()
        c.execute("select usn from customers")
        x = p_message
        if (f'{x}',) in c.fetchall():
            connection.close()
            return ["Enter your correct USN!"], False
        else:
            a = str(msg.author)
            c.execute("insert into customers values (?,?) ", (a, x))
            connection.commit()
            connection.close()
            return [f"Hey {str(msg.author).split('#')[0]}\nSend 'Hello' to order"], True

    return ['`Please enter your USN to register`'], False
