# ############### Blackjack Project #####################
# import random
# 
# 
# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card=random.choice(cards)
#     return card
# 
# 
# def calculate_score(cards):
#     """the Above function is to remove ace card if score is >=21"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     '''above function is to get blackjack'''
#     if 11 in cards and sum(cards)>21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)
# 
# def compare(user_score, computer_score):
#     if user_score>21 or computer_score>21:
#         return "you went over. you lose"
#     if user_score==computer_score:
#         return "Its a Draw."
#     elif user_score==0:
#         return "you win with a blackjack"
#     elif computer_score==0:
#         return "lose opponent has blackjack"
#     elif user_score>21:
#         return "you went over. you lose"
#     elif computer_score>21:
#         return "you win"
#     elif user_score>computer_score:
#         return "you win"
#     else:
#         return "you lose"
#     
# def play_game():        
#     
#     user_cards = []
#     computer_cards = []
#     is_game_over=False
#     
#     for i in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#     while not is_game_over:
#        user_score = calculate_score(user_cards)
#        computer_score = calculate_score(computer_cards)
#        print(f"Your cards {user_cards}, current score {user_score}" )
#        print(f"computer cards {computer_cards[0]}")
#        if user_score==0 or computer_score==0 or user_score > 21:
#            is_game_over = True
#        else:
#             user_input=input("type 'y' to pick another card or type 'n' to pass: ")
#        
#             if user_input=="y":
#                    user_cards.append(deal_card())
#             else:
#                is_game_overy=True
# 
#     while computer_score!=0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score=calculate_score(computer_cards)
#         
#     print(f"Your final Hand{user_cards} final score; {user_score}")
#     print(f"computer's final Hand {computer_cards} final score {computer_score}")
#     print(compare(user_score, computer_score))
# 
# while input("Do you want to play Game of Blackjack type 'y' or type 'n' to exit: ") =="y":
#     play_game()
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_v,times_v,places_v):
    new_country = {}
    new_country["country"] = country_v
    new_country["visits"]  = times_v
    new_country["citis"] = places_v
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
