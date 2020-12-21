import requests
from bs4 import BeautifulSoup
import tokenize
from io import StringIO
from collections import deque

class Expression :
    
    # Set the precedence level of the operators
    precedence = {"^" : 4,  
                  "/" : 3,
                  "*" : 3,
                  "+" : 2,
                  "-" : 2,
                  "(" : 1 } 

    def __init__(self, exp_str) :
        self.exp_str = exp_str
        self.infix_tokens = []  
        self.postfix_tokens = []  

    def Evaluate(self) :
        self.Tokenize()
        self.InfixToPostfix()
        self.EvaluatePostfix()

    def Tokenize(self) :

        tuplelist = tokenize.generate_tokens(StringIO(self.exp_str).readline)

        for x in tuplelist :
            if x.string :
                self.infix_tokens.append(x.string)

    def InfixToPostfix(self) :

        stack = deque()
        stack.appendleft("(")
        self.infix_tokens.append(")")
    
        while self.infix_tokens :
    
             token = self.infix_tokens.pop(0) 

             if token == "(" :
                 stack.appendleft(token)

             elif token == ")" :
                 # Pop out all the operators from the stack and append them to 
                 # postfix expression till an opening bracket "(" is found

                 while stack[0] != "(" : # peek at topmost item in the stack
                     self.postfix_tokens.append(stack.popleft())
                 stack.popleft()

             elif token == "*" or token == "/" or token == "+"\
                 or token == "-" or token == "^" :

                 # Pop out the operators with higher precedence from the top of the
                 # stack and append them to the postfix expression before
                 # pushing the current operator onto the stack.
                 while ( stack and self.precedence[stack[0]] >= self.precedence[token] ) : 
                     self.postfix_tokens.append(stack.popleft())
                 stack.appendleft(token)

             else :
                 # Positions of the operands do not change in the postfix
                 # expression so append an operand as it is to the postfix expression
                 self.postfix_tokens.append(token)

    def EvaluatePostfix(self) :

        stack_result = deque()
    
        while self.postfix_tokens :
            token = self.postfix_tokens.pop(0)

            if token.isdigit() :
               stack_result.appendleft(float(token))
            else :
               x = float(stack_result.popleft())
               y = float(stack_result.popleft())

               # Note the order of operands(x, y), result equals [y(operator)x]
               if (token == "+") :
                   stack_result.appendleft(float(y+x))
               elif (token == "-") :
                   stack_result.appendleft(float(y-x))
               elif (token == "*") :
                   stack_result.appendleft(float(y*x))
               elif (token == "/") :
                   stack_result.appendleft(float(y/x))
               elif (token == "^") :
                   stack_result.appendleft(float(pow(y,x)))
        global res
        res = str(stack_result.popleft())

resalt=19520000
tried=300
for x in range(tried):
    URL = 'http://45.122.249.68:8098/challenge.php'
    cookie = {'PHPSESSID': 'bce8faf3b061bcc8617fd96b8f131a4a'}
    dat = {'result': resalt}
    page = requests.post(URL,cookies=cookie,data=dat)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    data = soup.h1.h1.text
    print(str(page.content))
    print ('This is data')
    data_tm = str(data)

    data_str = '';
    for i in data_tm:
        if ((i >= '0' and i <= '9') or (i == '+') or (i == '-') or (i == '*')):
            data_str = data_str + i
    print (data_str)

    res = 0

    e = Expression(data_str) 
    e.Evaluate()
    resalt=int(float(res))
    print (resalt)
    print("\n --------- \n \n")


"""

 ---------


b'<!DOCTYPE html><h1>Correct answers continuously: 199 <h1><br>Please help me 7-7-36-51+26*10*99*59-93+87+2*46*16*39-97 hurry up!<form action="/challenge.php" method=post><input type=text name=result><input type=submit></form>\n'
This is data
7-7-36-51+26*10*99*59-93+87+2*46*16*39-97
1575878

 ---------


b'<!DOCTYPE html><h1>Correct answers continuously: 200 <h1><br>Solve this Your flag: R0b0t!_1s_th4t_u?_1+2_3<form action="/challenge.php" method=post><input type=text name=result><input type=submit></form>\n'
This is data
00141+23
164

 ---------

"""
