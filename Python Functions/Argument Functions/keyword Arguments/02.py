#if you don't know how many keyword arguments ypu pases so use
#**kwargs short-hand of keyword arguments 
#You want to create a user profile system where a user can enter any amount of info (name, email, phone, etc.). Your function should:
#Accept all keyword data
#Print it in a clean profile format
def user_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
user_profile(name="Areeba",email="areebas363@gmail.com",phone="09876534")
