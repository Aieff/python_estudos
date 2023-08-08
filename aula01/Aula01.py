#Converta o valores de Real para Dólar

def real_para_dolar(valor_em_real, taxa_de_cambio):
    valor_em_dolar = valor_em_real / taxa_de_cambio
    return valor_em_dolar

def main():
    taxa_de_cambio = 5.30  #Taxa de câmbio atual (valor aproximado)
    
    valor_em_real = float(input("Digite o valor em reais: "))
    
    valor_em_dolar = real_para_dolar(valor_em_real, taxa_de_cambio)
    
    print(f"R$ {valor_em_real:.2f} equivale a ${valor_em_dolar:.2f} dólares americanos.")

if __name__ == "__main__":
    main()