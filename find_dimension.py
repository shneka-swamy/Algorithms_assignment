def find_dimension(p_e,h,w):

    n = len(p_e) # Length of elements in the polish expression
    stack = []
    
    for i in range(0,n):

        # if the elememt in the ith index of expression is H or V,
        #we find the height and width of rectangles of that subtree.

        if(p_e[i]=='H'or p_e[i]=='h'or p_e[i]=='v'or p_e[i]=='V'):
            value_1 = stack.pop()-1
            value_2 = stack.pop()-1

            # Using vertical formula specified in problem 1.
            if(p_e[i]=='v'or p_e[i]=='V'):
                h[value_1] = max(h[value_1],h[value_2])
                w[value_1] = w[value_1]+ w[value_2]

            else:
                h[value_1] = h[value_1]+ h[value_2]
                w[value_1] = max(w[value_1],w[value_2])

            #The value_1 is altered to represent the new rectangle
            #and the index is stored in stack.
            stack.append(value_1+1)

        else:
            stack.append(p_e[i])

    final = stack.pop()-1
    print(str(h[final]) + " X " + str(w[final]))


find_dimension([1,2,3,4,'H','V',5,6,'V','H','V'], [10,7,4,3,3,3], [5,2,5,5,3,4])

