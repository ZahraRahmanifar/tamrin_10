def pda():
    s = input()
    state = 'q0'
    stack = ['y']
    i=0
    while True:
        if state=='q0' and i<len(s) and s[i]=='a':
            state='q1'
            stack.append('a')
            i+=1
        elif state=='q1' and i<len(s) and s[i]=='a':
            state='q1'
            stack.append('a')
            i+=1
        elif state=='q1' and i<len(s) and s[i]=='b':
            state='q2'
            stack.append('b')
            i+=1
        elif state=='q2' and i<len(s) and s[i]=='b':
            state='q2'
            stack.append('b')
            i+=1
        elif state=='q2' and i<len(s) and s[i]=='c':
            state='q3'
            i+=1
        elif state=='q3' and i<len(s) and s[i]=='c':
            state='q4'    
            i+=1
        elif state=='q4' and i<len(s) and s[i]=='c' and stack[-1]=='b':
            state='q4'
            stack.pop()    
            i+=1
        elif state=='q4' and i<len(s) and s[i]=='d':
            state='q5'
            stack.append('d')    
            i+=1
        elif state=='q5' and i<len(s) and s[i]=='d':
            state='q5'
            stack.append('d')   
            i+=1
        elif state=='q5' and i<len(s) and s[i]=='e' and stack[-1]=='d':
            state='q6'
            stack.pop()    
            i+=1
        elif state=='q6' and i<len(s) and s[i]=='e' and stack[-1]=='d':
            state='q6'
            stack.pop()    
            i+=1
        elif state=='q6' and i<len(s) and s[i]=='e' and stack[-1]=='a':
            state='q7'
            stack.pop()    
            i+=1
       elif state=='q7' and i<len(s) and s[i]=='e' and stack[-1]=='a':
            state='q7'
            stack.pop()    
            i+=1
        elif state=='q7' and stack[-1]=='y':
            state='q8'    
            stack.pop()    
        elif state == 'q8' and i == len(s):
            return True
        else:
            return False
if pda() == True:
    print('accept')
else:
    print('reject')

        
