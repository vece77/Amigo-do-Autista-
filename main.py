import datetime

class OAmigoAutista:
    def __init__(self, nome_usuario, mensalidade=29.90):
        self.usuario = nome_usuario
        self.mensalidade = mensalidade
        self.historico_compras = []
        self.produtos_seguranca = {} # Nome: {preco_base, duracao_estimada}
        
    def registrar_compra_inicial(self, data_compra, itens):
        """Simula o OCR (Leitura da Nota Fiscal)"""
        compra = {
            "data": datetime.datetime.strptime(data_compra, "%d/%m/%Y"),
            "itens": itens,
            "total": sum(item['preco'] for item in itens)
        }
        self.historico_compras.append(compra)
        
        # Mapeia produtos para monitorar duracao
        for item in itens:
            self.produtos_seguranca[item['nome']] = {
                "preco_base": item['preco'],
                "ultima_compra": compra['data']
            }
        print(f"✅ Nota Fiscal de {data_compra} processada. Total: R$ {compra['total']:.2f}")

    def prever_proxima_compra(self, dias_duracao=30):
        """Calcula a rotina e gera o alerta de reposição"""
        ultima_data = self.historico_compras[-1]['data']
        data_prevista = ultima_data + datetime.timedelta(days=dias_duracao)
        alerta_dia = data_prevista - datetime.timedelta(days=1)
        
        print(f"🕒 Piloto Automático: Sua próxima compra deve ser em {data_prevista.strftime('%d/%m/%Y')}.")
        print(f"🔔 Alerta agendado para {alerta_dia.strftime('%d/%m/%Y')}.")
        return data_prevista

    def dia_de_sorte(self, ofertas_mercado):
        """Cruza sua lista com os preços de Rio das Ostras"""
        economia_total = 0
        melhor_mercado = ""
        maior_desconto = 0
        
        print("\n🍀 Rodando 'Dia de Sorte'...")
        for mercado, produtos in ofertas_mercado.items():
            desconto_mercado = 0
            for item in produtos:
                if item['nome'] in self.produtos_seguranca:
                    preco_antigo = self.produtos_seguranca[item['nome']]['preco_base']
                    if item['preco'] < preco_antigo:
                        desconto_mercado += (preco_antigo - item['preco'])
            
            if desconto_mercado > maior_desconto:
                maior_desconto = desconto_mercado
                melhor_mercado = mercado
        
        if maior_desconto >= self.mensalidade:
            print(f"✨ VITORIA! No {melhor_mercado} você economiza R$ {maior_desconto:.2f}.")
            print(f"💰 Isso paga sua assinatura de R$ {self.mensalidade} e ainda sobram R$ {maior_desconto - self.mensalidade:.2f}!")
        else:
            print(f"📊 Economia encontrada no {melhor_mercado}: R$ {maior_desconto:.2f}.")
            
        return melhor_mercado, maior_desconto

# --- TESTE PRÁTICO (Simulando seus próximos 3 meses) ---

app = OAmigoAutista("Raphael Macaco")

# 1. Você foi ao mercado hoje e tirou foto da nota
itens_nota = [
    {"nome": "Arroz Tio Joao 5kg", "preco": 32.00},
    {"nome": "Leite Ninho", "preco": 7.50},
    {"nome": "Cafe Pilao", "preco": 18.00}
]
app.registrar_compra_inicial("05/03/2026", itens_nota)

# 2. O App calcula quando você vai precisar de novo
app.prever_proxima_compra(dias_duracao=30)

# 3. Simulação de ofertas colhidas no Instagram de mercados de Rio das Ostras
ofertas_da_semana = {
    "Multi Market": [
        {"nome": "Arroz Tio Joao 5kg", "preco": 28.00}, # R$ 4,00 de desconto
        {"nome": "Leite Ninho", "preco": 5.90}          # R$ 1,60 de desconto
    ],
    "Extra Rio das Ostras": [
        {"nome": "Arroz Tio Joao 5kg", "preco": 31.00},
        {"nome": "Cafe Pilao", "preco": 14.00}          # R$ 4,00 de desconto
    ]
}

# 4. Executando o Dia de Sorte
app.dia_de_sorte(ofertas_da_semana)
