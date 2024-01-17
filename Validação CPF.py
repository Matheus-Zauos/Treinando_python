import re
while True:
    #Entrada do CPF
    cpf_original = input("Insira o CPF para consulta: ")
    cpf_filtrado = ''
    multiplicadorx10 = 10
    multiplicadorx11 = 11
    soma_cpf_sem_um_dgto = 0
    som_cpf_com_um_dgto = 0

    #Faz a tratativa da string de input verificando se está entre 0 e 9
    cpf_filtrado = re.sub(r'[^0-9]',
                           '',
                        cpf_original)
    
    tamanho_da_string = len(cpf_filtrado)

    if tamanho_da_string == 0: cpf_filtrado = '123456789' 

    #Verifica se não há repetição de numeros
    primeiro_num_cpf = cpf_filtrado[0]
    busca_repeticao = primeiro_num_cpf * len(cpf_filtrado)

    if busca_repeticao == cpf_filtrado: 
        cpf_filtrado = '123456789'

    cpf_sem_digitos = cpf_filtrado[:9]
    cpf_com_um_digito = cpf_filtrado[:10]
    
    #Executa o cálculo de multiplicação onde x = somat (n * y-1) sendo y = 10.
    for numero in cpf_sem_digitos:
        soma_cpf_sem_um_dgto = soma_cpf_sem_um_dgto + int(numero) * multiplicadorx10
        multiplicadorx10 -= 1
            
    #Multiplicando o resultado x10 e encontrado o resto da divisão por 11
    digito1_calculado = (soma_cpf_sem_um_dgto * 10) % 11

    #Repete o procecesso para o segundo digito
    for numero in cpf_com_um_digito:
        som_cpf_com_um_dgto = som_cpf_com_um_dgto + int(numero) * multiplicadorx11
        multiplicadorx11 -= 1
         
    #Multiplicando o resultado x10 e encontrado o resto da divisão por 11
    digito2_calculado = (som_cpf_com_um_dgto * 10) % 11 

    #Verifica o valor do primerio digito para o CPF.
    if digito1_calculado <= 9: digito1_esperado = digito1_calculado         
    else: digito1_esperado = 0

    #Verifica o valor do segundo digito para o CPF.
    if digito2_calculado <= 9: digito2_esperado = digito2_calculado         
    else: digito2_esperado = 0
          
    if (digito1_esperado == int(cpf_filtrado[-2]) 
        and digito2_esperado == int(cpf_filtrado[-1])): 
        print("Este CPF é válido")           
    else:  print("Este CPF é inválido")    