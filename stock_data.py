import yfinance as yf


def download_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

tickers = ['MSFT']   # Example list of tickers
start_date = "2024-03-01"
end_date = "2024-12-31"

stock_data = download_stock_data(tickers, start_date, end_date)
print(stock_data)

print(yf.get_income_statement('MSFT'))