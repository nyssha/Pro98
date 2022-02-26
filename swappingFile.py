def swappingFile():
     file = open('Sample1.txt', 'r') 
     file1 = open('Sample1.txt', 'r')  
     with open(file, 'r') as a:
         data_a = a.read()
     with open(file1, 'r') as a:
         data_b = b.read()

     with open(file, 'w') as a:
         data_a = b.read()
     with open(file1, 'w') as a:
         data_b = a.read()


     
swappingFile()     







