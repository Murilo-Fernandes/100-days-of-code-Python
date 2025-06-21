class User: 
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.followers += 1
        self.following += 1

    def greeting(self):
        print(f'Hello, I am {self.name} and I have {self.followers} followers.')

user1 = User("245", "John Doe")
print(user1.id)  # This will print the user_id
print(user1.__dict__)  # This will show all attributes of the user1 object
user1.follow(user1)  # This will call the follow method 
user1.follow(user1)  # This will call the follow method 

user1.greeting()

# This will show all attributes of the user1 object