import requests
import pyfiglet

response = requests.get('https://api.ipify.org')
ip_address = response.text.strip()

ascii_art = pyfiglet.figlet_format(ip_address)
print(ascii_art)