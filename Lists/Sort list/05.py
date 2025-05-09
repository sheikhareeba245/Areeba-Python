# Program: Case-Sensitive vs Case-Insensitive Sorting
# 📌 Question:
# Write a Python program to sort a list of words ignoring case sensitivity
countries=["London","USA","Turkey","pakistan","Iran","india"]
countries.sort(key=str.lower)
print(countries)