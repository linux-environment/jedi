# -----------------
# for loops
# -----------------

for a in [1,2]:
    #? ['real']
    a.real

for a1 in 1,"":
    #? ['real']
    a1.real
    #? ['upper']
    a1.upper

for a3, b3 in (1,""), (1,""), (1,""):
    #? ['real']
    a3.real
    #? []
    a3.upper
    #? []
    b3.real
    #? ['upper']
    b3.upper

for a4, (b4, c4) in (1,("", list)), (1,("", list)):
    #? ['real']
    a4.real
    #? []
    a4.upper
    #? []
    b4.real
    #? ['upper']
    b4.upper
    #? []
    c4.real
    #? ['append']
    c4.append
    #? []
    c4.upper

# -----------------
# list comprehensions
# -----------------

a = ['' for abc in [1]]

#? str()
a[0]


# -----------------
# ternary operator
# -----------------

a = 3
b = '' if a else set()
#? str() set()
b

def ret(a):
    return ['' if a else set()]

#? str() set()
ret(1)[0]
#? str() set()
ret()[0]

# -----------------
# with statements
# -----------------

with open('') as f:
    #? ['closed']
    f.closed

with open('') as f1, open('') as f2:
    #? ['closed']
    f1.closed
    #? ['closed']
    f2.closed


# -----------------
# global vars
# -----------------

def global_define():
    global global_var_in_func
    global_var_in_func = 3

#? int()
global_var_in_func
