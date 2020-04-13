class SingletonExample(object):
    __instance = None
    def __call__(cls,*args,**kw):
        if not cls.__instance:
            cls.__instance = super(SingletonExample,cls).__call__(*args,**kw)
class Singleton(object):
    __metaclass__ = SingletonExample
    
    def do_something(self):
        print("This is a Singleton Design Pattern")

s = Singleton()
s.do_something()