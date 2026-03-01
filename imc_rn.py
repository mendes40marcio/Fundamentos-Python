while True:
    try:
        sexo = input("Informe o sexo (M/F): ").strip().upper()
        idade = int(input("Informe a idade em meses: "))
        altura = float(input("Informe a altura em metros: "))
        peso = float(input("Informe o peso em kg: "))

        if altura <= 0 or peso <= 0 or idade < 0:
            print("Valores inválidos. Tente novamente.\n")
            continue

        imc = peso / (altura ** 2)

        # Classificação aproximada para bebês até 12 meses
        if idade <= 12:
            if imc < 13:
                classificacao = "Magreza"
            elif 13 <= imc <= 18:
                classificacao = "Eutrofia (normal para idade)"
            else:
                classificacao = "Acima do esperado para idade"
        else:
            classificacao = "Tabela específica necessária para essa idade"

        print("\n----- RESULTADO -----")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        print("---------------------")

        break

    except ValueError:
        print("Digite valores válidos.\n")
