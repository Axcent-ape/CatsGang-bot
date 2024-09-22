# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'

DELAYS = {
    "REUPLOAD": [50, 100], #delay after a upload attempt
    "RELOGIN": [5, 10],  # delay after a login attempt
    'ACCOUNT': [50, 150],  # delay between connections to accounts (the more accounts, the longer the delay)
    'TASK':  [5, 10],  # delay after complete task
}

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "http",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "http"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

IMAGE_FOLDER_PATH = 'data/img'

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
