#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.


open_list = ["[","{","("] 
close_list = ["]","}",")"] 

def isBalanced(brackets):

    pilha = []

    # Loop
    for bracket in brackets:

        # Se houver bracket na open_list
        if bracket in open_list:
            # Add bracket na pilha
            pilha.append(bracket)
        
        # Se houver bracket na close_list
        elif bracket in close_list:

            # Cria variavel com index do bracket na 'close_list'
            pos = close_list.index(bracket)

            # Condição bem especifica para utilização do pop()
            if ((len(pilha) > 0) and (open_list[pos] == pilha[len(pilha)-1])):
                pilha.pop()
            else:
                return "[-] Desbalanceada"


    # Condição para o tamanho da pilha
    if len(pilha) == 0:
        return "[+] Balanceada"
    else:
        return "[-] Desbalanceada"


# Definindo strings e fazendo testes
string = "{[()]}"
print(string,"-", isBalanced(string)) 
  
string = "{[(])}"
print(string,"-", isBalanced(string)) 
  
string = "{{[[(())]]}}"
print(string,"-",isBalanced(string))



if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
