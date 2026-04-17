import portfolio.data
from portfolio.data import create_portfolio
from portfolio.report import print_report

my_portfolio = portfolio.data.create_portfolio("Retirement")
portfolio.report.print_report(my_portfolio)