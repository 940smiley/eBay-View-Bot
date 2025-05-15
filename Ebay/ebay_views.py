import sys
import requests
import time
import random
import json
from time import sleep
import datetime
from colorama import init
import threading
from threading import Semaphore
from colorama import Fore, Back, Style
sys.path.append("Utilities")
import credentials
import get_proxy
import data
from requests import exceptions as requestsExceptions

init(autoreset=True)

class Views:
    def __init__(self, EBAY:object, i ):
        self.lock = EBAY.lock
        self.sem = EBAY.sem
        self.URL = EBAY.URL
        self.task = i
        self.s = requests.Session()
        self.start()
        
    def start(self):
        self.chooseProxy()
        self.getViews()
        self.sem.release()
        return

    def chooseProxy(self):
        self.s.proxies.update(get_proxy.get_proxy())
        return

    def getViews(self):
        self.lock.acquire()
        print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"{Fore.GREEN}Adding 1 View")
        self.lock.release()

        while True:
            try:
                request = self.s.get(self.URL, headers=data.Headers.addViews, timeout=12)
                if request.status_code == 200:
                    self.lock.acquire()
                    print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , f"{Fore.GREEN}View Added Successfully")
                    self.lock.release()
                return
            except requests.exceptions.ConnectionError as connectionerror:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[CONNECTION ERROR]", Fore.RED+str(connectionerror))
                self.lock.release()
                continue
            except requests.exceptions.Timeout as timeout:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[TIMEOUT ERROR]", Fore.RED+str(timeout))
                self.lock.release()
                self.chooseProxy()
                continue
            except requests.exceptions.RequestException as err:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[ERROR]", Fore.RED+str(err))
                self.lock.release()
                continue
            except requests.exceptions.ProxyError as proxErr:
                self.lock.acquire()
                print(Fore.LIGHTMAGENTA_EX + f"[Task#: {self.task}]" ,Fore.BLUE + format(datetime.datetime.now()) , Fore.RED + "[PROXY ERROR]", Fore.RED+str(proxErr))
                self.lock.release()
                self.chooseProxy()
                continue

if __name__ == "__main__":
    print("This module is intended to be used as part of the main application.")
