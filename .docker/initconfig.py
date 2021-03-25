import os
import json


def main():
    """
    Creates a config file using docker environment variables
    """

    # Create Config
    telegram_bot_token = os.environ["1694554252:AAE_D4Wp2fJ5HxQUl7YAnd1SyQbL36a9hGw"]
    update_interval = os.environ["UPDATE_INTERVAL"]

    config = {}
    config["telegram_token"] = telegram_bot_token
    config["update_interval"] = update_interval

    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    filepath = os.path.join(base_path, "resources/credentials.json")

    with open(filepath, 'w+') as outfile:
        json.dump(config, outfile)


if __name__ == '__main__':
    main()
