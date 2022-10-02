# Create a class with the name "Comment". The __init__ method should accept 3 parameters:
# •	username
# •	content
# •	likes (optional, 0 by default)
# Use the exact names for your variables
# Note: there is no input/output for this problem. Test the class yourself and submit only the class

class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

# Testing:
# comment = Comment("user1", "I like this book")
# print(comment.usernaTme)
# print(comment.content)
# print(comment.likes)
