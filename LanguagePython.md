# Python the Language
Notes for python language itself.
## Table of Contents
- [Interesting Things About Class](interesting-things-about-class)
## Interesting Things About Class
Let's have a look at the following code first:
```python
class A:
    def printf(*args):
        print(args)
def printff(*args):
    print(args)

a=A()
a.printf()
print ('-'*5,a.printf)

A.printf=printff
a.printf()
print ('-'*5,a.printf)

A.printf=print
a.printf()
print ('-'*5,a.printf)

a.printf=printff
a.printf()
print ('-'*5,a.printf)

A.printf=printff
a.printf()
print ('-'*5,a.printf)

##Output
##(<__main__.A object at 0x01371070>,)
##----- <bound method A.printf of <__main__.A object at 0x01371070>>
##(<__main__.A object at 0x01371070>,)
##----- <bound method A.printff of <__main__.A object at 0x01371070>>
##
##----- <built-in function print>
##()
##----- <function printff at 0x01795858>
##()
##----- <function printff at 0x01795858>
```
