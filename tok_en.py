# package import statement
from smartapi import SmartConnect 
#or from smartapi.smartConnect import SmartConnect
#import smartapi.smartExceptions(for smartExceptions)

#create object of call
obj=SmartConnect(api_key="SBHeK1AK")
                #optional
                #access_token = "your access token",
                #refresh_token = "your refresh_token")

#login api call

data = obj.generateSession("T17727", "josh*1993")
refreshToken= data['data']['refreshToken']

#fetch the feedtoken
feedToken=obj.getfeedToken()

#fetch User Profile
userProfile= obj.getProfile(refreshToken)
# #place order
# try:
#     orderparams = {
#         "variety": "NORMAL",
#         "tradingsymbol": "SBIN-EQ",
#         "symboltoken": "3045",
#         "transactiontype": "BUY",
#         "exchange": "NSE",
#         "ordertype": "LIMIT",
#         "producttype": "INTRADAY",
#         "duration": "DAY",
#         "price": "19500",
#         "squareoff": "0",
#         "stoploss": "0",
#         "quantity": "1"
#         }
#     orderId=obj.placeOrder(orderparams)
#     print("The order id is: {}".format(orderId))
# except Exception as e:
#     print("Order placement failed: {}".format(e.message))



from smartapi import SmartWebSocket

# feed_token=092017047
FEED_TOKEN=feedToken
CLIENT_CODE="T17727"
# token="mcx_fo|224395"
token="nse_cm|3045&nse_cm|2885&nse_cm|1594&nse_cm|11536"    #SAMPLE: nse_cm|2885&nse_cm|1594&nse_cm|11536&nse_cm|3045
# token="mcx_fo|226745&mcx_fo|220822&mcx_fo|227182&mcx_fo|221599"
task="mw"   # mw|sfi|dp

ss = SmartWebSocket(FEED_TOKEN, CLIENT_CODE)
from datetime import datetime
import time

    



ltp_list1=[]
ltp_list2=[]
ltp_list3=[]


def ltpCheck():
    if ltp_list1[-1] < ltp_list1[0]:
        print(f"value gone down  {ltp_list1[-1]}initial val{ltp_list1[0]}")
        with open('value.txt', 'w') as f:
            f.write(ltp_list1[-1])
    if ltp_list2[-1] < ltp_list2[0]:
        print(f"value gone down  {ltp_list2[-1]}initial val{ltp_list2[0]}")
        with open('value.txt', 'w') as f:
            f.write(ltp_list2[-1])
    if ltp_list3[-1] < ltp_list3[0]:
        print(f"value gone down  {ltp_list3[-1]}initial val{ltp_list3[0]}")
        with open('value.txt', 'w') as f:
            f.write(ltp_list3[-1])
    
    with open('value.txt', 'w') as f:
        f.write(ltp_list1)
        

def on_message(ws, message):
    
    try:
        print("##########################################################")
        ltp_value1 = float(message[0]["ltp"])
        ltp_value2 = float(message[1]["ltp"])
        ltp_value3 = float(message[2]["ltp"])
        ltp_list1.append(ltp_value1)
        ltp_list2.append(ltp_value2)
        ltp_list3.append(ltp_value3)

        print("ltp_value1:",ltp_value1)
        print(".....................")
        print("ltp_value2:",ltp_value2)
        print(".....................")
        print("ltp_value3:",ltp_value3)
        ltpCheck()
        
        
    except :
        pass

    print("Ticks: {}".format(message))
     
def on_open(ws):
    print("on open")
    print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
    ss.subscribe(task,token)
    
def on_error(ws, error):
    print(error)
    
def on_close(ws):
   
    print("Close")

# Assign the callbacks.
ss._on_open = on_open
ss._on_message = on_message
ss._on_error = on_error
ss._on_close = on_close

ss.connect()



