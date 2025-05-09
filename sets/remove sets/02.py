#we use discard function to remove main difference is that if the item is not exist in the set we want remove rise error on the other side discard does not do this if the removed item not available in set
departments={"computer science","medical","fashion design","urdu","english","law"}
departments.discard("english")
print("items discarded: ",departments)
departments.discard("psycology")
print("items discarded: ",departments)