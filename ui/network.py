import requests

API_BASE_URL = "https://pyquad-peak-api.herokuapp.com/"
PING_ENDPOINT = "ping"
LOGS_ENDPOINT = "get_logs"

def ping_url(url):
    return requests.get(
        f"{API_BASE_URL}{PING_ENDPOINT}",
        params={"url": url}
    ).json()

def get_logs(url):
    return requests.get(
        f"{API_BASE_URL}{LOGS_ENDPOINT}",
        params={"url": url}
    ).json()
