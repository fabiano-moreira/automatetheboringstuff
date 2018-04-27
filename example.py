def hello(): #Uses the def statement to define a function call hello
    print ('Howdy!')
    print ('Howdy!!')
    print ('Hello there.')

hello()
hello()
hello()

###########################

def plusOne (number):
    return number + 1

newNumber = plusOne (5)
print(newNumber)


##########################

print ('Hello', end='')
print ('world')


############################

spam = 42 # Global Variable

def eggs():
    spam = 42 # Local Variable

print ('Some code here.')
print ('Some more code.')

##############

def spam(): 
    eggs = 99 # Local Variable
    bacon()
    print (eggs)

def bacon():
    ham = 101
    eggs = 0 # Local Variable

spam()

#################

def spam(): 
    eggs = 'Hello world'
    print (eggs)


eggs = 42
spam()
print(eggs)
