# Problem:Given a response code (200, 201, 400, 401, 404, 500), use match-case to print appropriate message:
# 200 → OK
# 201 → Created
# 400 → Bad Request
# 401 → Unauthorized
# 404 → Not Found
# 500 → Server Error
# Else → "Unknown Status Code"
response_code=int(input("Enter your respone code make sure respond code are these numbers 200,201,400,401,404,500: "))
match response_code:
    case 200:
        print("Status is OK!: ")
    case 201:
        print("Status is created: ")
    case 400:
        print("Status is Bad Request: ")
    case 401:
        print("Status is unauthorized: ")
    case 404:
        print("Status is Not Found: ")
    case 500:
        print("Status Server Error: ")
    case _:
        print("Unknown Status Code: ")
