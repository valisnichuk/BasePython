# class Foo:
#     """My klass class"""
#     bar = True
#
#     # def echo_name(self):
#     #     print(self.__class__.__name__)
#
#     @classmethod
#     def echo_name(cls):
#         print(cls.__name__)
#
#     # @staticmethod
#     # def echo_name():
#     #     print(klass.__name__)

def print_class_demo(klass):
    
    f = klass()
    print(klass, klass.__class__, type(klass))
    print(f, f.__class__, type(f))

    print('class', klass.echo_name())
    print('inst', f.echo_bar())
    print(klass.bar, f.bar)

    f.bar = False
    print(klass.bar, f.bar)

    f.bar = True
    klass.bar = False
    f2 = klass()
    f2.echo_bar()
    print(klass.bar, f.bar, f2.bar)

@classmethod
def echo_name(cls):
    print(cls.__name__)

def echo_bar(self):
    print(self.bar)

# Foo = type('Foo', (), {'bar': True, 'echo_name': echo_name, 'echo_bar': echo_bar})
# NewFoo = type('NewFoo', (Foo, ), {'spam': 'eggs'} )
#
# print(NewFoo)
# nf = NewFoo()
# print(nf)
# print(nf.spam)
# print(nf.bar)
# print(nf.echo_name())

# print_class_demo(Foo)

class MyMetaclass(type):
    def __new__(cls, name, bases, dct, *args, **kwargs):
        print('New class', name)
        print('Bases:', bases)
        dct['SPAM'] = 'EGGS'
        print('New attrs:', dct)
        # for k in dct.keys():
        #     if k.startswith('__'):
        #         v = dct.pop(k)
        #         dct[k.upper()] = v

        new_cls = super().__new__(cls, name, bases, dct, *args, **kwargs)
        print('created new cls:', new_cls)
        return new_cls

# class Foo(metaclass=MyMetaclass):
#     bar = True
#     __secret_attr = 'secret value'
#
#     @classmethod
#     def echo_name(cls):
#         print(cls.__name__)
#
#     def echo_bar(self):
#         print(self.bar)
#
# class NewFoo(Foo):
#     spam = 'eggs'

class BaseUser:
    is_staff = False
    is_admin = False

class User(BaseUser):
    pass

class Admin(BaseUser):
    is_staff = True
    is_admin = True


# пояснение псведокодом
# MyClass = MyMetaClass()
# my_instance = MyClass()

# Foo = MyMetaclass('Foo', (), {})
# NewFoo = MyMetaclass('NewFoo', (Foo, ), {'spam': 'eggs'})
# print(Foo.SPAM)
# print(NewFoo.SPAM)
# f = Foo()
# Foo.echo_bar(f)
# f.echo_bar()
# nf = NewFoo()
# print(f, f.SPAM)
# print(nf, nf.SPAM)


from abc import ABCMeta, abstractmethod, abstractclassmethod

class FileManagerABC(metaclass=ABCMeta):

    @abstractmethod
    def read_file(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def write_to_file(self, text: str) -> int:
        ...

    @abstractmethod
    def close(self) -> None:
        """
        Closing file
        :return:
        """

class FileManager(FileManagerABC):
    def __init__(self, filename: str):
        self._f = open(filename, "a+")

    def read_file(self) -> str:
        text = self._f.read()
        self._f.seek(0)
        return text

    def write_to_file(self, text: str) -> int:
        count = self._f.write(text)
        print('written text', text)
        return count

    def close(self) -> None:
        print("closing", self._f)
        self._f.close()

file_manager = FileManager('file.txt')
print(file_manager.read_file())
print(file_manager.write_to_file('\nhello again'))

file_manager.close()