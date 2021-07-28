import os

class Config:
    aid = int(os.environ.get("5311825")
    ahash = os.environ.get("b9bb40745d9d4cb257b901e64e540a0e")
    bot_token = os.environ.get("1938715174:AAHmbodeaX3--9cgqE3qNQ-TYgFy1Rrjbd4")
    sudo = [239508098, 1313665327]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
