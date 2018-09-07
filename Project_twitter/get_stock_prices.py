import pandas_datareader.data as web
import datetime
def give_date(ticker):
    start = datetime.datetime(2018, 1, 1)
    end = datetime.datetime(2018, 8, 30)

    df = web.DataReader(ticker, 'yahoo', start, end)
    open_values = df["Open"].values
    close_values = df["Close"].values
    substractions = []
    for i in range(len(open_values)):
        substraction = open_values[i] - close_values[i]
        z = (i, substraction)
        substractions.append(z)
    substractions = sorted(substractions, key=lambda k: abs(k[1]), reverse=True)
    y = substractions[0][0]
    print('Stock price change: ',substractions[0][1],'$')
    table = df.ix[y:y + 1]
    str_table = str(table)
    for i in range(len(str_table)):
        if str_table[i].isdigit() == True:
            date = str_table[i : i + 10]
            break

    return date
def change_date(date):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    date -= datetime.timedelta(4)
    return str(date)[:10]



