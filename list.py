li = []
lis = []

li.append(10)
li.append(20)
li.append(30)
li.append(40)
li.append(50)
li.append(20)
li.append(50)
li.append(10)
print "after appending the list",li

li.remove(20)
li.remove(50)
print "After delete operation",li

print "Is there an element 23 present in the list 'li':",(23 in li)
print "Is there an element 30 present in the list 'li':",(30 in li)

print "Is there any elements in the list li:",all(li)
print "'lis' Is it an empty list:",any(lis)
print "'li' Is it an empty list:",any(li)

print "Length of the 'li' list ",len(li)
print "Length of the 'lis' list ",len(lis)

print "Position of element 40",li.index(40)
print "Position of element 10",li.index(10)

print "No. of occurence of element 10 in list 'li'",li.count(10)
print "No. of occurence of element 40 in list 'li'",li.count(40)

li1 = [10, 30, 40, 20, 50, 10]
li2 = [10, 30, 40, 10, 50, 20]
print "compare list li with li1",cmp(li,li1)
print "compare list li2 with li",cmp(li2,li)
print "compare list li with li2",cmp(li,li2)
