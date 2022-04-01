import requests

# account credentials
user_name = "o_7l50rru47r"
pass_word = "asdfghjkl123"

# enter the url you want to shorten
URL = "https://www.linkedin.com/in/abhiram-kattunga-821426204"

# get the access token
authen_req = requests.post("https://api-ssl.bitly.com/oauth/access_token",auth=(user_name,pass_word))
if authen_req.status_code == 200:
    # if response is OK, get the access token
    access_token = authen_req.content.decode()
    print("[!] Got access token: ", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()

"""
We used requests.post() method to make a POST request to /oauth/access_token endpoint and obtain our access token. We passed auth parameter to add our account credentials to the request headers.

Now we have our access token, before we dive into shortening URLs, we first need to get the group UID associated with our Bitly account
"""
# Construct the request headers with authorization
headers = {"Authorization": f"Bearer {access_token}"}

# get the group UID associated with our account
group_req = requests.get("https://api-ssl.bitly.com/v4/groups", headers=headers)
if group_req.status_code == 200:
    # if response is OK, get theG UID
    group_data = group_req.json()['groups'][0]
    guid = group_data['guid']
else:
    print("[!] Cannot get GUID, exiting...")
    exit()

"""
Now that we have guid, let's make our request to shorten an example URL:
"""

# make the post request to get shortened url for 'URL'
short_req = requests.post("https://api-ssl.bitly.com/v4/shorten", json={"group_guid": guid, "long_url": URL}, headers=headers)
if short_req.status_code == 200:
    # if responsse is OK, get the shortened URL
    link = short_req.json().get("link")
    print("Shortened URL: ",link)

"""
We're sending a POST request to /v4/shorten endpoint to shorten our url, we passed the group_guid of our account and the url we want to shorten as the body of the request.

We used json parameter instead of data in requests.post() method to automatically encode our Python dictionary into JSON format and send it with Content-Type as application/json, we then added the headers to contain the authorization token we grabbed earlier.
"""