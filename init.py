import requests
import ping3


def https_request(URL):
    request = requests.get(URL)


    return(request.status_code)


print(https_request("https://google.com/"))