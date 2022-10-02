# Create class Email. The __init__ method should receive sender, receiver and a content.
# It should also have a default set to False attribute called is_sent. The class should have two additional methods:
# •	send() - sets the is_sent attribute to True
# •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver, and the third one – the content.
# On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
# Call the send() method for the given indices of emails. For each email, call the get_info() method.

class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []
command = input()

while command != "Stop":
    sender, receiver, content = command.split()
    emails_list.append(Email(sender, receiver, content))
    command = input()

indices_list = input().split(", ")
indices_list = list(map(int, indices_list))

for email in indices_list:
    emails_list[email].send()

for email in emails_list:
    print(email.get_info())
