# 1. Nossa base de dados: Uma lista contendo vários dicionários
lista_pacientes = [
    {"nome": "João", "idade": 65},
    {"nome": "Ana", "idade": 42},
    {"nome": "Carlos", "idade": 72},
    {"nome": "Maria", "idade": 30},
    {"nome": "Dona Sebastiana", "idade": 88},
    {"nome": "Lucas", "idade": 19}, 
    {"nome": "Antonio", "idade": 75},
    {"nome": "Fernanda", "idade": 65}
    ]

# 2. Criando o novo arquivo de relatório
with open("relatorio_avancado.txt", "w", encoding="utf-8") as arquivo:
    
    # Cabeçalho
    arquivo.write("SISTEMA HOSPITALAR - Versão 2.0\n")
    arquivo.write("=" * 45 + "\n")
    arquivo.write("PACIENTES PRIORITÁRIOS (A PARTIR DE 60 ANOS):\n\n")
    
    contador = 0
    
    # 3. O Loop: Passando por cada paciente da nossa lista
    for paciente in lista_pacientes:
        
        # Como 'paciente' agora é um dicionário, pegamos a idade assim:
        if paciente["idade"] >= 60:
            
            # Pegamos o nome e a idade usando as chaves do dicionário
            nome_paciente = paciente["nome"]
            idade_paciente = paciente["idade"]
            
            # Escrevemos a linha formatada no arquivo
            arquivo.write(f"- {nome_paciente} ({idade_paciente} anos) -> ENCAMINHAR PARA GERIATRIA\n")
            contador += 1
            
    # Rodapé
    arquivo.write("\n" + "=" * 45 + "\n")
    arquivo.write(f"Total de atendimentos prioritários: {contador}\n")

# 4. Mensagem de sucesso no terminal
print("Sucesso! O arquivo 'relatorio_avancado.txt' foi gerado com os nomes dos pacientes.")