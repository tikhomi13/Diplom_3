import faker
from data import URLs


def generator(): # теперь лишнее

    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return name, email, password






def get_email_and_password(email, password):

    my_email = email
    my_password = password

def generate_user_data():

    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()

  #  name, email, password = get_sign_up_data()

    payload = {
        'name': name,
        'email': email,
        'password': password

    }

    return payload



