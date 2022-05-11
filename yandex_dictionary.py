from fake_useragent import UserAgent
import requests

chrome = UserAgent().chrome

def get_from_dict(word, lang_from='ru', lang_to='en'):
    # Good luck
    x = requests.post(
        f"https://dictionary.yandex.net/dicservice.json/lookupMultiple?sid=aa81f3de.627bb1c4.5a068a6b.74722d74657874&ui={lang_from}&srv=tr-text&text={word}&type=regular,syn,ant,deriv&lang={lang_from}-{lang_to}&flags=15398&dict={lang_from}-{lang_to}.regular,{lang_from}.syn,{lang_from}.ant,{lang_from}.deriv&yu=986734521652273541&yum=1650020778552054204",
        headers = {'User-Agent': chrome}
    ).json()
    return x

