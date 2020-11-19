import sys
col = int(sys.argv[1])


# number of space in each row
x = col // 2 

## TOP Triangle
for i in range(1, col, 2):
    print(' ' * x*2, '* ' * i, ' ' * (x*4), '* ' * i,  sep='') 
    x -= 1

##  CENTER ROW
center = col * 2 + 2 if col % 2 == 0 else col * 2
print('* ' * center)

## BOTTOM
x = 1  # number of space
col = col - 1 if col % 2 == 0 else col - 2
for i in range(col, 0, -2):
    print(' ' * x*2, '* ' * i, ' ' * (x*4), '* ' * i, sep='') 
    x += 1
    
    
