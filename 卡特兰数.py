# -*- coding: utf8 -*-
import ccxt
import time
exchange_class = getattr(ccxt, 'huobipro')
exchange = exchange_class({
    'apiKey': "8a145ec9-3b4261d8-06eb8713-f3ad3",
    'secret': "5ee7bf92-57d5a5f2-1afb2dd4-30efe",
    'timeout': 30000,
    'enableRateLimit': False,
})
exchange.options['createMarketBuyOrderRequiresPrice'] = False
while True:
    try:
        res = exchange.create_market_buy_order('TOP/HT', 200)
    except Exception as e:
        time.sleep(0.1)

