from random import choice

def get_bot_response(user_response, sequence_events):

  # bot responses
  bot_response_play_first_round = ["Great, let's play!", "Perfect, let me set the game for you.", "Ha!, lets see how 'good' you are..."]
  bot_response_play_consecutive_round = ["Perfect, don't leave me alone. Keep playing!", "Once more? Excellent.", "Again? This is great, lets see how you perform this time.", "You know you would never beat my record? I'm too good."]
  bot_respond_insisting_first_round = ["Are you really not going to play? Please say yes!", "Why not? It will be fun. Just say yes.", "You know I'm pretty persistence. I can be here asking all day."]
  bot_respond_insisting_consecutive_round = ["Really? Ho ahead I wait for you to say yes.", "Yes, yes, yes, yes... There is what you should respond.", "Don't worry just play this last one. I promis it will be the last.", "Still waiting for you to say yes.", "If you want to go I understand but lets play this last. Belive me this will be really the last one."]

  if user_response.lower() == "no" and sequence_events == 0:
    start_game = False
    return choice(bot_respond_insisting_first_round), start_game # ESTO DEVLVERA UNA LISTA, TIENES QUE DESPUES DIVIDIR LA LISTA ANTES DE ENSEÑAR LA RESPUESTA DEL BOT
  elif user_response.lower() == "no" and sequence_events > 0:
    start_game = False
    return choice(bot_respond_insisting_consecutive_round), start_game # ESTO DEVLVERA UNA LISTA, TIENES QUE DESPUES DIVIDIR LA LISTA ANTES DE ENSEÑAR LA RESPUESTA DEL BOT
  elif user_response.lower() == "yes" and sequence_events == 0:
    start_game = True
    return choice(bot_response_play_first_round), start_game
  elif user_response.lower() == "yes" and sequence_events > 0: # ESTO DEVLVERA UNA LISTA, TIENES QUE DESPUES DIVIDIR LA LISTA ANTES DE ENSEÑAR LA RESPUESTA DEL BOT
    start_game = True
    return choice(bot_response_play_consecutive_round), start_game # ESTO DEVLVERA UNA LISTA, TIENES QUE DESPUES DIVIDIR LA LISTA ANTES DE ENSEÑAR LA RESPUESTA DEL BOT



print("Welcome, I'm Lyra! The best bot assistance you will ever\nmeet. I will help you to take the best decision of your life.\nAfter this decision definetly your life will change. Mark my words!\nIn what will I help you? Hear you asking...\nIn deciding if you want to play a game or not.\n")
print("The game is simple. You will go through a obstacle course.\nIn the obstacle course you can do one of two things jump or\nduck. The track will always be the same but the catch is how\nfast can you complete it. But don't worry you will never beat me.\n")
print("The game will look like this.\n")
print("This are the controls: Jump 'P' and Duck 'L'")
print("""
******************************************************************************
                                                                  |    |        
                                                                  |    |
                                   ╳╳╳╳╳╳                         ██████ 
                                   ╳╳╳╳╳╳                                                                         
      ▆▆▆▆▆▆                       ╳╳╳╳╳╳
      |    |
      |    |                                                                       
******************************************************************************
                                                                                    """)
user_response = input("Now the important decision... You want to play it? Yes or No?")
print(user_response)