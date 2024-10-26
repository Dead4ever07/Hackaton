from datetime import datetime, timedelta

def proximo_dia(data):
    # Converte a string de data para um objeto datetime
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    # Adiciona um dia
    proximo_dia = data_formatada + timedelta(days=1)
    # Retorna a data no formato desejado
    return proximo_dia.strftime('%Y-%m-%d')

# Exemplo de uso
data_atual = '2024-10-26'
print(proximo_dia(data_atual))