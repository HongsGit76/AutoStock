from slacker import Slacker

slack = Slacker('xoxb-1637588864358-1650823569092-JbpGBgKODsPWsRn5gQvdi9FV')

# Send a message to #general channel
slack.chat.post_message('#programming-develop', 'Hello fellow slackers!')