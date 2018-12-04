import random

def adj_operand(p_e, adj):
    # To get all the operators adjacent to each other as a list
    size = len(p_e)

    for i in range(size):
        if (not (p_e[i] == '*' or p_e[i]== '+')):
            adj.append(p_e[i])

def operator_index(p_e, oi):
    #To get the index of the first operators of a chain of operators
    size = len(p_e)
    i = 0

    while(i<size):
        if(p_e[i] == '*' or p_e[i] == '+'):
            oi.append(i)
            while(i<size and (p_e[i] == '*' or p_e[i] == '+')):
                i+=1
        i+=1
def move_one (p_e, adj):
    # Swap Adjacent operators
    size = len(adj)

    # Randaomly choose an operand to swap
    random_choice = random.randint(0, size-1)
    swap_choice = random_choice
    random_move = random.randint(0,1)
    
    # Randomly choose to move left or right in the list to choose the adjacent operand
    if(random_move == 0):
        swap_choice -= 1
        if (swap_choice == -1):
            swap_choice = random_choice + 1
    else:
        swap_choice+= 1
        if(swap_choice == size):
            swap_choice = random_choice -1

    # Swap the operands in the polish expression and list
    d = adj[random_choice]
    ind_1 = p_e.index(d)
    ind_2 = p_e.index(adj[swap_choice])

    p_e[ind_1] = adj[swap_choice]
    adj[random_choice] = adj[swap_choice]

    p_e[ind_2] = d
    adj[swap_choice] = d

    
def move_two (p_e, oi):
    # Randomly choose the chain to change
    ran = random.randint(0,len(oi) -1)
    random_choice = oi[ran]

    # Complement the signs of the operators
    while(random_choice< len(p_e) and (p_e[random_choice] == '+' or p_e[random_choice] == '*')):
        if(p_e[random_choice] == '+'):
            p_e[random_choice] = '*'
        else:
            p_e[random_choice] = '+'
        random_choice +=1

    
def move_three (p_e, h, w):
    print("In move three")

    
def simulated(p_e, h, w):
  adj = []
  oi = []
  adj_operand(p_e,adj)
  print (adj)
  operator_index(p_e,oi)
  print(oi)
  #choice = random.randint(1,3)
  print(p_e)
  choice = 1
  while(choice <3):
      move_one (p_e,adj)
      print(p_e)
      print(adj)
      choice+=1
  #elif(choice == 2):
     # move_two (p_e, oi)
     # print(p_e)
  #else:
   #   move_three (p_e, h, w)
      


simulated([1,2,3,4,'+','*',5,6,'*','+','*'], [10,7,4,3,3,3], [5,2,5,5,3,4]) 
