from slacker import Slacker

slack = Slacker('')

# Send a message to #general channel
slack.chat.post_message('#programming-develop', 'Hello fellow slackers!')