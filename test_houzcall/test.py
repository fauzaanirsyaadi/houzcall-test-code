# input :

array_1 = [10, 20, 30, 40, 50]
array_2 = [80, 70, 60, 50, 40, 30]

output = []
for i in array_1:
  print(i)
  for y in array_2:
    if i == y:
      output.append(i)
  
print(output)
# out put 
# [30, 40, 50]
  