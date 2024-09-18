class Contact:
    def __init__(self, name: str, age: int, mob_phone: int, email: str):
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def __str__(self):
        return f'Name: {self.name}, {self.age} years old. Phone: {self.mob_phone}, email:{self.email}'

class UpdateContact(Contact):
    def __init__(self, surname: str, name: str, age: int, mob_phone: int, email: str, job: str):
        super().__init__(name, age, mob_phone, email)
        self.surname = surname
        self.job = job

    def get_message(self):
        return (f'{self.surname} {self.name}, you got a new message to {self.mob_phone} and to email:{self.email}.'
                f' It`s about your job: {self.job}')


contact = Contact('Oleh',20, 38057843213, 'qwerty123@gmail.com')
print(contact)
contact1 = UpdateContact('Yemelianov','Oleh',20, 38057843213,'qwerty123@gmail.com','Python backend developer')
print(contact1.get_message())

print(contact1.__dict__)
print(UpdateContact.__base__)
print(UpdateContact.__bases__)