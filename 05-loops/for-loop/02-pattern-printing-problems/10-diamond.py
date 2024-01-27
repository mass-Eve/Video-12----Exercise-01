'''
                * 
              * * * 
            * * * * * 
          * * * * * * * 
        * * * * * * * * * 
          * * * * * * * 
            * * * * * 
              * * * 
                * 
'''

for i in range(5):
    for space in range(5*2 - ((i+1)*2)):
        print(' ', end = '')
    for stars in range((i*2) + 1):
        print('* ', end = '')
    print()
    
for i in range(4):
    for space in range((i+1)*2):
        print(' ', end = '')
    for stars in range((4*2-1) - (i*2)):
        print('* ', end = '')
    print()