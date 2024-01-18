import yfinance as yf

def fetch_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.info

def analyze_competitive_advantage(info):
    # Check for high return on equity
    count = 0
    if 'returnOnEquity' in info and info['returnOnEquity'] > 0.15:
        print("High return on equity indicates a competitive advantage.")
        count += 1
    # Check for high profit margins
    if 'profitMargins' in info and info['profitMargins'] > 0.20:
        print("High profit margins indicate a competitive advantage.")
        count += 1
    # Check for low debt to equity ratio
    if 'debtToEquity' in info and info['debtToEquity'] < 0.50:
        print("Low debt to equity ratio indicates a competitive advantage.")
        count += 1
    # Check for high free cash flow
    if 'freeCashflow' in info and info['freeCashflow'] > 1000000000:  # 1 billion
        print("High free cash flow indicates a competitive advantage.")
        count += 1
    # Check for high return on assets
    if 'returnOnAssets' in info and info['returnOnAssets'] > 0.10:
        print("High return on assets indicates a competitive advantage.")
        count += 1
    # Check for high net income
    if 'netIncome' in info and info['netIncome'] > 1000000000:  # 1 billion
        print("High net income indicates a competitive advantage.")
        count += 1
    if count == 6:
        print("Strong Competitive Advantage. 6/6 key metrics met.")
    elif count >= 3 and count < 6:
        print(f"Moderate Competitive Advantage. {count}/6 key metrics met.")
    else:
        print(f"No Competitive Advantage. {count}/6 key metrics met.")
    
    
    
    

def main():
    while True:
        ticker = input("Enter the ticker symbol of the company you are interested in: ")
        if not ticker:
            print("Ticker symbol cannot be empty. Please try again.")
            continue

        try:
            info = fetch_data(ticker)
        except Exception as e:
            print(f"Failed to fetch data for ticker symbol {ticker}. Please try again.")
            continue

        def quarterly_income_stmt(ticker):
            stock = yf.Ticker(ticker)
            print(f"{ticker}'s Income Statement: ")
            print("--------------------------")
            print(stock.quarterly_financials)
            print("--------------------------")
            print(f"{ticker}'s Balance Sheet: ")
            print("--------------------------")
            print(stock.quarterly_balance_sheet)
            print("--------------------------")
            print(f"{ticker}'s Cash Flow Statement: ")
            print("--------------------------")
            print(stock.quarterly_cashflow)
            print("--------------------------")

        # Display extended information
        print(f"\nCompany Name: {info['shortName']}")
        print(f"Current Price: {info['currentPrice']}")
        print(f"PE Ratio: {info['trailingPE'] if 'trailingPE' in info else 'N/A'}")
        print(f"PB Ratio: {info['priceToBook'] if 'priceToBook' in info else 'N/A'}")
        print(f"Profit Margins: {info['profitMargins'] if 'profitMargins' in info else 'N/A'}")
        print(f"Return on Equity: {info['returnOnEquity'] if 'returnOnEquity' in info else 'N/A'}")
        print(f"Dividend Yield: {info['dividendYield'] if 'dividendYield' in info else 'N/A'}")
        print(f"Debt to Equity: {info['debtToEquity'] if 'debtToEquity' in info else 'N/A'}")
        print(f"Free Cash Flow: {info['freeCashflow'] if 'freeCashflow' in info else 'N/A'}")
        print(f"Cash Flow from Operations: {info['cashFlow'] if 'cashFlow' in info else 'N/A'}")
        print(f"Return on Assets: {info['returnOnAssets'] if 'returnOnAssets' in info else 'N/A'}")
        print(f"Net Income: {info['netIncome'] if 'netIncome' in info else 'N/A'}")  # New line for Net Income
        print("--------------------------")
        quarterly_income_stmt(ticker)

        # Analyze for competitive advantage
        advantage = analyze_competitive_advantage(info)
        print(advantage)

        # Option to end the program
        if input("\nWould you like to analyze another company? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main() 




