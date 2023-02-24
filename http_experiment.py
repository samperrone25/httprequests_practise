import requests
import http # for CONNECT and TRACE methods not supported by 'requests'

# requests are sent to httpbin.org which returns the requests parameters in the reponse body

def get():
    # GET

    # adding GET URL params to request
    # params_dict = {"sample_param1" : 400, "sample_param2" : "Jimmy"} # places params within get url as https://www.python.org:443/?sample_param1=400
    # get_response = requests.get("https://www.python.org:443", params=params_dict)

    # demonstrating redirection
    get_redirected_response = requests.get("http://www.python.org:80/") # python will automatically redirect to https, to disable redirection, requests.get(URL, allow_redirects=False)
    print(get_redirected_response.history) # history will show this, note the HTTP 301 Moved Permanently
    print("##########################################")
    # regular get request
    get_response = requests.get("https://www.python.org:443/")
    print(get_response.text)
    print("##########################################")
    #print(get_response.content) # prints body response as binary not text

def head():
    # HEAD
    head_response = requests.head("https://www.python.org:443")
    print(head_response.text) # head request, should be empty
    print("##########################################")

def post():

    # POST
    headers_dict = {"user-agent" : "jimmy/0.1"} # changing headers (e.g. user-agent)
    post_response = requests.post("https://httpbin.org/post", headers=headers_dict)
    #post_response = requests.post("https://httpbin.org/post")
    print(post_response.text)
    print("##########################################")

def put():
    # PUT
    payload = {"key1" : "value1"}
    put_response1 = requests.put('https://httpbin.org/put', data=payload) # regular payload
    print(put_response1.text)
    print("##########################################")
    put_response2 = requests.put('https://httpbin.org/put', json=payload) # JSON payload, changes content-type to application/json
    print(put_response2.text)
    print("##########################################")
    print("Response status code:")
    print(put_response2.status_code)
    print("Response JSON:")
    print(put_response2.json)
    print("Response headers:")
    print(put_response2.headers)
    print("Original Request body:")
    print(put_response2.request.body)
    print("##########################################")

# DELETE
#r = requests.delete('https://httpbin.org/delete')

# CONNECT
def connect():
    # can't be done in requests lib, using python http.client library instead
    # requests that the recipient establishes a tunnel to the destination origin server and once established, blindly forward data in both directions until tunnel closure

    h1 = http.client.HTTPConnection("www.httpbin.org:80")
    print(h1)
    h1.request("CONNECT", "/", headers={"Host" : "www.python.org:80"})
    r1 = h1.getresponse()
    print(r1.status, r1.reason)
    print(r1.headers)
    print("##########################################")
    text = r1.read()
    print(text) # 405 CONNECT method not allowed at www.httpbin.org:80
    print("##########################################")

    # example CONNECT request

    # CONNECT tunnel_destination_url:port HTTP/1.1
    # Host: tunnel_destination_url:port
    # Example-Proxy-Auth: basic aGVsbG86d29ybGQ=

    # only a 2xx response indicates that the tunnel was created

# OPTIONS
def options():
    response = requests.options('http://httpbin.org/get')
    print(response.headers)
    print("##########################################")
    print(response.text)
    print("##########################################")

# TRACE
def trace():
    # can't be done in requests lib, using python http.client library instead
    # requests that the recipient establishes a tunnel to the destination origin server and once established, blindly forward data in both directions until tunnel closure

    h1 = http.client.HTTPConnection("www.httpbin.org:80")
    print(h1)
    h1.request("TRACE", "/")
    r1 = h1.getresponse()
    print(r1.status, r1.reason) # 405 not allowed : (
    print(r1.headers)
    print("##########################################")
    text = r1.read()
    print(text) #
    print("##########################################")

if __name__ == "__main__":
    # change as needed
    #put()
    #get()
    #options()
    #connect()
    trace()