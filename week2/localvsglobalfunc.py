def hello(): # This is the global variable.
    global o
    o = 'hi'

def bell():  # This is local variable.
    o = 'bye'

def prime():  #this is global variable.
   print(o)


eggs = 'global' #this is global variable.
hello()
print(o)