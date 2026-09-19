list_num=int(input("Введите колличество чисел для заполнения списка:"))

while True:
    list_robot=list(map(int, input("введите значения через пробел:").split()))
    
    list_result = [list_robot[0]] 
    best_result = [list_robot[0]]
    sh_num=1
    sh_max=sh_num
    for i in range (len(list_robot)-1):
        if list_robot[i]<list_robot[i+1]:
            sh_num+=1
            list_result.append(list_robot[i+1])
            if sh_max<sh_num:
                sh_max=sh_num
                best_result = list_result.copy()
        else:
            sh_num=1
            list_result = [list_robot[i+1]]
           
   
            
    print(sh_max)
    print(best_result)
    if (len(list_robot))==list_num:
        break

   