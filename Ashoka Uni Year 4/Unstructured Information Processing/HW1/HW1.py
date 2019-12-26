import re

query1 = re.compile(r'\bsavings\b|\bsaving\b|\bchecking\b|\bbank account\b|\baccount.*balance\b|\bbalance.*account\b|\baccount\b', flags = re.I)

query2 = re.compile(r'\boutstanding\b|\btotal.*owed\b|\bowe\b|\bhave to pay\b|\bcredit.*outstanding\b|\boutstanding.*payment\b|\boutstanding.*payments\b|\boutstanding.*pay\b', flags = re.I)

query3 = re.compile(r'\bdue\b|\bpayment.*due\b|\bhave to pay\b|\bwhen.*pay\bpay.*when\b|\bpay.*by', flags = re.I)
def state1():
    print ("What is your account number?")
    number = input()
    if re.match(r"^\d{9,13}$",number):
        print ("The balance for Account #%s is $200.00"%number)
    else:
        print ("Invalid account number")
        state1()

def state2():
    print ("What is your credit card number?")
    number = input()

    print ("Please remember we will never ask for your CVV")

    if lundcheck(number):
        print ("The outstanding balance for Credit Card #%s is $4320.00"%number)
    else:
        print ("Invalid credit card number")
        state2()

def state3():
    print ("What is your credit card number?")
    number = input()

    print ("Please remember we will never ask for your CVV")

    if lundcheck(number):
        print ("There are 2 payment(s) due on Credit Card #%s, $420.00 due on Sep. 10 2019,$30 due on Oct. 10 2019"%number)
    else:
        print ("Invalid credit card number")
        state3()

def lundcheck(num):
    sume = 0
    digits = len(num)
    xor = digits & 1
    for i in range(0,digits):
        digit = int(num[i])

        if not ((i & 1) ^ xor):
            digit = digit * 2

        if digit>9:
            digit = digit - 9
        sume = sume + digit
    if sume%10 == 0:
        return True
    return False

def queryloop(query):
    
    if query1.search(query):
        state1()
    elif query2.search(query):
        state2()
    elif query3.search(query):
        state3()
    else:
        print ("I cannot answer that. Please contact the branch.") 

print ("What would you like to do?")

response = input()

queryloop(response)
