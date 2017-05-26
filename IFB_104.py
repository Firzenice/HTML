
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9808264
#    Student name: Ngan Pok Ho
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopper
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for aggregating product data published by a variety of
#  online shops.  See the instruction sheet accompanying this file
#  for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution.)
from urllib import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from Tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression.  (You do NOT need to
# use these functions in your solution, although you will find
# it difficult to produce a robust solution without using
# regular expressions.)
from re import findall, finditer

# Import the standard SQLite functions just in case they're
# needed.
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the invoice file. To simplify marking, your program should
# produce its results using this file name.
file_name = 'invoice.html'

html_template = """<!DOCTYPE html>
<html>

<head>
    <title>Electronic Heaven</title>
</head>

<style> body {background-color:lightgrey} </style>

<body>

<table style="width:100%">

    <tr>
        <td align='center'>Electronic Heaven</td>
    </tr>

    <tr>
        <td align='center'><img src="https://t3.ftcdn.net/jpg/01/04/99/88/500_F_104998865_ZT6yvRZdRZeblGbbo5QycRFO9Gg5W4qv.jpg"</td>
    </tr>

</table>
    

      
  
"""

##print apple_contents

def regular_express(beginning_pat, end_pat, in_text, num):
    find_text = beginning_pat + '([\s\S]*?)' + end_pat
    # print find_text
    reg_list = findall(find_text, in_text)
    return_items = reg_list[0:num]
    return return_items


##apple_items = findall('<entry>([\s\S]*?)<\/entry>', apple_contents)
##print apple_items[0]

master_items1 = []

apple_store = "http://ax.itunes.apple.com/WebObjects/MZStoreServices.woa/ws/RSS/topsongs/limit=10/xml"

apple_contents = urlopen(apple_store).read()

apple_items = regular_express('<entry>', '<\/entry>', apple_contents, 5)
#print apple_items[0]


for each in apple_items:
  title = regular_express('<title>', '<\/title>', each, 1)
  price = regular_express('currency="USD">\$', '<\/im:', each, 1)
  image = regular_express('<im:image height="55">','<\/im:image>', each, 1)
  master_items1.append ([title,price,image])
  



doc = ""
for items in range(5):
    doc = doc + "<tr>" + "<td>" + master_items1[items][0][0] + "</td>" + "</tr>" + "</br>" + "</br>" + "\n"
    doc = doc + "<tr>" + "<td>" + master_items1[items][1][0]*1.33 + "</td>" + "</tr>" + "</br>" + "</br>" + "\n"
    doc = doc + "<tr>" + "<td>"+ "<img src=" + master_items1[items][2][0] + ">" + "</td>" + "</tr>" + "\n"
    


##headphones_store = "https://www.hifiheadphones.ca/rss.php?action=featuredproducts&type=rss"
##headphones_contents = urlopen(headphones_store).read()
##
##headphones_items = regular_express('<item>', '<\/item>', headphones_contents, 2)
###print headphones_items[0]
##
##for each in headphones_items:
##  title = regular_express('<title>', '<\/title>', each, 1)
##  price = regular_express('<isc:price>', '<\/isc:price>', each, 1)
##  image = regular_express('<isc:image>', '<\/isc:image>', each, 1)
##  master_items.append ([title,price,image])
##
##
##
##
##
##
##stereophone_store = "https://www.stereophonic.com.au/rss.php?action=featuredproducts&type=rss"
##stereophone_contents = urlopen(stereophone_store).read()
##
##stereophone_items = regular_express('<item>', '\/item', stereophone_contents, 2)
###print stereophone_items[0]
##
##for each in stereophone_items:
##  title = regular_express('<title>', '<\/title>', each, 1)
##  price = regular_express('<isc:price>', '<\/isc:price>', each, 1)
##  image = regular_express('<isc:image>', '<\/isc:image>', each, 1)
##  master_items.append ([title,price,image])





    
  

    
bottom_html = "</body>" + "\n" + "</html>"

final = html_template + doc + bottom_html
html_file = open(file_name, 'w')
html_file.write(final)
html_file.close()






     

##print master_items[0][1]*2

##print 'html header'
##    for items in master_items:
##    
##        print 'The code before the title ' + items[0]
##        print 'The code between the title and the price ' + str(round(items[1]*1.33, 2))

    



# Create a window
the_window = Tk()

# Give the window a title
the_window.title('Welcome To Electronic Heaven')

# Set the window size
the_window.geometry('500x500')


# The download status when the invoice button is pressed
def downloading():
    download_status['text'] = "Downloading Invoice..."
    the_window.after(1500, clear_label)

# Upadating the label
def clear_label():
    download_status['text'] = "Done"
##    html_file = open(file_name, 'w')
##    html_file.write(html_template)
##    html_file.close()

    




#Create a label widget
introduction = Label(the_window, text = 'Electronic Heaven',
                     fg = 'orange red', font = ('Times', 20))
step_one = Label(the_window, text = 'Choose Your Product And Quantity',
                    fg = 'orange red', font = ('Times', 15))
watches = Label(the_window, text = 'Watches',
                    fg = 'black', font = ('Times', 15))
phones = Label(the_window, text = 'Phones',
                    fg = 'black', font = ('Times', 15))
television = Label(the_window, text = 'Television',
                    fg = 'black', font = ('Times', 15))
step_two = Label(the_window, text = 'Get Invoice For Details On The Choosen Products',
                    fg = 'orange red', font = ('Times', 15))
progress = Label(the_window, text = 'Order Progress', fg = 'orange red',
                 font = ('Times', 15))
download_status = Label(the_window, text = 'Ready', fg = 'black',
                 font = ('Times', 20))

# Spinbox widget
spinwidget1 = Spinbox(the_window, from_= 0, to = 5, width = 3)
spinwidget2 = Spinbox(the_window, from_= 0, to = 5, width = 3)
spinwidget3 = Spinbox(the_window, from_= 0, to = 5, width = 3)


# Create a button widget
print_invoice = Button(the_window, text = 'Print Invoice', width = 10,
                       activebackground = 'grey', relief = 'groove',
                       command = downloading)
                       



################### - Calling the geometry manager - ################

# Label Geometry Manager
introduction.grid(row = 1, column = 4, pady = 5, ipadx = 150, columnspan = 10)
step_one.grid(row = 2, column = 4, pady = 10, columnspan = 10)
watches.grid(row = 3, column = 3, pady = 15, columnspan = 10)
phones.grid(row = 4, column = 3, pady = 15, columnspan = 10)
television.grid(row = 5, column = 3, pady = 15, columnspan = 10)
step_two.grid(row = 6, column = 4, pady = 10, columnspan = 10)
progress.grid(row = 8, column = 4, pady = 30, columnspan = 10)
download_status.grid(row = 9, column = 4, columnspan = 10)



# Button Geometry Manager
print_invoice.grid(row = 7, column = 4, ipady = 2, columnspan = 10)



# Spinbox Geometry Manger
spinwidget1.grid(row = 3, column = 6, columnspan = 10)
spinwidget2.grid(row = 4, column = 6, columnspan = 10)
spinwidget3.grid(row = 5, column = 6, columnspan = 10)













#------------------------------------------------------------------
the_window.mainloop()


