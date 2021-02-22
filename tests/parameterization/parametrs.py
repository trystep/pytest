from os import environ


class Parameters:

    @staticmethod
    def webdriver_url():
        return environ["WD_URL"] if "WD_URL" in environ else "http://selenium:4444/wd/hub"

    @staticmethod
    def webdriver_platform():
        return environ["WD_PLATFORM"] if "WD_PLATFORM" in environ else "linux"

    @staticmethod
    def webdriver_browser():
        return environ["WD_BROWSER"] if "WD_BROWSER" in environ else "chrome"

    @staticmethod
    def webdriver_version():
        return environ["WD_BROWSER_VERSION"] if "WD_BROWSER_VERSION" in environ else 88

    @staticmethod
    def gmail_url():
        return environ["GMAIL_URL"] if "GMAIL_URL" in environ else "https://gmail.com"

    @staticmethod
    def gmail_username():
        return environ["GMAIL_USERNAME"] if "GMAIL_USERNAME" in environ else "aqa.engineer.test.alekseev.ms"

    @staticmethod
    def gmail_password():
        return environ["GMAIL_PASSWORD"] if "GMAIL_PASSWORD" in environ else "webcreateaccount1"

    @staticmethod
    def gmail_message_to():
        return Parameters.gmail_username()

    @staticmethod
    def gmail_message_subject():
        return "Тестовое задание Алексеев М.С."

    @staticmethod
    def gmail_message_body():
        return "Анекдот 'Чем отличается TCP от UDP?'" \
               "Если ты не поймешь с первого раза, что такое TCP, то я объясню тебе еще раз." \
               "А если ты не поймешь с первого раза, что такое UDP, то я не буду тебе объяснять."
