import subprocess
import requests
import time


urls = [
    "http://45.77.186.141/mnstatus",
    "http://45.63.95.218/mnstatus",
    "http://45.32.133.172/mnstatus",
    "http://45.32.135.243/mnstatus",
    "http://149.28.202.56/mnstatus",
    "http://45.77.2.100/mnstatus",
    "http://104.207.150.38/mnstatus",
    "http://45.32.131.213/mnstatus",
    "http://144.202.104.178/mnstatus",
    "http://149.28.205.148/mnstatus",
]

sub = "MASTERNODE_SYNC_FINISHED"

def get_mn_status():
    result = ""
    for url in urls:
        output = ""
        try:
            r = requests.get(url, timeout=5)
            output += url + "</br>"
            output += r.text + "</br>"
            output += "====================================</br></br>"
        except:
            output += url + "</br>"
            output += "Request Error</br></br>"
            output += "====================================</br></br>"
        result += output
    
    count = result.count(sub)
    print("FINISH Count: ", count)


if __name__ == '__main__':
    index = 0
    while True:
        index += 1
        get_mn_status()
        if index > 10:
            break
        time.sleep(30)

        