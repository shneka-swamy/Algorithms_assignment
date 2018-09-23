#This is to form the left and right subarray in the increasing order of width
def make_list(sub_array, h_w, index):

    if (h_w[index][0] > h_w[index][1]):
        sub_array.append(h_w[index])
        sub_array.append((h_w[index][1], h_w[index][0]))

    elif(h_w[index][0] < h_w[index][1]):
        sub_array.append((h_w[index][1], h_w[index][0]))
        sub_array.append(h_w[index])

    else:
        sub_array.append(h_w[index])

#This is to join the blocks based on stockmeyers algorithm (when Vertical cut is encountered)
def join_vertical(temp , Left, Right, val):
    inter = []
    k = len(Left)
    m = len(Right)
    i = 0
    j = 0

    while(i<k and j<m):
        inter.append((max(Left[i][0],Right[j][0]), Left[i][1]+Right[j][1]))
        if(Left[i][0] > Right[j][0]):
            i = i+1
        elif(Left[i][0] < Right[j][0]):
            j = j+1
        else:
            i = i+1
            j = j+1
    temp[val] = inter

#This is to join the blocks based on stockmeyers algorithm (when Horizontal cut is encountered)
def join_horizontal(temp , Left, Right,val):
    inter = []
    i = len(Left) - 1
    j = len(Right) - 1

    while(i>=0 and j>=0):
        inter.append((Left[i][0]+Right[j][0],max(Left[i][1],Right[j][1])))
        if(Left[i][1] > Right[j][1]):
            i = i-1
        elif(Left[i][1] < Right[j][1]):
            j = j-1
        else:
            i = i-1
            j = j-1
    temp[val] = inter

def bt_vertical(lt_tree,L,R,refer):
    k = len(L)
    m = len(R)
    i =0
    j = 0

    while(i<k and j<m):
        value = (max(L[i][0],R[j][0]), L[i][1]+R[j][1])
        if(refer[0]== value[0] and refer[1]== value[1]):
            lt_tree.append((L[i][0],L[i][1]))
            lt_tree.append((R[j][0],R[j][1]))
            break
        else:
            if(L[i][1] > R[j][1]):
                i = i-1
            elif(L[i][1] < R[j][1]):
                j = j-1
            else:
                i = i-1
                j = j-1

def bt_horizontal(lt_tree,L,R,refer):
    i = len(L) - 1
    j = len(R) - 1

    while(i>=0 and j>=0):
        value = (L[i][0]+R[j][0],max(L[i][1],R[j][1]))
        if(refer[0]== value[0] and refer[1]== value[1]):
            lt_tree.append((L[i][0],L[i][1]))
            lt_tree.append((R[j][0],R[j][1]))
            break
        else:
            if(L[i][1] > R[j][1]):
                i = i-1
            elif(L[i][1] < R[j][1]):
                j = j-1
            else:
                i = i-1
                j = j-1
    
            
        

def topdown(expr, temp, h_w, t_d, orientation):
    n = len(expr)
    L = []
    R = []
    lt_tree = []

    for i in range(0,n,3):
        L[:] = []
        R[:] = []
        flag_1 = 0
        flag_2 = 0
        lt_tree[:] = []

        refer = t_d.pop()

        if(type(expr[i]) == int):
           make_list(L,h_w,expr[i]-1)
           flag_1 = 1
        else:
           L = temp[int(expr[i][1])]

        if(type(expr[i+1])== int):
            make_list(R,h_w,expr[i+1]-1)
            flag_2 = 1
        else:
            R = temp[int(expr[i+1][1])]
            

        if(expr[i+2] == 'v' or expr[i+2] == 'V'):
            bt_vertical(lt_tree,L,R,refer)
            #print(lt_tree)
        else:
            bt_horizontal(lt_tree,L,R,refer)
            #print(lt_tree)
            
        #To check for the presence of leaf node

        if(flag_1 == 1 and flag_2 == 1):
            if(h_w[expr[i]-1][0] != lt_tree[0][0]):
                orientation[expr[i]-1] = 1
            if(h_w[expr[i+1]-1][0] != lt_tree[1][0]):
                orientation[expr[i+1]-1] = 1
        elif(flag_1 == 1):
            if(h_w[expr[i]-1][0] != lt_tree[0][0]):
                orientation[expr[i]-1] = 1
            t_d.append(lt_tree[1])
        elif(flag_2 == 1):
            if(h_w[expr[i+1]-1][0] != lt_tree[1][0]):
                orientation[expr[i+1]-1] = 1
            t_d.append(lt_tree[0])
        else:
            t_d.append(lt_tree[0])
            t_d.append(lt_tree[1])
    print("\n")
    print("'1' refers to rotate the block, '0' refers to maintain the block")
    print("The reqired orientation is,")
    print(orientation)
        
