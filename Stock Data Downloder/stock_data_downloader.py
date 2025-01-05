import yfinance as yf
import os

def download_stock_data(ticker, start_date, end_date):
    print(f"Downloading data for {ticker} from {start_date} to {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    
    filename = f"{ticker}_data.csv"
    
    print(f"Saving data to {filename}...")
    data.to_csv(filename)
    
    print("Download complete!")

if __name__ == "__main__":
    print("Welcome to the Stock Data Downloader!")
    
    ticker_symbol = input("Enter the stock ticker symbol (e.g., AAPL): ").strip()
    start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter the end date (YYYY-MM-DD): ").strip()
    
    download_stock_data(ticker_symbol, start_date, end_date)
    
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")
