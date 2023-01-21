import requests

#   Zwaraca podaną wartosci w złotówkach
def to_pln(ammount: int, currency: str):
    pln_req = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/" + currency + "?format=json")
    pln_req_data = pln_req.json()
    pln_value = pln_req_data['rates'][0]['mid']
    pln_value = round(pln_value, 2)

    return round(ammount * pln_value, 2 )

#   Zwraca podajną wartość w podenej walucie względem złotówki
def from_pln(ammount: int, currency: str):
    pln_req = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/" + currency + "?format=json")
    pln_req_data = pln_req.json()
    pln_value = pln_req_data['rates'][0]['mid']
    pln_value = round(pln_value, 2)

    return round(ammount / pln_value, 2 )

#   Zwraca podaną wartość drugiej waluty względem pierwszej 
def convert(ammount: int, from_curr: str, to_curr: str):
    usd_to_pln = to_pln(1, from_curr)
    req = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/" + to_curr + "?format=json")
    req_data = req.json()
    value = req_data['rates'][0]['mid']
    value = round(value, 2)

    return round((ammount * usd_to_pln) / value, 2)

