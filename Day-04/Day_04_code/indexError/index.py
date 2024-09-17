# Python IndexError
# You may sometimes get an IndexError such as the following when running your code:

# IndexError: list index out of range
# What does it mean?
# An IndexError means that your code is trying to access an index that is invalid. This is usually because the index goes out of bounds by being too large.

# For example, if you have a list with three items and you try to access the fourth item, you will get an IndexError.

# This can happen with strings, tuples, lists, and generally any object that is indexable.

# Which line causes it?
# Typically, Python will tell you which line is causing the error. For example:

# Traceback (most recent call last):
#   File "/tmp/pyrunnerj1Bs76Cx/code.py", line 3, in
#     print(xs[2])
# IndexError: list index out of range
# It can be helpful to read the error message carefully, paying special attention to the highlighted line.

# Common causes
# Typically the cause of an IndexError is that you forgot that indexing starts at 0 in Python.

# So if you have a list with two items:

# Then letters[0] is the first item, letters[1] is the last item, 
# and letters[2] goes out of bounds and causes an IndexError, just like Example below.
letters = ["A", "B"]
print(letters[0, 1])
print(letters[2])

# Debugging
# It can be useful to add in a call to print right before the offending line,
# so you can see the object you are indexing into. If the index is a variable,
# you can also print that. This way you can see precisely what's going on in your code.