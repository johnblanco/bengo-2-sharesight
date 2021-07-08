import pandas as pd
from os import listdir
from os.path import isfile, join

columns = ["Trade Date", "Instrument Code", "Market Code", "Quantity", "Price",
           "Transaction Type", "Exchange Rate (optional)", "Brokerage (optional)",
           "Brokerage Currency (optional)", "Comments (optional)"]


def source_files():
    files = [f for f in listdir(".") if isfile(join(".", f))]
    return list(filter(lambda x: 'txt' in x, files))


def df_from_lines(stock, lines):
    rows = {}
    temp_arr = []
    i = 0
    for l in lines:
        temp_arr.append(l)
        if len(temp_arr) == 4:
            transaction_type = "SELL" if 'VEN' in temp_arr[1] else 'BUY'
            quantity = abs(int(temp_arr[2].replace(".","").replace(",00", "")))
            price = temp_arr[1][8:]
            date = temp_arr[0]

            rows[i] = [date, stock, "NYSE", quantity, price, transaction_type, None, None, None, None]
            i += 1
            temp_arr = []

    df = pd.DataFrame.from_dict(rows, orient='index',
                                columns=columns)

    return df


def read_file(filename):
    original_lines = open(filename, "r").read().split("\n")
    return list(filter(lambda x: x != '', original_lines))


def main():
    files = source_files()
    if len(files) == 0:
        print("No se encontraron archivos txt para leer")
    for filename in files:
        stock = filename.replace(".txt", "").upper()
        lines = read_file(filename)

        df = df_from_lines(stock, lines)
        df.to_csv('{}.csv'.format(stock), index=False)
        print('exportando {}.csv ... LISTO'.format(stock))


if __name__ == "__main__":
    main()
