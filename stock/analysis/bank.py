import pandas as pd
from matplotlib import pyplot as plt

from stock.models import BankBasicInfo,StockTradeMoneyHis
from stock.crawls.crawlutils import get_sql_engine

class BankAnalysis:
    '''
    
    '''
    # 板块走势分析
    def trend_analysis(self,bankname):
        bank = BankBasicInfo.objects.get(name=bankname)
        if not bank:
            return
        stocks = bank.stocks.all()
        codes = [stock.code for stock in stocks]
        codes = ','.join(codes)
        print(codes)
        df = pd.read_sql('select * from stock_stocktrademoneyhis where code in ({0})'.format(codes),con=get_sql_engine())
        df = df.drop('id',axis=1)
        df = df[df['change_rate']>=9]
        group = df.groupby('trade_date')
        close_count = group['code'].count()
        close_count = close_count.sort_index(ascending=False)
        # close_count = (close_count - close_count.shift(-1))/close_count.shift(-1) * 100
        close_count.plot()
        close_count = close_count.reset_index()
        print(close_count)
        close_count.plot()
        plt.show()






















