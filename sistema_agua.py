from colorama import init, Fore, Style

# Inicializa o colorama (necessário, especialmente no Windows)
init()

def definir_cor_nivel(nivel):
    """
    Função responsável por associar o nível à cor e mensagem correspondente.
    """
    # Lista com as mensagens de situação conforme o índice (Nível - 1)
    situacoes = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                 # Nível 2
        "Médio",                 # Nível 3
        "Alto",                  # Nível 4
        "Muito alto (alerta)"    # Nível 5
    ]
    
    # Lista com as cores correspondentes aos níveis
    cores = [
        Fore.RED,     # Nível 1
        Fore.YELLOW,  # Nível 2
        Fore.GREEN,   # Nível 3
        Fore.CYAN,    # Nível 4
        Fore.BLUE     # Nível 5
    ]

    # Ajuste de índice (Nível 1 é o índice 0)
    idx = nivel - 1

    if 0 <= idx < len(situacoes):
        cor_escolhida = cores[idx]
        mensagem = situacoes[idx]
        print(f"{cor_escolhida}Nível {nivel}: {mensagem}{Style.RESET_ALL}")
    else:
        print("Nível fora do intervalo de monitoramento.")

# --- Simulação do Sistema ---
def executar_monitoramento():
    print("--- MONITORAMENTO DE RESERVATÓRIO ---")
    
    # Simulando os 5 níveis descritos no projeto
    niveis_simulados = [1, 2, 3, 4, 5]

    for nivel in niveis_simulados:
        definir_cor_nivel(nivel)

if __name__ == "__main__":
    executar_monitoramento()
