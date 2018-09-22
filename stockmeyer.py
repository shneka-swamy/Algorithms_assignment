def make_list(sub_array, h_w, index):

    if (h_w[index][0] > h_w[index][1]):
        sub_array.append(h_w[index])
        sub_array.append((h_w[index][1], h_w[index][0]))

    elif(h_w[index][0] < h_w[index][1]):
        sub_array.append((h_w[index][1], h_w[index][0]))
        sub_array.append(h_w[index])

    else:
        sub_array.append(h_w[index])

def join_vertical(temp, Left, Right, val):
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

def join_horizontal(temp, Left, Right, val):
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

def optimal_solution (p_e,h_w):

    val = 0
    n = len(p_e)
    m = (n-1)/2
    Left = []
    Right = []
    stack = []
    temp = [[]]*m
    

    for i in range(0,n):
        Left[:] = []
        Right[:] = []
            
        if(p_e[i]=='v'or p_e[i]=='V'or p_e[i]=='h'or p_e[i]=='H'):

            ri = stack.pop()
            le = stack.pop()

            if(type(le) == int):
                make_list(Left, h_w, le-1)
                print(Left)
            else:
                Left = temp[int(le[1])]
                print(Left)
                                
            if(type(ri)== int):
                make_list(Right, h_w, ri-1)
                print(Right)
            else:
                Right = temp[int(ri[1])]
                print(Right)

            if(p_e[i]=='v'or p_e[i]=='V'):
                join_vertical(temp,Left,Right,val)
                print(temp)
            else:
                join_horizontal(temp,Left,Right,val)
                print(temp)
        
            stack.append('D'+str(val))
            val+=1

        else:
            stack.append(p_e[i])

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
                   
                   
    

        
optimal_solution([1,2,3,4,'H','V',5,6,'V','H','V'],
                 [(10,5),(7,2),(4,5),(3,5),(3,3),(3,4)])

