import time


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class CurrenciesList(metaclass = Singleton):

    def __init__(self, currencies_ids_lst = None):
        self.__cur_ids_lst = currencies_ids_lst
        self.__exec_time = None
        self._link = "http://www.cbr.ru/scripts/XML_daily.asp"
        print(self.get_currencies())

    def get_currencies(self) -> dict:
        if (self.__exec_time == None) or (time.time() - self.__exec_time > 5):
            self.__exec_time = time.time()
            return self.__action()
        else:
            print("Wait 5 seconds")
            time.sleep(5)
            self.__exec_time = time.time()
            return self.__action()

    def __action(self):
        import requests
        from xml.etree import ElementTree as ET
        cur_res_str = requests.get(self._link)
        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")

        result = {}

        if self.__cur_ids_lst is None:
            self.__cur_ids_lst = ['R01010']
        
        for _v in valutes:
            valute_id = _v.get('ID')

            if str(valute_id) in self.__cur_ids_lst:
                valute_cur_val = _v.find('Value').text
                valute_cur_name = _v.find('Name').text

                result[valute_id] = (valute_cur_val, valute_cur_name)
        return result


curlst = CurrenciesList(['R01090B'])
time.sleep(5)
print(curlst.get_currencies())