
import subprocess
def beautifulPrint(sayHello):
    def func(name):
        print "*"*50
        sayHello(name)

    return func

@beautifulPrint
def sayHello(name):
    print "hello %s"% name


sayHello("hu")

