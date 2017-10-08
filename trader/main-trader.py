# Libs
import krakenex
import time

# Variables
parameters = {"pair" : "XXRPZEUR"}
currentMovingAverage = 0
prices = []
lastTrade = 0

# Krakenex init 1
k = krakenex.API()

#Key loader from only 2 comps
#k.load_key('')

# Latency check
start = k.query_public('Time')
end = k.query_public('Time')
latency = end['result']['unixtime']-start['result']['unixtime']

print('latency: ' + str(latency))


timeout = time.time() + 60*60*24
while True:
    #print(type(k.query_public('Ticker',{"pair" : "XXRPZEUR"})))
    data = k.query_public('Ticker',{"pair" : "XXRPZEUR"})
    lastTrade = float(data['result']['XXRPZEUR']['c'][0])
    prices.append(lastTrade)
    print("Kraken - XRP/EUR - last transaction %r | moving average %r" % (lastTrade, currentMovingAverage))
    time.sleep(14)
    if time.time() > timeout:
        break

#lastTrade = float(data['result']['XXRPZEUR']['c'][0])
