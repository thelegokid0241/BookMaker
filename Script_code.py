from Questions.User import *
#from Login import *
from Questions.Book import *
u1 = User(f'{username}.csv')#making users
#u2 = User('user2.csv')#User('filename.csv') goes to User.__init__
#u3 = User('user3.csv')

u1.load_books()#loading books from user1.csv
#u2.load_books()#loading books from user2.csv
#u3.load_books()
m_e=input("Do you want to make or edit (M for make, E for edit)?")

uo=4

print()
ae = input("BOOK NUMBER?")
if m_e.lower() == 'm':


    print(f"{u1.__dict__}")
    Book1 = Book(input('enter book1 title '),input('enter book1 insides'), number=None)#goes to Book.__init__
    u1.add_book(Book1)

    #Book2 = Book(input('enter your new title for a new book'), input('enter book2 insides'), number=None)
    #ae = input("BOOK NUMBER?")   #u2.add_book(Book2)  #adding a book to a user
def search():
    #ae=input("BOOK NUMBER?")
     e=0
     pre=-1
     while u1.book_list != ae:
        e=pre+2 or
        pre=pre+1
        book=








if m_e.lower() == 'e':
    search()









while uo != 5:
    pass
open('u1.csv')
#Book3 = Book(input('enter the new title for a new book '), input('enter the paragraph(s) for a new book'), number=None)
    #u3.add_book(Book3)
#u1.add_book(Book1)  #adding   a   book   to   a   user   goes   to   User.add_book
#ans=input("new book?")








print('user1 book list: ', u1.book_list)
#print('user2 book list: ', u2.book_list)
#print('user3 book list: ', u3.book_list)
#u1.book_list.clear()
#u2.book_list.clear()
#u3.book_list.clear()








#u1.save_books()#saving to file
print()
#if ans.lower() == 'yes':
        #Book2 = Book(input('enter book2 title '), input('enter book2 insides'), number=2)
        #u2.add_book(Book2)  # adding a book to a user

        #Book3 = Book(input('enter the new title for a new book '), input('enter the paragraph(s) for a new book'),number=3)
#u3.add_book(Book3)  # adding a book to a user
'''with open ('user1.csv', 'r') as user1:
print(user1.readlines())'''

u1.save_books()  # saving to file
#u2.save_books()
#u3.save_books()

'''def search():
    num=0
    while Book3.number != num:
        num = num+1
    print('found')
if m_e.lower() == 'e':
    ans=input("Book number?")
    search()
Book2 = Book(input('enter book2 title '),input('enter book2 insides'), number=2)
u2.add_book(Book2)#adding a book to a user

Book3 = Book(input('enter the new title for a new book '),input('enter the paragraph(s) for a new book'), number=3)
u3.add_book(Book3)#adding a book to a userç

print('user1 book list: ', )
print('user2 book list: ', )
print('user3 book list: ', )
#u1.save_books()#saving to file
#u2.save_books()
#u3.save_books()
del u1.book_list
del u2.book_list
del u3.book_list'''
