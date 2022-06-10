def pda():
    s = input()
    state = 'q0'
    stack = ['z']

    i=0
    while True:
        if state=='q0' and i<len(s) and s[i]=='a':
            state='q1'
            stack.append('a')
            i+=1
        elif state=='q1' and i<len(s) and s[i]=='a':
            state='q2'
            stack.append('a')
            i+=1
        elif state=='q2' and i<len(s) and s[i]=='a':
            state='q2'
            stack.append('a')
            i+=1
        elif state=='q2' and i<len(s) and s[i]=='b' and stack[-1]=='a':
            state='q3'
            stack.pop()
            i+=1
        elif state=='q3' and i<len(s) and s[i]=='b' and stack[-1]=='a':
            state='q4'
            stack.pop()
            i+=1
        elif state=='q4' and i<len(s) and s[i]=='b' and stack[-1]=='a':
            state='q4'
            stack.pop()
            i+=1

  
        elif state=='q4' and stack[-1]=='z':
            state='q5'    
            stack.pop()
            
        elif state == 'q5' and i == len(s):
            return True
        else:
            return False

if pda() == True:
    print('accept')
else:
    print('reject')

        
