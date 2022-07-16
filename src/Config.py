import os

class Config:
    aid = int(os.environ.get("3716422"))
    ahash = os.environ.get('779c90c42677827af815808dac47244c')
    bot_token = os.environ.get("5565096928:AAG5ZV21qcBm5BGRDHLIV_9HlEBba71o1Ok")
    sudo = [1830238543]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
