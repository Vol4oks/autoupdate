mask_yaml = "_auto.yaml"
name_env = ".env"

def generate_env():
    res = input("Create config for telegram bot? [y/n]: ").lower().strip()
    if res == 'y':
        bot_token =  input("input bot token: ")
        user_id = input("input user_id: ")
        file = [
                f'BOT_TOKEN={bot_token}\n',
                f'ADMINS={user_id}\n',
                'WORK_BOT=true\n',
            ]
    else:
        file = [
                'BOT_TOKEN=\n',
                'ADMINS=\n',
                'WORK_BOT=false\n',
            ]
    with open(".env", "w") as f:
            f.writelines(file)
