while True:
    #Entrada do CPF
    cpf_original = input("Insira o CPF para consulta: ")
    cpf_separado = []
    multiplicador1 = 10
    multiplicador2 = 11
    somatoria_cpf = 0
    somatoria2_cpf = 0

    #Percorre o CPF digitado filtrando pelos números
    for numeros in cpf_original:
        try:
                cpf_separado.append(int(numeros))
        except:
                next  

    #Executa o cálculo de multiplicação onde x = somat (n * y-1) sendo y = 10.
    limite1 = range(8)
    for unidade in limite1:
        somatoria_cpf = somatoria_cpf + (cpf_separado[unidade] * multiplicador1)
        multiplicador1 -= 1
        unidade += 1  

    #Multiplicando o resultado x10 e encontrado o resto da divisão por 11
    digito1_calculado = (somatoria_cpf * 10) % 11 

    #Verifica o valor do primerio digito para o CPF.
    if digito1_calculado <= 9:
          digito1_esperado = digito1_calculado
    else:
          digito1_esperado = 0
    #Repete o procecesso para o segundo digito
    limite2 = range(10)
    for unidade in limite2:
        somatoria2_cpf = somatoria2_cpf + (cpf_separado[unidade] * multiplicador2)
        multiplicador2 -= 1
        unidade += 1  

    #Multiplicando o resultado x10 e encontrado o resto da divisão por 11
    digito2_calculado = (somatoria2_cpf * 10) % 11 

    #Verifica o valor do primerio digito para o CPF.
    if digito2_calculado <= 9:
          digito2_esperado = digito2_calculado
    else:
          digito2_esperado = 0

    if digito1_esperado == cpf_separado[9] and digito2_esperado == cpf_separado[10]:
        print("Este CPF é válido")  
    else:
        print("CPF inválido")
        
    
        