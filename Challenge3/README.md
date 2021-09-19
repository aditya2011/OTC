# Challenge3

We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
Example Inputs
object = '{"a":{"b":{"c":"d"}}}'
key = a/b/c
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a

# nestedobj

nestedobj python program will take the input as string object, where we need to extract the key and value, for example:

**Key** is the combination of keys with the '/' 

if object = {“a”:{“b”:{“c”:”d”}}}

key will be **a/b/c**

**Value** is the last value of object, for example:

if object = {“a”:{“b”:{“c”:”d”}}}

value will be **d**


```
python3  nestedobj.py
```


**Tests**

1. First Test:

```
inputstring = {“a”:{“b”:{“c”:”d”}}}
```

**Output**
Key -> a/b/c, Value -> d

2. Second Test:

```
inputstring = {"x":{"y":{"z":"a"}}}
```

**Output**
Key -> x/y/z, Value -> a
