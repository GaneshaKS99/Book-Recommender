import requests
import urllib.request

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk,kk): print("\033[93m {}\033[00m" .format(skk),kk) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 


def test1():							# Fetching the home page
    print("\n Conducting Test 1:",end="")
    prCyan(" Fetching the home page...")
    response = requests.get('http://127.0.0.1:8000/')
    if response.status_code == 200:
   	    prGreen('\t \n -----> Test 1 Success! <------\n\n')

def test2():							#getting Ratings page for book which is present in the Data base
    print("\n Conducting Test 2:",end="")
    prCyan(" Getting the Ratings page for book which is present in the Database...")
    response = requests.get('http://127.0.0.1:8000/4/')
    if (response.status_code == 200):
   	    prGreen('\t \n -----> Test 2 Success! <------\n\n')

def test3():							#getting a book which isnt present
    print("\n Conducting Test 3:",end="")
    prCyan(" Getting a book with a Book ID which is unsyntactical...")
    response = requests.get('http://127.0.0.1:8000/hgh/')
    if (response.status_code==404):
    	prGreen("\t \n -----> Test 3 Success! <------\n\n")

def test4():							#Testing Validity of Search Bar
    print("\n Conducting Test 4:",end="")
    prCyan(" Testing the working of the Search bar...")
    response = requests.get('http://127.0.0.1:8000/?q=asd/')
    if (response.status_code==200):
    	prGreen("\t \n -----> Test 4 Success! <------\n\n")
    #prGreen("\t \n -----> Test 4 Success! <------\n\n") if (response.status_code==200) else prRed ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else prYellow (response.status_code)

def test5():							#Accessing the Recommendation page
    print("\n Conducting Test 5:",end="")
    prCyan(" Accessing the Recommendation page...")
    response = requests.get('http://127.0.0.1:8000/recommend/')
    if (response.status_code==200):
    	prGreen("\t \n -----> Test 5 Success! <------\n\n")
    #prGreen("\t \n -----> Test 5 Success! <------\n\n") if (response.status_code==200) else print ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else print (response.status_code)

def test6():							#Making Changes to Ratings through External means //CSRF protection
    print("\n Conducting Test 6:",end="")
    prCyan(" Making Changes to Ratings of a book through External means")
    response = requests.post('http://127.0.0.1:8000/3/')
    if (response.status_code==403):
    	prGreen("\t \n -----> Test 6  Success! <------\n\n")
    #prGreen("\t \n -----> Test 6 Success! <------\n\n") if (response.status_code==200) else print ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else prYellow("\n \t ERROR ",response.status_code)
    print("\n")

def test7():							#Making Changes to Ratings through External means
    print("\n Conducting Test 7:",end="")
    prCyan(" Making Changes to Books through External means")
    response = requests.post('http://127.0.0.1:8000/hgh/')
    if (response.status_code==404):
    	prGreen("\t \n -----> Test 7  Success! <------\n\n")
    #prGreen("\t \n -----> Test 7 Success! <------\n\n") if (response.status_code==200) else print ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else prYellow("\n \t ERROR ",response.status_code)
    print("\n")

def test8():							#Checking permanent redirection of a page
    print("\n Conducting Test 8:",end="")
    prCyan(" Checking the redirection of a page")
    response = requests.get('http://127.0.0.1:8000/3/')
    if (response.is_permanent_redirect==False):
    	prGreen("\t \n -----> Test 8 Success! <------\n\n")
    #prGreen("\t \n -----> Test 8 Success! <------\n\n") if (response.status_code==200) else print ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else prYellow("\n \t ERROR ",response.status_code)
    print()


def test9():							# reply shouldnt be in JSON format
    print("\n Conducting Test 9:",end="")
    prCyan("Testing invalidity of JSON format reply")
    response = requests.get('http://127.0.0.1:8000/4/')
    try:
        print(response.json())
    except ValueError:
        #print("JSON Decoding failed since result not in JSON format")
        prGreen("\t \n -----> Test 9 Success! <------\n\n")


def test10():							#Character encoding of list of books should be utf-8
    print("\n Conducting Test 10:",end="")
    prCyan("Character encoding of list of books should be utf-8")
    response = requests.get('http://127.0.0.1:8000/')
    #prGreen("\t \n -----> Test 10 Success! <------\n\n") if (response.status_code==200) else print ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else prYellow("\n \t ERROR ",response.status_code)
    if (response.encoding=="utf-8"):
    	prGreen("\t \n -----> Test 10 Success! <------\n\n")
    #prGreen("\t \n -----> Test 8 Success! <------\n\n") if (response.status_code==200) else print ("\t \n Page Couldn't be found \n \n") if (response.status_code==404) else prYellow("\n \t ERROR ",response.status_code)
    print()
    


#test_function = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10]


#n = int(input('Enter the number of tests to perform(max 10): '))
#for i in range(n):
#    test_function[i]()
