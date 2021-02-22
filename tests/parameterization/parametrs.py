from os import environ


class Parameters:

    @staticmethod
    def webdriver_url():
        return environ["WD_URL"]

    @staticmethod
    def webdriver_platform():
        return environ["WD_PLATFORM"]

    @staticmethod
    def webdriver_browser():
        return environ["WD_BROWSER"]

    @staticmethod
    def webdriver_version():
        return environ["WD_BROWSER_VERSION"]

    @staticmethod
    def gmail_url():
        return environ["GMAIL_URL"]

    @staticmethod
    def gmail_username():
        return environ["GMAIL_USERNAME"]

    @staticmethod
    def gmail_password():
        return environ["GMAIL_PASSWORD"]

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
