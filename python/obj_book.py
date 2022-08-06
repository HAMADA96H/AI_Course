from book10 import book
#book100 = (6,7)
book1 = book(name ="py",auther="ahmad",num_pages=100,typee="prog",a=10,b=5)
book2 =  book(name ="algebra",auther="raghad",num_pages=200,typee="math")
book3 =  book("history",auther="sami",num_pages=100,typee="s")

#printvalue(v)
book2.push("math")

print ("\n===============================\n")
book2.buy(100)
print ("\n===============================\n")

v = book1.mul(book1.a,book1.b)
print(v)
print ("\n===============================\n")

book1.printvalue(v)