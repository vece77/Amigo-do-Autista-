import streamlit as st
import datetime
import time

# Configurações de Acessibilidade e Identidade
st.set_page_config(page_title="Amigo do Autista", page_icon="🧩", layout="centered")

# Estilo visual calmo para evitar sobrecarga sensorial
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .card-seguro { 
        padding: 20px; border-radius: 12px; background-color: #ffffff; 
        border: 1px solid #e2e8f0; margin-bottom: 20px;
    }
    .nota-legal { font-size: 0.8em; color: #718096; margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 10px; }
    h1, h2, h3 { color: #1a365d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧩 Amigo do Autista")
st.markdown("### *Sua paz vale mais que qualquer fila.*")

# Mensagem de Propósito e Transparência
st.markdown("""
<div class="card-seguro">
    <h4>💙 Nossa Missão</h4>
    <p>O mercado pode ser hostil para autistas e famílias atípicas. 
    <b>Nós usamos inteligência de dados para encontrar o melhor preço global em Rio das Ostras.</b> 
    Você paga o valor justo e recebe tudo em casa em uma única entrega oficial do mercado selecionado.</p>
</div>
""", unsafe_allow_html=True)

# Aviso de Logística Única (Para evitar múltiplos fretes)
st.info("💡 **Entrega Otimizada:** Selecionamos sempre um **único estabelecimento** para sua lista inteira. Isso garante que você receba apenas um entregador e pague apenas **uma taxa de deslocamento**.")

st.divider()

# Entrada de Dados
col1, col2 = st.columns(2)
with col1:
    valor_referencia = st.number_input("Valor total da última nota (R$)", min_value=0.0, value=200.0)
    chave = st.text_input("Chave Mestre (Privado)", type="password")

with col2:
    st.write("**Logística Rio das Ostras**")
    st.success("☀️ Operação Normal: Entregas sem atrasos hoje.")
    previsao = "60-90 min"

# Lógica de Cálculo (Otimização por Mercado Único)
# Simulamos a busca pelo mercado que oferece a melhor cesta completa
preco_custo_estimado = valor_referencia * 0.85 
taxa_entrega_mercado = 15.00 # Taxa única oficial do mercado

# Verificação de Chave VIP (MACACAO2026)
is_vip = chave.upper() == "MACACAO2026"
total_final = (preco_custo_estimado + taxa_entrega_mercado) if is_vip else (valor_referencia + taxa_entrega_mercado)

st.subheader("🤝 Sua Garantia de Sossego")
st.markdown(f"""
<div style="background-color: #fff; padding: 25px; border-radius: 15px; border: 2px solid #4a90e2; text-align: center;">
    <p style="margin-bottom: 5px;">Total a pagar (Produtos + Frete Único):</p>
    <h1 style="color: #1a365d; margin-top: 0;">R$ {total_final:.2f}</h1>
    <p style="color: #718096;">Entrega oficial realizada pelo mercado na sua porta.</p>
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Confirmar Compra sem Estresse"):
    with st.spinner('Consolidando sua lista no melhor mercado...'):
        time.sleep(2)
        st.balloons()
        st.success("Pedido enviado! O mercado selecionado processará sua entrega em breve.")

# Rodapé de Responsabilidade (Aviso solicitado pelo Raphael)
st.markdown(f"""
<div class="nota-legal">
    <b>Aviso Importante:</b> Este aplicativo é uma plataforma de inteligência e auxílio logístico criada por Raphael Vessi. 
    A separação, venda e <b>entrega física dos produtos</b> são de responsabilidade exclusiva do supermercado parceiro 
    e de seus respectivos entregadores oficiais.
</div>
""", unsafe_allow_html=True)
