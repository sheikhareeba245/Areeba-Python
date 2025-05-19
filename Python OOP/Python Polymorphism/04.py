#Class Poloymorphism means diffrent classes using same method with the same name, but their behavior can be different depending on the class #
#This allows us to use a common interface for multiple classes
#Social Media Posts
# Problem:
# Create classes for TextPost and ImagePost. Both should have a method display(). Show how polymorphism works using a loop. 
class TextPost:
    def create(self):
        print("I created a text post for my instagram page")
class ImagePost:
    def create(self):
        print("I created some image post for my instagram posts")
posts=[TextPost(),ImagePost()]
for post in posts:
    post.create()
    