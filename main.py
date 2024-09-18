import asyncio
import os
from data import config
from utils.core.file_manager import get_images_from_folder
from utils.core.telegram import Accounts
from utils.starter import start, stats

async def main():
    print("Soft's author: https://t.me/ApeCryptor\n")
    action = int(input("Select action:\n0. About soft\n1. Start soft\n2. Get statistics\n3. Create sessions\n\n> "))

    if action == 0:
        print(config.SOFT_INFO)
        return

    if not os.path.exists(config.WORKDIR):
        os.mkdir(config.WORKDIR)

    if config.PROXY['USE_PROXY_FROM_FILE']:
        if not os.path.exists(config.PROXY['PROXY_PATH']):
            with open(config.PROXY['PROXY_PATH'], 'w') as f:
                f.write("")
    else:
        if not os.path.exists(os.path.join(config.WORKDIR, 'accounts.json')):
            with open(os.path.join(config.WORKDIR, 'accounts.json'), 'w') as f:
                f.write("[]")

    if action == 3:
        await Accounts().create_sessions()

    if action == 2:
        await stats()

    if action == 1:
        folder_path = config.IMAGE_FOLDER_PATH
        images = get_images_from_folder(folder_path)

        accounts = await Accounts().get_accounts()
        tasks = []

        for thread, account in enumerate(accounts):
            session_name, phone_number, proxy = account.values()
            tasks.append(asyncio.create_task(start(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy, images=images)))

        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
