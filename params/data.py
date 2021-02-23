import random
import string


class Email:
    def __init__(self, email_subject, email_to, email_body):
        self.email_subject = email_subject
        self.email_to = email_to
        self.email_body = email_body


def random_string():
    letters = string.ascii_lowercase
    return (''.join(random.choice(letters) for i in range(10)))


test_data = [Email(email_to="aqa.engineer.test.alekseev.ms@gmail.com", email_subject=random_string(),
                   email_body=random_string()),
             Email(email_to="aqa.engineer.test.alekseev.ms@gmail.com", email_subject=random_string(),
                   email_body='')]
