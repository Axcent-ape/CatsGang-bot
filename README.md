# CatsGang-bot
Soft for https://t.me/catsgang_bot

More crypto themes and softs in telegram: [ApeCryptor](https://t.me/+_xCNXumUNWJkYjAy "ApeCryptor") 🦧

## Functionality
| Functional                                                     | Supported |
|----------------------------------------------------------------|:---------:|
| Multithreading                                                 |     ✅     |
| Binding a proxy to a session                                   |     ✅     |
| r; auto-reger; complete tasks,                         |     ✅     |
| Random sleep time between accounts                             |     ✅     |
| Support pyrogram .session                                      |     ✅     |
| Get statistics for all accounts                                |     ✅     |

## Settings data/config.py
| Setting                      | Description                                                                                    |
|------------------------------|------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**        | Platform data from which to launch a Telegram session _(stock - Android)_                      |
| **DELAYS-ACCOUNT**           | Delay between connections to accounts (the more accounts, the longer the delay) _(eg [5, 15])_ |
| **PROXY_TYPES-TG**           | Proxy type for telegram session _(eg 'socks5')_                                                |
| **PROXY_TYPES-REQUESTS**     | Proxy type for requests _(eg 'socks5')_                                                |
| **WORKDIR**                  | directory with session _(eg "sessions/")_                                                      |
| **TIMEOUT**                  | timeout in seconds for checking accounts on valid _(eg 30)_                                    |

## Requirements
- Python 3.9 (you can install it [here](https://www.python.org/downloads/release/python-390/)) 
- Telegram API_ID and API_HASH (you can get them [here](https://my.telegram.org/auth))

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the bot:
   ```bash
   python main.py
   ```
