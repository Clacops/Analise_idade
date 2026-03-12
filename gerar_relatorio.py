lista_pacientes = [12, 65, 30, 72, 45, 88, 19, 60]

with open("relatorio_triagem.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("SISTEMA DE GESTAO HOSPITALAR - TRIAGEM\n")
    arquivo.write("========================================\n")
    arquivo.write("LISTA DE PACIENTES PRIORITARIOS:\n\n")

    contador = 0

    for idade in lista_pacientes:
        if idade >= 60: 
            arquivo.write(f"- Paciente com {idade} anos: ENCAMINHAR SETOR A\n")
            contador = contador + 1

    arquivo.write("========================================\n")
    arquivo.write(f"Total de prioridades encontradas: {contador}\n")

print("Processamento concluido! Verifique o arquivo relatorio_triagem.txt")