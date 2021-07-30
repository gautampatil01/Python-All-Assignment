x = input('gift_presented_to: ')
val = [int(i) for i in x.split()]
print(val)

gift_received_from = [2, 1, 4, 5, 3]

for i in range(len(val)):
  print("Person P" + str(val[i])  + " has received gift from Person P" + str(gift_received_from[i]))
