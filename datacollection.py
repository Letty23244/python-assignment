#list:are mutable , it also works with index
# items stored shud be the same
studentNames = ['sandra', 'patricia','phionah','anitah']
studentMarks =[90,80,70,60]


# access the whole list
print(studentNames, type(studentNames))

# index(positive indexing)
print(studentNames[1])
print(studentNames[2])
print(studentNames[3])


#adding new item to the list
#at the end
studentNames.append('michelle')
print(studentNames)

#at aparticular position
studentNames.insert(2, 'faith')
print(studentNames)