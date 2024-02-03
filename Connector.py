import httpx
import time
import json
from datetime import datetime

# HTTPX object
limits = httpx.Limits(max_keepalive_connections=35, max_connections=77)
timeout = httpx.Timeout(10.0, read=None)
super_httpx = httpx.Client(limits=limits, timeout=timeout)
# HTTPX

def get_data(headers, endp_url, params):

    start = time.time()
    endpoint_data = super_http.get(url=endp_url, headers=headers, params=params)
    roundtrip = time.time() - start

    if endpoint_data.status_code == 429:

        dt_object = datetime.fromtimestamp(int(endpoint_data.headers.get('x-organization-rate-limit-reset'))) - datetime.now()
        time.sleep(dt_object.seconds + 1)
        endpoint_data = super_http.get(url=endp_url, headers=headers, params=params)

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))
        return endpoint_data.json()

    elif endpoint_data.status_code == 400:

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))

        return endpoint_data.json()
    
    elif endpoint_data.status_code == 200:

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))
        #print("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))

        return endpoint_data.json()

    else:

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))
        print("status code: ", endpoint_data.status_code)
        return endpoint_data.json()
    

def post_data(headers, endp_url, payload):

    start = time.time()
    endpoint_data = super_http.post(url=endp_url, headers=headers, data=payload)
    roundtrip = time.time() - start

    if endpoint_data.status_code == 429:

        dt_object = datetime.fromtimestamp(int(endpoint_data.headers.get('x-organization-rate-limit-reset'))) - datetime.now()
        time.sleep(dt_object.seconds + 1)
        endpoint_data = super_http.post(url=endp_url, headers=headers, data=payload)

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))
        return endpoint_data.status_code

    elif endpoint_data.status_code == 403:

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))

        return endpoint_data.status_code
    
    elif endpoint_data.status_code == 200 or endpoint_data.status_code == 201:

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))
        #print("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))

        return endpoint_data.status_code

    else:

        #logging.info("Status Code " + str(endpoint_data.status_code) + ": " + endp_url + " time: " + str(roundtrip))
        print("status code: ", endpoint_data.status_code)
        return endpoint_data.status_code