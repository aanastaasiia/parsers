import requests
from bs4 import BeautifulSoup
import lxml

cookies = {
    'wfSessionId': 'qyNuYLdAaT10Uo-V8PHr',
    'wfTrackCookie': 'yUoy1XjLYIM0LBsPqi2F',
    'mobileVersion': 'na',
    'wf_h2p_1699891581': '1',
    'wf_h2p_3611321162': '1',
    'wf_h2p_2727015678': '1',
    '_gid': 'GA1.2.1386832675.1708597269',
    'zabUserId': '1708597269281zabu0.9298656167443531',
    'zsc52cb1ef0dab44a1aa201e5ee5ff2ef35': '1708597269407zsc0.9225553829783832',
    'zft-sdc': 'isef%3Dtrue-isfr%3Dtrue-src%3Ddirect',
    '_gcl_au': '1.1.1988339456.1708597270',
    'wf_h2p_1097695789': '1',
    'wf_h2p_511600405': '1',
    'wf_h2p_2771464370': '1',
    '_uetsid': '50db9d40d16c11ee9c7d79ca402b6b11',
    '_uetvid': '50dbe160d16c11ee9a84f95d3a62e684',
    '_ga_77BT9VMKLR': 'GS1.2.1708597270.1.1.1708597388.0.0.0',
    '_ga_6V0KLPCE6W': 'GS1.1.1708597269.1.1.1708597388.0.0.0',
    '_ga': 'GA1.2.1677502240.1708597269',
    'zps-tgr-dts': 'sc%3D1-expAppOnNewSession%3D%5B%5D-pc%3D3-sesst%3D1708597269408',
}

headers = {
    'authority': 'www.internationalwholesale.com',
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': 'wfSessionId=qyNuYLdAaT10Uo-V8PHr; wfTrackCookie=yUoy1XjLYIM0LBsPqi2F; mobileVersion=na; wf_h2p_1699891581=1; wf_h2p_3611321162=1; wf_h2p_2727015678=1; _gid=GA1.2.1386832675.1708597269; zabUserId=1708597269281zabu0.9298656167443531; zsc52cb1ef0dab44a1aa201e5ee5ff2ef35=1708597269407zsc0.9225553829783832; zft-sdc=isef%3Dtrue-isfr%3Dtrue-src%3Ddirect; _gcl_au=1.1.1988339456.1708597270; wf_h2p_1097695789=1; wf_h2p_511600405=1; wf_h2p_2771464370=1; _uetsid=50db9d40d16c11ee9c7d79ca402b6b11; _uetvid=50dbe160d16c11ee9a84f95d3a62e684; _ga_77BT9VMKLR=GS1.2.1708597270.1.1.1708597388.0.0.0; _ga_6V0KLPCE6W=GS1.1.1708597269.1.1.1708597388.0.0.0; _ga=GA1.2.1677502240.1708597269; zps-tgr-dts=sc%3D1-expAppOnNewSession%3D%5B%5D-pc%3D3-sesst%3D1708597269408',
    'referer': 'https://www.internationalwholesale.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

params = {
    'rand': '0.5553713024554445',
    'cookies': 'nlyhUq/kcEoS3qOdbTZ+DsRYXisdhcxC/mp+163MZFunrjfePUMtDhkygbYNuFVmqGMmOmhsfkoOteA1M6Z/KHExg6Zv9HBL',
    'siteId': '6943',
    'url': 'https://www.internationalwholesale.com/',
    'referer': '',
    'title': 'Wholesale Dollar Store Supplier - Dollar Items | International Bulk Discount Wholesale Distributor Near Me',
    'memberIds': '',
}

response = requests.get('https://www.internationalwholesale.com/', params=params, cookies=cookies, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
#забираем названия
names = []
brands = []
nameshtml = soup.findAll(itemprop="name")
for name in range(1, len(nameshtml), 2):
    i = nameshtml[name].get('content')
    names.append(i)
brand = nameshtml[0].get('content')
brands.append(brand)

#забираем upc и scu
upcs = []
scus = []
elems = soup.findAll(style="font-size: 9pt; color: #515254; font-weight: bold; font-style: normal; text-decoration: none")
for i in elems:
    number = i.get_text()
    if len(number) == 10:
        upcs.append(number)
    elif len(number) == 5:
        scus.append(number)
print(names, brands, upcs, scus)
