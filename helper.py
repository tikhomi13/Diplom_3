import faker


class FakeData:

    def fake_email(self):

        fake = faker.Faker()
        email = fake.email()

        return email


def get_sign_up_data():

    fake = faker.Faker()
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return name, email, password
