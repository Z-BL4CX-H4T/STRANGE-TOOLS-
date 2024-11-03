import requests
import threading

def make_request(url, method, headers=None, data=None):
    """
    Melakukan request ke website dengan berbagai metode HTTP.

    Args:
    url: URL website.
    method: Metode HTTP (GET, POST, PUT, DELETE, PATCH).
    headers: Header request (opsional).
    data: Data request (opsional).
    """
    try:
        response = requests.request(method, url, headers=headers, data=data)
        response.raise_for_status()  # Memeriksa status code HTTP

        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Content-Type: {response.headers['Content-Type']}")
        print(f"Content: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Attack: {e}")

def thread_function(url, method, headers=None, data=None):
    """
    Fungsi yang dijalankan dalam thread terpisah.
    """
    make_request(url, method, headers, data)

if __name__ == '__main__':
    url = input("Masukkan URL website: ")
    num_threads = int(input("Masukkan jumlah thread: "))
    method = input("Masukkan metode HTTP (GET, POST, PUT, DELETE, PATCH): ").upper()

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=thread_function, args=(url, method))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
