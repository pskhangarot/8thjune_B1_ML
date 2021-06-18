############################################################################################################### 
#############                             Practice Set 1                                     ##################
###############################################################################################################

### Question 2


print(5**9)
print(3//2)
print(7//3)
print(7/3)
print(6 == 6)
a = 20; a+= 30; a%=3; print(a)
print(True * False)
print(True & False)
print(True and False)
print(((6>3) and (7<4) or (18==3)) and (9>3))
print(True is False)
print(((True == False) or (False > True)) and (False <= True))



##################################################################################################################

### Question 3


s1 = 'Nice to have it'
s2 = 'here'
print(s1)


####################################################################################################################

### Question 4


a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])


###################################################################################################################

### Question 5


s1 = 'Nice to have it'
s2 = 'here'
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.append(s2)
a.insert(0, s1)
print(a)


##################################################################################################################

### Question 6


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1 - color_list_2)


#################################################################################################################

### Question 7


import string
def ispangram (str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True

string= input('Enter Words:')
if(ispangram(string)== True):
    print('Yes')
else:
    print('No')




#################################################################################################################

### Question 8


a = int(input("enter the number: "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)



####################################################################################################################

### Question 9


word = input("input words")
a = word.split(",")
a.sort()
print((', ').join(a))


####################################################################################################################

### Question 10


d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57, 87, 67, 79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])