from urllib import error, request

import json


URL = "https://ep.api.getfastah.com/whereis/json/{}"


def fetch_details(ip, token):
    url = URL.format(ip)
    headers = {'Fastah-Key': token}
    req = request.Request(url, headers=headers)
    response = None

    try:
        with request.urlopen(req) as connection:
            response = connection.read()
            return response.decode()
    except error.HTTPError as e:
        if e.code in [400, 404]:
            print("IP address {} is invalid.".format(ip))
        elif e.code == 401:
            print("Token : {} is invalid.".format(token))
        else:
            print("Invalid response received from the server.")
        print(e.reason)
    except error.URLError as e:
        custom_message = ('Problem while making connection.'
                          'Please check the Internet connection')
        print(e.message)
        print(custom_message)


def fetch_multiple_details(ips, token):
    ips = set(ips)
    responses = []
    for ip in ips:
        response = fetch_details(ip, token)
        if response:
            response = json.loads(response)
            responses.append({ip: response})
        else:
            return None
    return responses
