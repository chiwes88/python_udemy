import math

# Hello World program in Python
print(type(2 + 4))

print(bin(25))

#convert from binary to int
print(int('0b101', 2)) #binanry value, base 2

#private variable
__name__ #two underscores

#shorthand assignment of variables
a, b, c = 1, 2, 3

#Escape characters
#tab \t  newline \n string \
weather = "\t It\'s \"kinda of\" sunny \n good day!"

print(weather)

#formatted strings
name = 'Jenn'
age = 30
print("Wsup, " + name + " ....Are you " + str(age) + " years old?")
print(f'Wsup, {name} ....Are you {age} years old?')

#string indexes
# [start:stop:stepover]
print(name[::-1]) #reverse order
print(name[::-2]) #reverse order by 2
print(name[-1]) #prints last element: n
print(name[:1]) #prints:J

#FIND FUNCTION
print(name.find('e'))


#list 
li = [1, 2, 56, 87, 46]
li2 = ['bu', 'gy', 'mu']
print(li[2]) #output : 56

#list slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] #copying prev cart and making a new cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart) #prints original cart


#matrix - multi-dimensional arrays
matrix = [
    [1, 0, 1],
    [0, 5, 8],
    [9, 6, 4]
]
print(matrix[1][2]) #should print 8

basket = [1, 2, 3, 4, 5]

#adding
# basket.append(100)
# new = basket
# basket.insert(2, 3)
# new1 = basket
new3 = basket.extend([25]) #modifies in place
# print(new)
# print(new1)
print(basket)

#deleting
basket.pop() #removes last item and returns it
print(basket)
basket.pop(0) #removes number at index specified
print(basket)
basket.remove(3) #removes from indix 3
print(basket)
basket.clear() #clears out entire list
print(basket)

#find index
bask = ['a', 'b', 'c', 'd', 'j', 'e', ]
 #searches for letter 'd' between index 0 - 3
print(bask.index('d', 0, 4)) 
print('d' in bask) #returns true if d in bask
print(bask.count('d')) #counts number of occurances

#sorting
bask.sort() #modifies list in place; doesnt create a new list
bask.copy()
bask.reverse()
print(sorted(bask)) #creates new list; NOT in-place

#range
print(range(1, 100))
print(list(range(1, 100)))

#.join
sentence = 'hey '.join(['wsup', 'with', 'you'])
print(sentence)

#list unpacking
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)
a,b,c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(other)
print(d)
