import streamlit as st
import time

# 1. Configuração de Design Sensorial (Cores Suaves e Tipografia Grande)
st.set_page_config(page_title="CompraCalma", page_icon="🧩", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #F0F4F8; } /* Azul acinzentado calmo */
    .big-button { 
        background-color: #4A90E2; color: white !important; 
        padding: 30px; border-radius: 15px; text-align: center;
        font-size: 24px; font-weight: bold; margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .card-mercado {
        background: white; padding: 20px; border-radius: 10px;
        border-left: 5px solid #4A90E2; margin-bottom: 10px;
    }
    h1, h2 { color: #1A365D; font-family: sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO SIMPLIFICADA ---
if 'passo' not in st.session_state:
    st.session_state.passo = 'inicial'

# --- TELA 1: INICIAL ---
if st.session_state.passo == 'inicial':
    st.title("🧩 CompraCalma")
    st.write("Refaça sua compra com um clique, sem barulho e sem estresse.")
    
    if st.button("📷 ESCANEAR QR DA NOTA (NFCe)", use_container_width=True):
        st.session_state.passo = 'escaneamento'
        st.rerun()

    col1, col2 = st.columns(2)
    with col1:
        st.button("🧾 Histórico", use_container_width=True)
    with col2:
        st.button("🛒 Compra Mensal", use_container_width=True)

# --- TELA 2: ESCANEAMENTO (Simulação de QR) ---
elif st.session_state.passo == 'escaneamento':
    st.subheader("📷 Posicione o QR Code")
    st.info("Aponte a câmera para o código quadrado na parte de baixo da sua nota fiscal.")
    
    # Simulador de leitura bem-sucedida
    if st.button("Simular Leitura Correta (Verde ✅)"):
        with st.spinner("Lendo produtos da NFCe..."):
            time.sleep(2)
            st.session_state.passo = 'produtos'
            st.rerun()
    
    if st.button("Voltar"):
        st.session_state.passo = 'inicial'
        st.rerun()

# --- TELA 3: PRODUTOS DETECTADOS ---
elif st.session_state.passo == 'produtos':
    st.subheader("📋 Itens Detectados")
    st.write("Confirme se está tudo certo:")
    
    itens = ["Arroz 5kg", "Feijão 1kg", "Leite 1L", "Ovos 30un", "Frango 1kg"]
    for item in itens:
        col_a, col_b = st.columns([3, 1])
        col_a.write(f"✅ {item}")
        if col_b.button("❌", key=item):
            st.toast(f"{item} removido")

    st.divider()
    if st.button("🔍 COMPARAR PREÇOS NOS MERCADOS", use_container_width=True):
        st.session_state.passo = 'comparacao'
        st.rerun()

# --- TELA 4: COMPARAÇÃO DE MERCADOS ---
elif st.session_state.passo == 'comparacao':
    st.subheader("🛒 Melhor Opção para Rio das Ostras")
    
    # Mercado A (Vencedor)
    st.markdown("""
    <div class="card-mercado">
        <h3 style='margin:0;'>⭐ Atacadão (Mais Barato)</h3>
        <p>Total: <b>R$ 175,00</b> | Entrega: R$ 8,00<br>
        Previsão: <b>1h 20min</b></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("COMPRAR NO ATACADÃO"):
        st.session_state.passo = 'confirmacao'
        st.rerun()

    # Mercado B
    st.markdown("""
    <div class="card-mercado" style='border-left-color: #CCC;'>
        <h3 style='margin:0;'>Assaí</h3>
        <p>Total: R$ 182,00 | Entrega: R$ 12,00<br>
        Previsão: 2h</p>
    </div>
    """, unsafe_allow_html=True)

# --- TELA 5: CONFIRMAÇÃO ---
elif st.session_state.passo == 'confirmacao':
    st.balloons()
    st.success("✅ Pedido Confirmado!")
    st.markdown(f"""
    **Resumo do Pedido:**
    - Mercado: Atacadão
    - Total: R$ 183,00 (Produtos + Frete Único)
    - Previsão de chegada: **{ (datetime.datetime.now() + datetime.timedelta(minutes=80)).strftime('%H:%M') }**
    """)
    
    st.info("📦 O mercado já está separando seus produtos. Você receberá uma notificação suave quando o entregador sair.")
    
    if st.button("Início"):
        st.session_state.passo = 'inicial'
        st.rerun()
