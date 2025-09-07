from faker import Faker
import random

faker = Faker()

class TestData:
    @staticmethod
    def random_email(domain = "luisxyz.com"):
        return faker.user_name() + "@" + domain
    
    @staticmethod
    def random_first_name():
        return faker.first_name()
    
    @staticmethod
    def random_last_name():
        return faker.last_name()
    
    @staticmethod
    def random_company():
        return faker.company()
    
    @staticmethod
    def randon_phone():
        return faker.phone_number()
    
    @staticmethod
    def random_title():
        return f"Title_{faker.word()}"