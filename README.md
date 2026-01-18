# 🚀 Vibecode Speedtest

> Uma ferramenta de teste de velocidade de internet modernizada: do Desktop (Tkinter) para a Web (Streamlit).

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Status](https://img.shields.io/badge/Status-Educational-green.svg)

## 📖 Sobre o Projeto

Este projeto nasceu de um exercício de **refatoração**. Encontrei um script antigo ("internet.py") que escrevi quando comecei a estudar Python. A versão original usava `tkinter` e rodava apenas localmente no desktop.

Como parte da minha transição para a área de **Engenharia de Dados**, decidi modernizar o código com foco em:
- **Experiência do Utilizador (UX):** Migrar de uma interface desktop bloqueante para uma Web App fluida.
- **Arquitetura Web:** Entender na prática a diferença entre execução *Client-side* e *Server-side*.

## 💡 A Grande Lição (Client vs. Server)

Se testares este projeto online (via Streamlit Cloud), vais notar que a velocidade é absurdamente alta (frequentemente acima de **1 Gbps**).

**Porquê?**
Diferente do JavaScript, que roda no navegador do utilizador, o **Python roda no servidor** (backend).
- Quando clicas em "Iniciar Teste", o script mede a velocidade da internet do **Data Center** onde a aplicação está hospedada (ex: AWS/Google Cloud), e não a da tua casa.
- Foi um excelente laboratório para entender conceitos de infraestrutura e nuvem.

## 🛠️ Tecnologias Utilizadas

- **Python 3**: Linguagem principal.
- **Streamlit**: Para criação da interface Web e deploy.
- **speedtest-cli**: Biblioteca para comunicação com os servidores de teste.

## 🚀 Como Rodar Localmente

Se quiseres testar a tua própria internet (não a do servidor), precisas de rodar o projeto na tua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/vibecode-speedtest.git](https://github.com/SEU-USUARIO/vibecode-speedtest.git)
   cd vibecode-speedtest
