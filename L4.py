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
        elif state=='q1' and i<len(s) and s[i]=='b' and stack[-1]=='a':
            state='q2'
            stack.pop()
            i+=1
        elif state=='q2' and i<len(s) and s[i]=='b' and stack[-1]=='a':
            state='q2'
            stack.pop()
            i+=1
        elif state=='q2' and i<len(s) and s[i]=='b' and stack[-1]=='y':
            state='q3'
            i+=1
        elif state=='q3' and i<len(s) and s[i]=='b' and stack[-1]=='y':
            state='q3'    
            i+=1
        elif state=='q3' and stack[-1]=='y':
            state='q4'    
            stack.pop() 
        elif state == 'q4' and i == len(s):
            return True
        else:
            return False
if pda() == True:
    print('acept')
else:
    print('reject')

        
