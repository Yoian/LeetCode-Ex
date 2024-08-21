lista_input=[1,4,2,3,5]
target=4


for i in range(len(lista_input)):
    for j in range(i+1,len(lista_input)):
        if lista_input[i]+lista_input[j] == target:
            lista_output=[i,j]
            print(lista_output,lista_input[i],lista_input[j])
            break
    if lista_input[i]+lista_input[j] == target: break

            