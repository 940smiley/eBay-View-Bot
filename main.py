import sys
import datetime
import time
from time import sleep
from colorama import init
import threading
from threading import Semaphore
from colorama import Fore, Back, Style
from Ebay import ebay_views
from Ebay import account_create
from Ebay import ebay_watchers

init(autoreset=True)

class EBAY:
    def __init__(self,) -> None:
        self.lock = Semaphore(value=1)

        print(Fore.GREEN +"███████╗██████╗  █████╗ ██╗   ██╗".center(90))
        print(Fore.GREEN +"██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝".center(90))
        print(Fore.GREEN +"█████╗  ██████╔╝███████║ ╚████╔╝ ".center(90))
        print(Fore.GREEN +"██╔══╝  ██╔══██╗██╔══██║  ╚██╔╝  ".center(90))
        print(Fore.GREEN +"███████╗██████╔╝██║  ██║   ██║  ".center(87))
        print(Fore.GREEN +"╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝ ".center(87))
        print()

        print(f"{Fore.CYAN}[1] {Fore.YELLOW}Add Views".center(92))
        print(f"{Fore.CYAN}[2] {Fore.YELLOW}Add Watchers".center(93))
        print(f"{Fore.CYAN}[3] {Fore.YELLOW}Account Generator".center(100))
        print(f"{Fore.CYAN}Press 'q' to Quit".center(100))
        print()
            
        self.main()

    def main(self):
        while True:
            choice = input(f"{Fore.CYAN}Enter your choice: ")
            if choice == "1":
                self.URL = str(input("Enter eBay Listing URL: "))
                while 'https://www.ebay.com' not in self.URL:
                    print(Fore.BLUE + format(datetime.datetime.now()), Fore.RED +"Please Enter a valid eBay Link")
                    self.URL = str(input("Enter eBay Listing URL: "))
                self.view()
            elif choice == "2":
                self.URL = str(input("Enter eBay Listing URL: "))
                while 'https://www.ebay.com' not in self.URL:
                    print(Fore.BLUE + format(datetime.datetime.now()), Fore.RED +"Please Enter a valid eBay Link")
                    self.URL = str(input("Enter eBay Listing URL: "))
                self.watcherBot()
            elif choice == "3":
                self.accountGenerator()
            elif choice == "q":
                print(Fore.BLUE +"Closing Instance...  Bye Bye!")
                break
            else:
                print(Fore.BLUE + format(datetime.datetime.now()), Fore.RED +"ERROR CHOICE UNAVAILABLE!")

    def view(self):
        if 'https://www.ebay.com' not in self.URL:
            print(Fore.BLUE + format(datetime.datetime.now()), Fore.RED +"Please Enter a valid eBay Link")
            return

        views = int(input("Enter amount of views needed: "))
        num_tasks = int(input("Enter amount of tasks at a time: "))
        self.sem = threading.Semaphore(value=num_tasks)
        threads = []
        for i in range(views):
            self.sem.acquire()
            task = threading.Thread(target=ebay_views.Views, args=(self, i))
            threads.append(task)
            time.sleep(.05)
            task.start()
        for t in threads:
            t.join()

    def watcherBot(self):
        views = int(input("Enter amount of Watchers needed: "))
        num_tasks = int(input("Enter amount of tasks at a time: "))
        self.sem = threading.Semaphore(value=num_tasks)
        threads = []
        with open('Config/created_accounts.txt', 'r') as f1:
            for i, line in enumerate(f1):
                parts = line.strip().split(":")
                if len(parts) < 2:
                    continue
                email, password = parts[0], parts[1]
                self.sem.acquire()
                task = threading.Thread(target=ebay_watchers.Watch, args=(self, email, password, i))
                threads.append(task)
                time.sleep(.05)
                task.start()
        for t in threads:
            t.join()
              
    def accountGenerator(self):
        num_tasks = int(input("Enter amount of tasks at a time: "))
        self.sem = threading.Semaphore(value=num_tasks)
        threads = []
        with open('Config/emails.txt', 'r') as f1:
            for i, line in enumerate(f1):
                email = line.strip().split(":")[0]
                self.sem.acquire()
                task = threading.Thread(target=account_create.Gen, args=(self, email, i))
                threads.append(task)
                time.sleep(.05)
                task.start()
        for t in threads:
            t.join()

if __name__ == "__main__":
    EBAY()
    sleep(3)
    exit()
