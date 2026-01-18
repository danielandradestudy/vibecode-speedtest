import streamlit as st
import speedtest

# Configuração da página (título na aba do navegador)
st.set_page_config(page_title="Vibecode Speedtest", page_icon="🚀")

st.title("🚀 Teste de Velocidade - Vibecode")
st.markdown("Este projeto mede a velocidade da internet do **servidor** onde está rodando.")

# O botão que inicia tudo
if st.button('Iniciar Teste'):
    
    # Cria uma barra de progresso ou spinner para o usuário não ver tela branca
    with st.spinner('A conectar aos servidores... (Isto pode demorar uns segundos)'):
        try:
            # 1. Configurar o Speedtest
            st_obj = speedtest.Speedtest(secure=True)
            
            # 2. Escolher o melhor servidor
            st.write("🔎 A procurar o melhor servidor...")
            st_obj.get_best_server()
            
            # 3. Medir Download
            st.write("⬇️ A testar download...")
            download_speed = st_obj.download() / 1_000_000  # Converter para Mbps
            
            # 4. Medir Upload
            st.write("⬆️ A testar upload...")
            upload_speed = st_obj.upload() / 1_000_000  # Converter para Mbps
            
            ping = st_obj.results.ping

            # 5. Exibir Resultados Finais
            st.success("Teste concluído!")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Download", f"{download_speed:.2f} Mbps")
            col2.metric("Upload", f"{upload_speed:.2f} Mbps")
            col3.metric("Ping", f"{ping:.0f} ms")

        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
            st.warning("Dica: Se estiver rodando localmente, verifique sua conexão.")