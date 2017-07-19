# coding=utf-8
__author__ = 'zenith'

import ConfigParser as cp

path = 'D:\\authz'
c = cp.ConfigParser()
c.read(path)
if not c.has_section('users'):
    c.add_section('users')

print(c.sections())

c.set('users','zenith','4433')


print(c.options('users'))
print(c.items('users'))

print(c.get('users','zenith'))


#c.remove_section('users')
#c.remove_option('users','zenith')
c.write(open(path, 'w'))
