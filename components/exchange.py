import requests


def transform_currency(amount, from_currency, to_currency):
    rate = get_rate(from_currency + "-" + to_currency)
    return amount * rate


# get the exchage rate
def get_rate(id="MXN-BRL"):
    url = "https://economia.awesomeapi.com.br/last/" + id
    response = requests.get(url)
    data = response.json()
    data_id = id.replace("-", "")
    rate = data[data_id]["bid"]
    return float(rate)

