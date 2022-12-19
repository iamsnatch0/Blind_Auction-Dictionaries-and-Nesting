#Dictionaries and Nesting

from replit import clear
from art import logo
print(logo)

user_bid = {}
bid_done = False

def look_highest_bidder(bid_record):
  highest_bid = 0
  winner_user = ""
  for bidder in bid_record:
    amount_bid = bid_record[bidder]
    if amount_bid > highest_bid:
      highest_bid = amount_bid
      winner_user = bidder
  print(f"The winner is {winner_user} with a bid of £{highest_bid}")
    
  
while not bid_done:
  user_question = True
  user = input("What is your name?: ")
  bid = int(input("What is your bid price?: £"))
  user_bid[user] = bid
  continue_bid = input("Is there another user who want to bid? Type 'yes' or 'no' to continue. \n")
  if continue_bid == "no":
    bid_done = True
    look_highest_bidder(user_bid)
  elif continue_bid == "yes":
    clear()
    