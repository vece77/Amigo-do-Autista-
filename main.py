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
    h1, h2, h3 { color: #1a365d; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧩 Amigo do Autista")
st.markdown("### *Sua paz vale mais que qualquer fila.*")

# Mensagem de Propósito (Apelo Emocional)
st.markdown("""
<div class="card-seguro">
    <h4>💙 Por que este app existe?</h4>
    <p>O mercado pode ser um ambiente hostil para autistas e mães atípicas. O barulho, as luzes e a falta de empatia geram um desgaste desnecessário. 
    <b>Nós garantimos que você pague o mesmo valor da sua última nota fiscal</b>, enquanto cuidamos de toda a logística para você receber tudo em casa, com segurança e silêncio.</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Entrada de Dados
col1, col2 = st.columns(2)
with col1:
    valor_referencia = st.number_input("Valor total da última nota (R$)", min_value=0.0, value=200.0)
    chave = st.text_input("Chave Mestre (Opcional)", type="password")

with col2:
    st.write("**Logística Rio das Ostras**")
    st.info("☀️ Operação Normal: Entregas sem atrasos hoje.")
    previsao = "60-90 min"

# Lógica de Cálculo (Arbitragem de Preço)
preco_custo_estimado = valor_referencia * 0.85
taxa_entrega = 15.00

# Verificação de Chave VIP
is_vip = chave.upper() == "MACACAO2026"
total_final = (preco_custo_estimado + taxa_entrega) if is_vip else (valor_referencia + taxa_entrega)

st.subheader("🤝 Nossa Proposta")
st.markdown(f"""
<div style="background-color: #fff; padding: 25px; border-radius: 15px; border: 2px solid #4a90e2; text-align: center;">
    <p style="margin-bottom: 5px;">Você paga o valor da nota + entrega:</p>
    <h1 style="margin-top: 0;">R$ {total_final:.2f}</h1>
    <p style="color: #718096;">Previsão: {previsao} | Entrega na sua porta</p>
</div>
""", unsafe_allow_html=True)

if st.button("🚀 Confirmar Compra sem Estresse"):
    with st.spinner('Garantindo o melhor preço para você...'):
        time.sleep(2)
        st.balloons()
        st.success("Pedido confirmado! Pode relaxar. Nós cuidamos do mercado por você.")
