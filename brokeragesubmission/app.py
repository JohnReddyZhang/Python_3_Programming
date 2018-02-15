import brokerage


_brokers_list = {}
_investors_list = {}


def _rename_exchange():
    brokerage.default_exchange.name = input('Please assign a new name: ')
    return f'Now your working exchange forum is {brokerage.default_exchange.name}'


def _add_stock(company_name, ticker_symbol):
    stock = brokerage.Stock(company_name, ticker_symbol)
    brokerage.default_exchange.add_security(stock)


def _set_prices():
    brokerage.default_exchange.set_prices()
    for symbol, stock in brokerage.default_exchange.securities.items():
        print(f'{symbol}, ask price: {stock.ask_price:.3f}, bid price: {stock.bid_price:.3f}')


def _set_broker(name, per_share_commission_amount):
    _brokers_list[name] = brokerage.Brokers(name, per_share_commission_amount)


def _set_investor(name, cash_balance):
    _investors_list[name] = brokerage.Investors(name, cash_balance)


def _set_portfolio(portfolio_name, investor_name):
    _investors_list[investor_name].portfolios[portfolio_name] \
        = brokerage.Portfolios(portfolio_name)


def opt_trade():
    print('PLEASE INPUT EXISTING VALUES.')
    investor_name = input('Please assign investor: ')
    broker = input('please assign a broker: ')
    ticker_symbol = input('You want to trade on stock symbol: ')
    portfolio_name = input('Using portfolio: ')
    quantity = input('The amount of trade is: (positive for buying, negative for selling)\n')
    exchange = brokerage.default_exchange
    _investors_list[investor_name].execute_trade(_brokers_list[broker], ticker_symbol, portfolio_name, quantity, exchange)
    print(f'Trade process ended.\n'
          f'Current investor\'s Net worth is {_investors_list[investor_name].net_worth():.3f}')


def loop(style_guide, example, func):
    while True:
        try:
            cont = input('Continue to add? y/n ')
            if cont == 'y':
                print(style_guide)
                func(*input(example).split(', '))
            elif cont == 'n':
                break
            else:
                raise ValueError
        except ValueError:
            print('Please input y or n!')
            continue


def run_app():
    try:
        print('Welcome! You are using the Default One World exchange forum.\n Do you want to set a new name to it?')
        if input('y/n: ') is 'y':
            _rename_exchange()

        print('Now you can add Stock to your exchange. PLEASE ADD AT LEAST ONE INSTANCE')
        loop('Please input the Stock\'s name and symbol:',
             'e.g. Apple, AAPL', _add_stock)

        input('Now setting prices. press any key to continue...')
        _set_prices()

        print('Now you can assign several brokers in the market. PLEASE ADD AT LEAST ONE INSTANCE')
        loop('Please input the Broker\'s name and his commission per share.',
             'e.g. Fidelity, 7.50', _set_broker)

        print('Now you can create Investors. PLEASE ADD AT LEAST ONE INSTANCE.')
        loop('Please input Investor\'s name and cash balance',
             'e.g. Billy Pope, 100', _set_investor)

        print('To add portfolios to a certain investor, please type in the investor\'s name,\n'
              'and then the portofolio\'s name.\n'
              'If the investor is not added in the previous step, you can add them here.' 
              'When you finish, type "exit" on investor name'
              'PLEASE, BY ANY METHOD, ADD AT LEAST ONE INSTANCE')
        while True:
            investor_name = None
            try:
                investor_name = input('Investor name: ')
                if not investor_name:
                    raise IOError
                elif investor_name == 'exit':
                    break
                elif investor_name not in _investors_list:
                    raise ValueError
                else:
                    portfolio_name = input('Portfolio\'s name: ')
                    _set_portfolio(portfolio_name, investor_name)
            except IOError:
                print('Please input an Investor name or exit!')
                continue
            except ValueError:
                create = input('Investor not created. Add this investor? y/n ')
                if create == 'y':
                    _set_investor(investor_name, input('Please then set cash balance: '))
                    _set_portfolio(input('Then Portfolio\'s name: '), investor_name)
                else:
                    print('Skipped. Restarting')
                    continue

        print('Finally, you can execute trade by typing "Trade"\n'
              'type exit to exit.\n'
              'On exit, the script will call all other functions that were not used before.\n')
        while True:
            command = input('Your call: ')
            if command == 'exit':
                print('Calling midmarket_value dynamic property:')
                for stock in brokerage.default_exchange.securities.values():
                    print(f'{stock.midmarket_value:.3f}')
                print('Other methods are already used in the process before.')
                break
            elif command == 'Trade':
                opt_trade()
            else:
                print('Please enter a valid command.')
                continue

    except KeyboardInterrupt:
        print("\nInterrupted and stopped. Use app.run_app() or restart to run again.")


run_app()
