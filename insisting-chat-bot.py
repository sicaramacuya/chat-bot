from random import choice
import time

# This functions are just the greetings just helps clean up the code.
def greetings_Lyra():
    print("Welcome, I'm Lyra! The best bot assistance you will ever\nmeet. I will help you to take the best decision of your life.\nAfter this decision definetly your life will change. Mark my words!\nIn what will I help you? Hear you asking...\nIn deciding if you want to play a game or not.\n")
    print("The game is simple. You will go through a obstacle course.\nIn the obstacle course you can do one of two things jump or\nduck. The track will always be the same but the catch is how\nfast can you complete it. But don't worry you will never beat me.\n")
    print("The game will look like this.\n")
    print("This are the controls: Jump 'P' and Duck 'L'")
    print(get_mini_game_scenario(5))

# This function will provide the responses from the bot.
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

# This function just contains the posible senarios of the course.
def get_mini_game_scenario(index):
  game_scenarios = ["""
  ***********************************000****************************************
                                                                      |    |
                                                                      |    |
                                  ╳╳╳╳╳╳                              ██████
                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳


  ******************************************************************************
  """, """
  *************************************111**************************************
                                  |    |
                                  |    |
                                  ██████

                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
  ******************************************************************************
  """, """
  ************************************222***************************************

                                  ╳╳╳╳╳╳                         
                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
                                  ▆▆▆▆▆▆
                                  |    |
                                  |    |
  ******************************************************************************
  """, """
  *************************************333**************************************
      |    |                                                          |    |
      |    |                                                          |    |
      ██████                                                          ██████

                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
  ******************************************************************************
  """, """
  ************************************444***************************************
      |    |
      |    |
      ██████

                                  ╳╳╳╳╳╳                              ▆▆▆▆▆▆
                                  ╳╳╳╳╳╳                              |    |
                                  ╳╳╳╳╳╳                              |    |
  ******************************************************************************
  """, """
  ************************************555***************************************
                                                                      |    |
                                  ╳╳╳╳╳╳                              |    |
                                  ╳╳╳╳╳╳                              ██████
                                  ╳╳╳╳╳╳
      ▆▆▆▆▆▆                       
      |    |
      |    |
  ******************************************************************************
  """, """
  ************************************666***************************************

                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
      ▆▆▆▆▆▆                                                          ▆▆▆▆▆▆
      |    |                                                          |    |                       
      |    |                                                          |    |
  ******************************************************************************
  """, """
  *************************************777**************************************
                                       |    |
                               ╳ ╳╳ ╳╳╳|    |
                                ╳╳╳ ╳╳╳██████
                                  ╳╳╳╳╳╳
                                  
  

  ******************************************************************************
  """, """
  ************************************888***************************************



                                  ╳╳╳╳╳╳
                                ╳╳╳ ╳╳╳▆▆▆▆▆▆
                               ╳ ╳╳╳ ╳╳|    |
                                       |    |
  ******************************************************************************
  """, """
  *************************************999**************************************
                                       |    |
                                       |    |
                               ╳ ╳╳ ╳╳╳██████
                                  ╳╳╳╳╳╳
                                  ╳╳╳╳╳╳
                                  
  

  ******************************************************************************
  """
  ]

  print(game_scenarios[index])

def start_obstacle_course():

  # The values on this list represent the index that will be provided to the get_mini_game_scenario() to display the correct course's scenario-sequence.
  obstacle_order = [0, 1, 3, 1, 4, 2, 5, 1, 4, 2, 6, 2, 5, 1, 3, 1, 4, 2, 6, 2, 6, 2, 5, 1, 3, 1, 4, 2, 5, 1, 4, 2, 6, 2, 5, 1, 3, 1, 4, 2]

  # The values in this list represent the correct movements to complete the obstacle course without crashing.     l: duck, p: jump, t: transition, this is just a place holder
  correct_movements =   ["l", "t", "l", "t", "p", "t", "l", "t", "p", "t", "p", "t", "l", "t", "l", "t", "p", "t", "p", "t", "p", "t", "l", "t", "l", "t", "p", "t", "l", "t", "p", "t", "p", "t", "l", "t", "l", "t", "p"]

  # This value will keep changing inside the for loop to update which value inside the list it will retrive.
  obstacle_index = 0

  # Printing first game scenario to console.
  get_mini_game_scenario(obstacle_index)

  # Setting the previous_user_movement with a bigger scope to allow the program perform decisions inside the loop. The value is "middle" because user starts here.
  previous_user_movement = "middle"

  # This is when the counter starts, before starting the game.
  time.perf_counter()

  # Each iteration of the for loop the movement variable will have the correct movement.
  for movement in correct_movements:
    # The values 1 and 2 inside the obstacle_order list just represent transition scenarios inside get_mini_game_scenario() function.
    if obstacle_order[obstacle_index] == 1 or obstacle_order[obstacle_index] == 2:
      obstacle_index += 1
      time.sleep(0.3)
      get_mini_game_scenario(obstacle_order[obstacle_index])
      continue

    current_user_movement = input()
    

    # This run when user provide the correct movements.
    if current_user_movement.lower() == movement: 
      obstacle_index += 1
      get_mini_game_scenario(obstacle_order[obstacle_index])
    # This run when user provide the wrong movements.
    else: 
      # Run when wrong movement is "l".
      if current_user_movement.lower() == "l":
        user_crash_low = 8
        get_mini_game_scenario(user_crash_low)
        print("Wrong move, you crash!")
        # Will break to the for loop
        break
      # Run when wrong movement is "p".
      elif current_user_movement.lower() == "p":
        user_crash_up = 7
        get_mini_game_scenario(user_crash_up)
        print("Wrong move, you crash!")
        # Will break to the for loop.
        break
      # Run with any other wrong movment.
      else:
        # Run when the wrong movement was done at the start of the game.
        if previous_user_movement == "middle":
          user_crash_middle = 9
          get_mini_game_scenario(user_crash_middle)
          print("Wrong move, you crash!")
          # Will break to the for loop.
          break
        # In the case the user press an incorect key this will run if the user where at the botton of the track.
        elif previous_user_movement.lower() == "l":
          user_crash_low = 8
          get_mini_game_scenario(user_crash_low)
          print("You did move and crash!")
          break
        # In the case the user press an incorect key this will run if the user where at the top of the track.
        elif previous_user_movement.lower() == "p":
          user_crash_up = 7
          get_mini_game_scenario(user_crash_up)
          print("Wrong move, you crash!")
          # Will break to the for loop.
          break
          
    # This will let the program know the last movement from the user.
    previous_user_movement = current_user_movement
  
  # This print the total time elapse while user is playing the game and format the number to three decimal places.
  print(f'The total time in secons is: {time.perf_counter():.3f}')
# --------------------------------------------------------------------------------------------------------

# greetings_Lyra()
# user_response = input("Now the important decision... You want to play it? Yes or No?\n\n\n\n\n")

start_obstacle_course()