import os
import re
import logging


def main():
    logging.basicConfig(filename='data-changer.log', level=logging.INFO, format='%(asctime)s %(message)s')  # logging of the
    # script that shows if file was changed
    # --------------------------- ORDER FINDING --------------------------- #
    try:
        list_of_orders = os.listdir("Cargill_Interface/OUT")
    except FileNotFoundError:
        logging.error(f"[!] The system cannot find the path specified: 'Cargill_Interface/OUT'.")
    else:
        if len(list_of_orders) < 0:
            logging.info(f"[!] No files found.")
        else:
            for order_file in list_of_orders:
                with open(f"Cargill_Interface/OUT/{order_file}", "r",
                          encoding="ISO-8859-1") as data_file:  # opening in this format as ANSI
                    # doesn't recognized by Python
                    new_file = data_file.readlines()
                    order = "".join(new_file)
                # --------------------------- CHANGES --------------------------- #
                try:
                    wrong_date_format_searcher = re.search(r'\d+\.\d+\.\d+', order).group()  # Searching for
                    # dates in format "xx.xx.xxxx", for example: 03.08.2021
                except:
                    logging.info(f"[-] {order_file} wasn't changed.")
                    continue
                else:
                    splited_date = wrong_date_format_searcher.split(
                        ".")  # taking digits with splitting xx.xx.xxxx by dots
                    year = splited_date[2]
                    month = splited_date[1]
                    day = splited_date[0]
                    new_order = ""

                    if wrong_date_format_searcher in order:
                        new_order = order.replace(wrong_date_format_searcher, f"{year}-{month}-{day}")
                    # print(new_order)
                    # --------------------------- FILE CHANGING --------------------------- #
                    with open(f"Cargill_Interface/OUT/{order_file}", "w", encoding='utf_8_sig') as final_file:
                        final_file.write(new_order)
                    logging.info(f'[+] {order_file} was successfully changed.')

main()










