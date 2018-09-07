from get_twits import twitts
import get_stock_prices as pa
from read_file import read_tickers


def main():
    tickers = read_tickers('S&P 500.csv')
    print('Choose the company:')
    for i in range(len(tickers)):
        print(tickers[i][0], ' - ', i)
    s = int(input('Print the number: '))
    print('----------------------------------------------------')
    print('Company: ', tickers[s][0] )
    end_date=pa.give_date(tickers[s][1])
    print('Date: ', end_date)
    print('----------------------------------------------------')
    print('Related tweets:')
    start_date = pa.change_date(end_date)
    twitts(start_date, end_date, tickers[s][0])



main()