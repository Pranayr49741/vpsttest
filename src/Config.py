import os

class Config:
    aid = int(os.environ.get("18622297")
    ahash = os.environ.get("27e6993af0786f66f96599db6cd10bcc")
    bot_token = os.environ.get("5006835603:AAEOu5gqL7vi6CxnxLCo4lCgxh95aWFH2fU")
    sudo = [163494588, 1511373882]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
