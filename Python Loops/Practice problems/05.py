#5. Customer Feedback Classifier
#Ask 5 users for feedback (good, bad, average, etc.)
#If "bad" is received, immediately stop collection (break)
#If all inputs are okay, print "All feedback collected!" (use for-else)
for i in range(5):
    feedback=input(f"Enter the feedback of a customer {i+1}: ")
    if feedback=="bad":
        print("Bad feedback giving by the customer: ")
        continue
    else:
        print("All feedback collected: ")
    