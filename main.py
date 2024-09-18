#Завдання 2
import inspect


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

#Завдання 3

#hasattr()
print('Is here my email:', hasattr(contact1, 'emal'))
print('Is here my year of birth', hasattr(contact1, 'year_of_birth'))

#getattr:

name = getattr(contact1, 'name')
print(name)

year_of_birth = getattr(contact1, 'year_of_birth', 'None')
print(year_of_birth)

#setattr:
setattr(contact1, 'name', 'Ivan')
print(f'New name:{contact1.name}')

#delattr
# delattr(contact1, 'job')
# print(contact1.job) #Error

#Завдання 4

contact_base = Contact('Dmytro', 25, 380572442213, 'qwertyoiop@gmail.com')
contact_child = UpdateContact('Petrov','Dmytro', 25, 380572442213, 'qwertyoiop@gmail.com', 'Python data scientist')

print(isinstance(contact_base, Contact))
print(issubclass(Contact, UpdateContact))

print(isinstance(contact_child, UpdateContact))
print(issubclass(UpdateContact, Contact))

#Завдання 5
print(f'Info of contact_base:{dir(contact_base)}')
print(f'Info of contact_child:{dir(contact_child)}')

delattr(contact_child, 'job')
print(f'New contact_child:{dir(contact_child)}')

#Завдання 6

for method in inspect.getmembers(Contact):
    print(f'Methods in Contact class:{method}')

for new_method in inspect.getmembers(Contact):
    print(f'Methods in UpdateContact class:{new_method}')