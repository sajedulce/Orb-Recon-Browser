import requests 
import os 
import webbrowser
import base64
  

search = input("Website/IP:")

search_orb = search.encode('utf-8')
orb_sentinel = base64.b64encode(search_orb)
orb64_search = orb_sentinel.decode('utf-8')
BOLD = "\033[1m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

url = f"https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q={search}"
url2 = f"https://securitytrails.com/domain/{search}"
url3 = f"https://www.shodan.io/search?query={search}"
url4 = f"https://api.hackertarget.com/dnslookup/?q={search}"
url5 = f"https://www.zoomeye.ai/searchResult?q={search}"
url6 = f"https://viewdns.info/iphistory/?domain={search}"
url7 = f"https://www.nslookup.io/domains/{search}/dns-records/"
url8 = f"https://web-check.xyz/check/{search}"
url9 = f"https://en.fofa.info/result?qbase64={orb64_search}"
url10 = f"https://fullhunt.io/search/?query={search}"

print(f"Opening search results for: {search}\nPresented By {BOLD}{GREEN}ORB{RESET} {BOLD}{RED}SENTINEL{RESET} (fb.me/orb.sentinel)...")

webbrowser.open(url, new=2)
webbrowser.open(url2, new=2)
webbrowser.open(url3, new=2)
webbrowser.open(url4, new=2)
webbrowser.open(url5, new=2)
webbrowser.open(url6, new=2)
webbrowser.open(url7, new=2)
webbrowser.open(url8, new=2)
webbrowser.open(url9, new=2)
webbrowser.open(url10, new=2)
