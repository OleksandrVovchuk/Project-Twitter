def read_tickers(path):
    f = open(path, 'r')
    tickers_list = [(line.split(',')[1], line.split(',')[0]) for line in f ]
    del tickers_list[0]
    return tickers_list
print(read_tickers('S&P 500.csv'))