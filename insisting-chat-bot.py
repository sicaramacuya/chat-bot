from random import choice
import time

# This functions are just the greetings just helps clean up the code.
def greetings_Lyra():
    print()
    print("Welcome, I'm Lyra! The best bot assistance you will ever meet. I will help you to take the best decision of your life.\nAfter this decision definetly your life will change. Mark my words! In what will I help you? Hear you asking... Basically\ndeciding if you want to play a game or not.\n")
    # time.sleep(7.5)
    print("The game is simple. You will go through a obstacle course. In the obstacle course you can do one of two things jump or\nduck. The track will always be the same but the catch is how fast can you complete it.\n")
    # time.sleep(5)
    print("The game will look like this.\n")
    # time.sleep(0.5)
    print("This are the controls: Jump 'P' and Duck 'L'")
    get_mini_game_scenario(5)

# This function will provide the responses from the bot.
def get_bot_response(user_response, sequence_events):
  # # This will help vary the answers even more.
  # sequence_events = 0

  # bot responses
  bot_response_play_first_round = ["Great, let's play!"]
  bot_response_play_consecutive_round = ["Perfect, don't leave me alone. Keep playing!", "Once more? Excellent.", "Again? This is great, lets see how you perform this time.", "You know you would never beat my record? I'm too good.", "Perfect, let me set the game for you.", "Ha!, lets see how 'good' you are..."]
  bot_respond_insisting_first_round = ["Are you really not going to play? Please say yes!"]
  bot_respond_insisting_consecutive_round = ["Really? You know, I'll wait for you to say yes.", "Yes, yes, yes, yes... There is what you should respond.", "Don't worry just play one. I promise it will be the last.", "Still waiting for you to say yes.", "If you want to go I understand but lets play this last. Belive me this will be really the last one.", "Why not? It will be fun. Just say yes.", "You know I'm pretty persistant. I can be here asking all day."]

  if user_response.lower() == "no" and sequence_events == 0:
    sequence_events += 1
    start_game = False
    # print("TEST 1")
    print(choice(bot_respond_insisting_first_round))
    return(start_game)
  elif user_response.lower() == "no" and sequence_events > 0:
    sequence_events += 1
    start_game = False
    # print("TEST 2")
    print(choice(bot_respond_insisting_consecutive_round))
    return(start_game)
  elif user_response.lower() == "yes" and sequence_events == 0:
    sequence_events += 1
    start_game = True
    # print("TEST 3")
    print(choice(bot_response_play_first_round))
    return(start_game)
  elif user_response.lower() == "yes" and sequence_events > 0:
    sequence_events += 1
    start_game = True
    # print("TEST 4")
    print(choice(bot_response_play_consecutive_round))
    return(start_game)

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

# This function contains the obstacle course game and the logics of it.
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
  total_amount_playing = time.perf_counter()

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
  
  # This will calculate the total time playing. The order is important final time minus the initial time.
  total_amount_playing = time.perf_counter() - total_amount_playing

  # This print the total time elapse while user is playing the game and format the number to three decimal places.
  print(f'The total time in secons is: {total_amount_playing:.3f}')
# --------------------------------------------------------------------------------------------------------

greetings_Lyra()
print("Now the important decision... You want to play it? Yes or No?")

#This will help vary the answers inside the get_bot_response() function.
sequence_events = 0

while True: 
  user_response = input()

  if user_response.lower() == "no":
    start_game = get_bot_response(user_response, sequence_events)

  elif user_response.lower() == "yes":
    print("\n\n\nREMEMBER: This are the controls: Jump 'P' and Duck 'L'")
    start_obstacle_course()
    print("Do you want to play again?") #######

  sequence_events += 1
