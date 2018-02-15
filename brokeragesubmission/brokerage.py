from random import uniform


class Stock(object):
    def __init__(self, company_name, ticker_symbol):
        self.company_name = company_name
        self.ticker_symbol = ticker_symbol
        self.bid_price = None
        self.ask_price = None

    @property
    def midmarket_value(self):
        try:
            if self.bid_price and self.ask_price:
                return (self.bid_price + self.ask_price)/2
            raise ValueError
        except ValueError:
            if not self.bid_price:
                print('Bid price is empty!')
                return None
            print('Ask price is empty')
            return None


class Exchange(object):
    def __init__(self, name):
        self.name = name
        self.securities = {}  # Keys: stock ticker 'AAPL', Values: instances of Stock

    def add_security(self, stock):
        try:
            if not isinstance(stock, Stock):
                raise TypeError
            else:
                self.securities[stock.ticker_symbol] = stock
        except TypeError:
            print('Please add a Stock instance!')

    def set_prices(self):
        for ticker, stock in self.securities.items():
            ran_ask_price = uniform(1, 1000)
            ran_bid_price = uniform(ran_ask_price*(1-0.02), ran_ask_price*(1-0.005))
            self.securities[ticker].ask_price = ran_ask_price
            self.securities[ticker].bid_price = ran_bid_price


class Brokers(object):
    def __init__(self, name, per_share_commission_amount):
        self.name = name
        self.per_share_commission_amount = float(per_share_commission_amount)
        # This represents the amount an investor must pay to the broker per - share traded for executing
        # a trade on the investor's behalf.


class Portfolios(object):
    def __init__(self, name):
        self.name = name
        self.holdings = {}  # Keys: stock ticker 'AAPL', Values: number of share, an int, may be negative.

    def update_position(self, ticker_symbol, shares_purchased):
        if ticker_symbol in self.holdings:
            self.holdings[ticker_symbol] = self.holdings[ticker_symbol] + shares_purchased
        else:
            self.holdings[ticker_symbol] = shares_purchased

    # @property, could be a property.
    def current_value(self):
        # Positive value is "long", negative is "short"
        current_value_total = 0
        for value in self.each_current_value_generator():
            current_value_total += value[1]
        return current_value_total

    def each_current_value_generator(self):
        for ticker_symbol, number in self.holdings.items():
            stock = default_exchange.securities[ticker_symbol]  # make stock the item in Exchange. Add a Exception here?
            if number > 0:
                yield (ticker_symbol, number * stock.ask_price)
            elif number < 0:
                yield (ticker_symbol, number * stock.bid_price)


class Investors(object):
    def __init__(self, name, cash_balance):
        self.name = name
        self.cash_balance = float(cash_balance)
        self.portfolios = {}  # keys are portfolio names and values are instances of portfolio class

    def execute_trade(self, broker, ticker_symbol, portfolio_name, quantity, exchange):
        quantity = int(quantity)
        stock = exchange.securities[ticker_symbol]
        try:
            total_spence = broker.per_share_commission_amount * abs(quantity) \
                           + quantity * (stock.ask_price if quantity > 0 else stock.bid_price)
            if self.cash_balance < total_spence:
                raise ValueError
            self.cash_balance -= total_spence
            self.portfolios[portfolio_name].update_position(ticker_symbol, quantity)
        except ValueError:
            print('No enough money, trade cancelled.')
        # This method makes a call to the appropriate portfolio instance's update_position method

    def net_worth(self):
        net_worth = 0
        for name, portfolio in self.portfolios.items():
            print(f'Worth of {name} is {portfolio.current_value():.3f}')
            net_worth += portfolio.current_value()
        print(f'Sum is {net_worth}')
        return net_worth


default_exchange = Exchange("Default One World")