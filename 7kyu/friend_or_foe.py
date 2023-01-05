def friend(x):
    friend_list = []
    friend_list_final = []

    for i in x:
        if len(i) == 4:
            friend_list.append(i) 
            
    for j in friend_list:
        num_check = j.isalpha()
        if num_check == True:
            friend_list_final.append(j)
            
    return friend_list_final