# Python the Language
Notes for python language itself.
## Table of Contents
- [Interesting Things About Class](#interesting-things-about-class)
- [Python Exceptions](#python-exceptions)
- [Slicing](#slicing)

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
print ('-'*5,A.printf)

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
##----- <function printff at 0x01795858>

```
And from this kind of behavior, I think I leart :
- The method defined in the class is called `bound method`.
- The function specificly assigned to the class later will become its `bound method` too. And **magically**, the name will change to the function's name. What's more, when I call `a.printff` ,it throw an error.
- The python interpreter treated built-in functions diffrently. Thus function `print` wound not become a `bound method`.
- After the function is assign to the instance, it would not become a `bound method`, but rather simply a function.
- ~~After a function is assign to the instance, the corresponding `bound method` in the class would magically change.~~
- After a function is assign to the instance, the **behavoir** when assigning functions again to an class would **magically** change.
- (Though I **really don't** know some of them ,I think I'd better put them down)

## Python Exceptions
I encountered this problem when writing `nb.py`. I wrote`except Exception:` instead of `except KeyboardInterrupt:` ,and it did not catch the KeyboardInterrupt as I expected. But now I figured out that KeyboardInterrupt is not included in Exception:
```shell
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
    +-- ...
	+-- ...
```

## Slicing
#### Here is a valid slice

```python
s='jksahgijsdhgedhjgkh'
print(s[5:999])

##Output
##gijsdhgedhjgkh
```

#### a valid way to create a slice
```python
a=slice(1,5,2)
print(a.start)
print(a.stop,a.step)

##Output
##1
##5 2
```
#### the invalid way
```python
a=[1:3:4]

##Output
##SyntaxError
```
#### cooperate with class
```python
class A:
    def __getitem__(self,arg):
	    print(arg)
		return 
a=A()
b=a[123,...,1:3:5,[1,2,3]]

##Output
##(123, Ellipsis, slice(1, 3, 5), [1, 2, 3])
```
