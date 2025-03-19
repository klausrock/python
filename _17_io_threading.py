""" 
How to Speed Up an I/O-Bound Program

Let's start by focusing on I/O-bound programs and a common problem: 
downloading content over the network. 
For our example, you will be downloading web pages from a few sites, 
but it really could be any network traffic. It's just easier to 
visualize and set up with web pages.

https://realpython.com/python-concurrency/#how-to-speed-up-an-io-bound-program
"""
import concurrent.futures
import requests
import threading
import time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":

    sites = ["https://http-quss.com/test/test05/img0001.png",
     "https://http-quss.com/test/test05/img0002.png",
     "https://http-quss.com/test/test05/img0003.png",
     "https://http-quss.com/test/test05/img0004.png",
     "https://http-quss.com/test/test05/img0005.png",
     "https://http-quss.com/test/test05/img0006.png",
     "https://http-quss.com/test/test05/img0007.png",
     "https://http-quss.com/test/test05/img0008.png"
     ] 

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")