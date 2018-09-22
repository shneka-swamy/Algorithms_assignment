def find_dimension(p_e,h,w):
    n = len(p_e)
    stack = []

    for i in range(0,n):
        if(p_e[i]=='H'or p_e[i]=='h'or p_e[i]=='v'or p_e[i]=='V'):
            value_1 = stack.pop()-1
            value_2 = stack.pop()-1

            if(p_e[i]=='v'or p_e[i]=='V'):
                h[value_1] = max(h[value_1],h[value_2])
                w[value_1] = w[value_1]+ w[value_2]

            else:
                h[value_1] = h[value_1]+ h[value_2]
                w[value_1] = max(w[value_1],w[value_2])

            stack.append(value_1+1)
            #print(stack)

        else:
            stack.append(p_e[i])
            #print(stack)

    final = stack.pop()-1
    print(str(h[final]) + " X " + str(w[final]))


find_dimension([2,3,'H',1,'V'],[5,2,3],[4,3,3])
