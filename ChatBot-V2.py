import shelve
from fuzzywuzzy import fuzz

with shelve.open("Queries", writeback=True)as query:
    query["q0"] = '''Thank you for visiting Centralized Public Grievance Redress
And Monitoring System swachha, farewell\n'''
    query["q1"] = '''Press on the yellow button on right corner of your page
mentioning "SIGN IN" or check for the tab notifying "USER LOGIN"\n'''
    query["q2"] = '''sorry, after 3 unsuccessful log ins your account
will be blocked\n'''
    query["q3"] = '''click on forgot password below your login details, and you will be
receiving an OTP to your registered email ID or mobile number\n'''
    query["q4"] = '''from the homepage you could download the guidelines of public grievance
and other guidelines as a PDF file\n'''
    query["q5"] = '''please, check on nodal PG officers and choose
(central/state) division to know further\n'''
    query["q6"] = '''click on contact us on the top of the page or you could
get the details in nodal PG officers list\n'''
    query["q7"] = '''click on aboutus/FAQ's and help\n'''
    query["q8"] = '''english and hindi translation of page is available\n'''
    query["q9"] = '''Could you please be more specific\n'''
    Query = dict.copy(dict(query))

with shelve.open("Terminate", writeback=True)as terminate:
    terminate["term"] = {"bye": "q0",
                         "farewell": "q0",
                         "see ya": "q0"}
    Terminate = dict.copy(dict(terminate))

with shelve.open("Path", writeback=True)as path:
    path["pat"] = {"sign in": "q1",
                   "signin": "q1",
                   "create an account": "q1",
                   "attempts for logging in this website": "q2",
                   "max no of attempts to login": "q2",
                   "no of attempts": "q2",
                   "change my password": "q3",
                   "forgot my password": "q3",
                   "password recovery": "q3",
                   "don't know my password": "q3",
                   "reset my password": "q3",
                   "guidelines": "q4",
                   "contact number": "q6",
                   "contacts": "q6",
                   "number": "q6",
                   "officers responsible to take actions": "q5",
                   "officer details": "q5",
                   "list of officers information": "q5",
                   "phone number of officer": "q6",
                   "fax number": "q6",
                   "about centralized public grievance redress and monitoring system swachha": "q7",
                   "about cpgrams": "q7",
                   "about gov portal": "q7",
                   "about government portal": "q7",
                   "languages available": "q8",
                   "languages": "q8",
                   "website translatable languages": "q8",
                   "need help": "q9",
                   "want some help please": "q9"}
    Path = dict.copy(dict(path))

print("Hello, fellow citizen of India")
print("how can I be at service")
flag = False
while True:
    found = False

    print("="*40)
    ask = str(input()).lower()
    print("="*40)

    for q in Terminate["term"]:
        if fuzz.ratio(ask, q) > 45 or q in ask:
            ask = Terminate["term"][q]
            flag = True
            break
    if flag is True:
        print(Query[ask])
        break

    for q in Path["pat"]:
        if fuzz.ratio(ask, q) > 45 or q in ask:
            ask = Path["pat"][q]
            found = True
            print(Query[ask])
            break

    if found is False:
        print("kindly visit FAQ for more details")
