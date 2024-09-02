print('''
     start - to start the car game
     stop - to stop the car game
     quit - to exit
     NB: type help to restart
      ''')
command = ""
started = False
while command != 'quit':
   command = input('>')
   
   if command == 'start': 
    if started:
        print('car is already started')
    else:
        started = True
        print('car started......ready to go:')
        
   elif command == "stop":
       if not started:
           print('car is already stopped')
       else:
           started = False
           print('car stopped.')
    
   elif command == 'help':
    print('''
         start - to start the car game
         stop - to stop the car game
         quit - to exit
          ''')
   elif command =='quit':
    print('youve exited the game')
    break
   else:
    print('this entery doesnt match the game')
    

   

    
    
