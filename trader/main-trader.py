import krakenex

k = krakenex.API()


k.load_key('')



print(k.query_private('Balance'))
