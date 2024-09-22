import random
from utils.cats_gang import CatsGang
from data import config
from utils.core import logger
import datetime
import pandas as pd
from utils.core.telegram import Accounts
import asyncio
import os


async def start(thread: int, session_name: str, phone_number: str, proxy: [str, None], images: [list, None]): # type: ignore
    while True:
        random.shuffle(images)
        
        cats = CatsGang(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy, images=images)
        account = session_name + '.session'

        await asyncio.sleep(random.uniform(*config.DELAYS['ACCOUNT']))

        try:
            attempts = 3
            while attempts:
                try:
                    await cats.login()
                    logger.success(f"Thread {thread} | {account} | Login")
                    break
                except Exception as e:
                    logger.error(f"Thread {thread} | {account} | Left login attempts: {attempts}, error: {e}")
                    await asyncio.sleep(random.uniform(*config.DELAYS['RELOGIN']))
                    attempts -= 1
            else:
                logger.error(f"Thread {thread} | {account} | Couldn't login")
                return

            attempts = 10
            while attempts:
                logger.info(f"Thread {thread} | {account} | Upload avatar attempts left {attempts}")
                try:
                    await cats.upload_avatar()
                    break
                except:
                    await asyncio.sleep(random.uniform(*config.DELAYS['REUPLOAD']))
                    attempts -= 1

            for task in await cats.get_tasks():
                if task['completed'] or task['title'] in config.BLACKLIST_TASKS:
                    continue

                if task['type'] == 'OPEN_LINK':
                    if await cats.complete_task(task_id=task['id']):
                        logger.success(f"Thread {thread} | {account} | Completed task «{task['title']}» and got {task['rewardPoints']} CATS")
                    else:
                        logger.warning(f"Thread {thread} | {account} | Couldn't complete task «{task['title']}»")

                elif task['type'] == 'SUBSCRIBE_TO_CHANNEL' and task['allowCheck']:
                    if await cats.check_task(task_id=task['id']):
                        logger.success(f"Thread {thread} | {account} | Completed task «{task['title']}» and got {task['rewardPoints']} CATS")
                    else:
                        logger.warning(f"Thread {thread} | {account} | Couldn't complete task «{task['title']}»")

                else:
                    continue
                await asyncio.sleep(random.uniform(*config.DELAYS['TASK']))

        finally:
            await cats.logout()
            logger.info(f"Thread {thread} | {account} | Logged out and session closed")

        logger.info(f"Thread {thread} | {account} | Waiting 24 hours before next execution")
        await asyncio.sleep(86400)  # Задержка в 24 часа (86400 секунд)


async def stats():
    accounts = await Accounts().get_accounts()

    tasks = []
    for thread, account in enumerate(accounts):
        session_name, phone_number, proxy = account.values()
        tasks.append(asyncio.create_task(CatsGang(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy).stats()))

    data = await asyncio.gather(*tasks)
    path = f"statistics/statistics_{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.csv"
    columns = ['Phone number', 'Name', 'balance', 'leaderboard', 'referral_link', 'Proxy (login:password@ip:port)']

    if not os.path.exists('statistics'): os.mkdir('statistics')
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(path, index=False, encoding='utf-8-sig')

    logger.success(f"Saved statistics to {path}")
