# list
actual list :- [1, 2, 3, 'sai', 'gbaar', 2]
use remove method to remove value :-  [1, 3, 'sai', 'gbaar', 2]
remove method with index to remove value  [1, 'sai', 'gbaar', 2]
l.remove(9)
    ~~~~~~~~^^^
ValueError: list.remove(x): x not in list
l.remove(l[1],2)
    ~~~~~~~~^^^^^^^^
TypeError: list.remove() takes exactly one argument (2 given)

list which pop given index value :-  [1, 2, 'sai', 'gbaar', 2]
list where pop index is not given last index value :- [1, 2, 'sai', 'gbaar']
Traceback (most recent call last):
  File "c:\Users\Admin\Desktop\workplace\homework\homework4.py", line 24, in <module>
    l.pop(l[1],2)
    ~~~~~^^^^^^^^
TypeError: pop expected at most 1 argument, got 2
