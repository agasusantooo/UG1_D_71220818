baris= int(input('Input lebar belah ketupat: '))
print()
  
for i in range(baris):
  for j in range(baris-i):
    print(' ',end='')
      
  for k in range(i+1):
    print('* ',end='')
  print()
 
for i in range(1,baris):
  for j in range(i+1):
    print(' ',end='')
      
  for k in range(baris-i):
    print('* ',end='')
  print()