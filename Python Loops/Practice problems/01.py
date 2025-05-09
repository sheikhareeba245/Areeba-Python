# 1. ATM PIN Verification System
# Prompt the user to enter a 4-digit PIN (max 3 attempts).
#If correct PIN ("4312"), print "Transaction Allowed"
#If wrong 3 times, print "Card Blocked"
#Use while, break, else
correct_pin=4312
attempts=0
while attempts<3:
 pin=int(input("Enter you  4 digit pin: "))
 if pin==correct_pin:
  print("Transcation allowed: ")
  break
 else:
  print("Wrong Pin")
  attempts+=1
else:
 print("Transcation Failed ")
 