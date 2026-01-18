import streamlit as st
import speedtest

st.set_page_config(page_title="Speedtest Vibecode", page_icon="🚀")

st.title("🚀 Teste de Velocidade")
st.write("Um projeto simples para testar sua conexão.")

# Botão para iniciar
if st.button('Iniciar Teste'):
    with st.spinner('Conectando aos servidores...'):
        try:
            # Inicializa o objeto
            st_obj = speedtest.Speedtest(secure=True)
            
            # Pega o melhor servidor
            st_obj.get_best_server()
            
            # Mede download e upload
            with st.spinner('Medindo Download...'):
                download = st_obj.download() / 1_000_000
            
            with st.spinner('Medindo Upload...'):
                upload = st_obj.upload() / 1_000_000
                
            ping = st_obj.results.ping

            # Exibe os resultados em colunas bonitas (métricas nativas do Streamlit)
            col1, col2, col3 = st.columns(3)
            col1.metric("Download", f"{download:.2f} Mbps")
            col2.metric("Upload", f"{upload:.2f} Mbps")
            col3.metric("Ping", f"{ping:.0f} ms")
            
            st.success("Teste finalizado com sucesso!")
            
        except Exception as e:
            st.error(f"Ocorreu um erro ao testar: {e}")
