import json

from core.logger import logger


class PassDBManager:
    @staticmethod
    def save_pass(website, email, password):
        new_data = {website.lower(): {"email": email, "password": password}}
        try:
            with open("./src/db/base/passwords.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError as Err:
            logger.error(Err)

        with open("./src/db/base/passwords.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    @staticmethod
    def delete_pass(website):
        try:
            with open("./src/db/base/passwords.json", "r") as data_file:
                data = json.load(data_file)
                if website.lower() in data:
                    del data[website.lower()]
        except FileNotFoundError as Err:
            logger.error(Err)

        with open("./src/db/base/passwords.json", "w") as data_file:
            json.dump(data, data_file, indent=4)

    @staticmethod
    def get_pass(website):
        try:
            with open("./src/db/base/passwords.json", "r") as data_file:
                data = json.load(data_file)
                creds = data.get(website.lower())
                if creds:
                    user_password = creds.get("password")
                    email_password = creds.get("email")
                    return email_password, user_password
                else:
                    return None, None

        except FileNotFoundError as Err:
            logger.error(Err)
            open("./src/db/base/passwords.json", "w").close()