def optimal_solution (p_e,h_w):

    val = 0
    n = len(p_e) 
    m = (n-1)/2 #finds the number of internal nodes
    Left = []
    Right = []
    stack = []
    index = (m*3) - 1 # this is used for forming the array required for top-down tree approach
    expr = [0]*(m*3) # Top- down array formed
    temp = [[]]*m # This a list of list for storing the list at internal nodes.

    orientation = [0]*(m+1)
    # Bottom- up part of the code
    for i in range(0,n):
        Left[:] = []
        Right[:] = []
            
        if(p_e[i]=='v'or p_e[i]=='V'or p_e[i]=='h'or p_e[i]=='H'):

            ri = stack.pop()
            le = stack.pop()

            # To create the list for top - down traversal
            expr[index] = p_e[i]
            index -= 1
            expr[index] = ri
            index -= 1
            expr[index] = le
            index-= 1


            inter_vert = []
            inter_hori = []

            # when the node popped out is integer then the node encountered is a leaf node
            # otherwise, the node is an internan node.
            # All the internal node with V or H are converted to D0, D1, D2, ... Dn for the sake of calculation)
                
            if(p_e[i]=='v'or p_e[i]=='V'):
                if(type(le) == int and type(ri) == int):
                    make_list(Left, h_w, le-1)
                    make_list(Right, h_w, ri-1)
                    join_vertical(temp,Left,Right,val)
                elif(type(le) != int and type(ri) == int):
                    make_list(Right, h_w, ri-1)
                    join_vertical(temp,temp[int(le[1])],Right,val)
                elif(type(le) == int and type(ri)!= int):
                    make_list(Left, h_w, le-1)
                    join_vertical(temp,Left,temp[int(ri[1])],val)
                else:
                    join_vertical(temp,temp[int(le[1])],temp[int(ri[1])],val)

                #print(temp)
                
            elif(p_e[i]=='h' or p_e[i] == 'H'):
                if(type(le) == int and type(ri) == int):
                    make_list(Left, h_w, le-1)
                    make_list(Right, h_w, ri-1)
                    join_horizontal(temp,Left,Right,val)
                elif(type(le) != int and type(ri) == int):
                    make_list(Right, h_w, ri-1)
                    join_horizontal(temp,temp[int(le[1])],Right,val)
                elif(type(le) == int and type(ri)!= int):
                    make_list(Left, h_w, le-1)
                    join_horizontal(temp,Left,temp[int(ri[1])],val)
                else:
                    join_horizontal(temp,temp[int(le[1])],temp[int(ri[1])],val)
                #print(temp)
        
            stack.append('D'+str(val))
            val+=1

        #when the node is a number just append it to the stack
        else:
            stack.append(p_e[i])

    # This part is used to find the final efficient height and width after the traversal of the tree.
    height = 0
    width = 0
    area_min = float("inf")
    for k in range(0,len(temp[m-1])):
        area = temp[m-1][k][0] * temp[m-1][k][1]
        if(area_min > area):
            area_min = area
            height = temp[m-1][k][0]
            width = temp[m -1][k][1]

    
    print("The efficient height and width are  "+str(height)+" X "+str(width))
    #print(expr)

    t_d = [(height,width)]
    topdown(expr, temp, h_w, t_d, orientation)
                   
                   
    
#optimal_solution([1,2,3,'V',4,'V','V'],[(5,2),(5,4),(5,6),(5,7)])
#optimal_solution([1,2,'H',3,4,'H','V'],[(2,4),(3,4),(2,4),(3,4)])      
optimal_solution([1,2,3,4,'H','V',5,6,'V','H','V'],
                 [(5,10),(7,2),(5,4),(3,5),(3,3),(4,3)])
