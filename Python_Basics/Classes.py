
class MyClass:
    def method1(self):
        print('method 1')

    def method2(self, hello):
        print('method 2 ' + hello)


# class AnotherMyClass inherit class MyClass
class AnotherMyClass(MyClass):
    # call inherited function from super class (MyClass)
    def method1(self):
        MyClass.method1(self)
        print('another method 1')

    # overwrite the function method2
    def method2(self, hello):
        print('another method 2 ')


def main():
    c = MyClass()
    c.method1()
    c.method2('hello')

    c2 = AnotherMyClass()
    c2.method1()
    c2.method2("hello world")


if __name__ == '__main__':
    main()
