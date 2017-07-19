
from random import seed
import forgery_py



def generateLine():
    email=forgery_py.internet.email_address()
    username=forgery_py.internet.user_name(True)
    password=forgery_py.lorem_ipsum.word()
    name=forgery_py.name.full_name()
    location=forgery_py.address.city()
    # about_me=forgery_py.lorem_ipsum.sentence()
    member_since=forgery_py.date.date(True)
    line="{email} {username} {password} {name} {location} {member_since}" .format (
        email=email,username=username,password=password,name=name,location=location,
        member_since=member_since
    )
    return str(line)

def makeData(count=10):
    while(count>0):
        line=generateLine()
        print line
        count=count-1

makeData(1000)
# generateLine()