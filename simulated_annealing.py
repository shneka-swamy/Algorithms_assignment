import random
import calcarea

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

def oper_opra(p_e,opr):
    i = 0
    while(i<len(p_e)):
        i+=1
        if(not( p_e[i-1] == '+' or p_e[i-1] == '*')):
            if(i<len(p_e) and (p_e[i] == '+' or p_e[i] == '*')):
                opr.append(i-1)
        else:
            if(i<len(p_e) and (not(p_e[i] == '+' or p_e[i]=='*'))):
                opr.append(i-1)
        
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

    
def move_three (p_e, opr):
    ran = opr[random.randint(0,len(opr)-1)]

    no_oper = 0
    no_operand = 0
    flag = True
    
    if(p_e[ran] == '+' or p_e[ran] == '*'):
        if(p_e[ran] != p_e[ran+2]):
            dup = p_e[ran]
            p_e[ran] = p_e[ran+1]
            p_e[ran+1] = dup
    else:
        if(p_e[ran+1] != p_e[ran-1]):
            for i in range(0,ran+1):
                if(p_e[i] == '+' or p_e[i] == '*'):
                    no_oper+=1
                else:
                    no_operand +=1
                if(no_operand  <= no_oper+1):
                    flag = False
                    break
            if(flag):
                dup = p_e[ran]
                p_e[ran] = p_e[ran+1]
                p_e[ran+1] = dup

    
def simulated(p_e, h_w):
    calcarea.optimal_solution(p_e, h_w)
    for i in range(1,100):
        adj = []
        oi = []
        opr = []
        adj_operand(p_e,adj)
        
        operator_index(p_e,oi)
    
        choice = random.randint(1,3)

        if(choice ==1):
            move_one (p_e,adj)
            calcarea.optimal_solution (p_e, h_w)
            print(p_e)
        elif(choice == 2):
            move_two (p_e, oi)
            calcarea.optimal_solution (p_e, h_w)
            print(p_e)
        else:
            opr[:] = []
            oper_opra(p_e, opr)
            move_three (p_e, opr)
            calcarea.optimal_solution (p_e, h_w)
            print(p_e)
      


simulated([1,2,3,4,'+','*',5,6,'*','+','*'],
                 [(5,10),(7,2),(5,4),(3,5),(3,3),(4,3)])
