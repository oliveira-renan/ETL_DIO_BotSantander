# 🤖 Geração de Mensagens Personalizadas para Clientes com IA (Gemini API)

Projeto desenvolvido em Python para automatizar a criação de mensagens personalizadas de marketing bancário sobre investimentos, utilizando a API do Google Gemini e técnicas de ETL / engenharia de prompts.

---

## 📌 Visão Geral do Projeto

O objetivo deste projeto é integrar a API do **Google Gemini** a uma base de dados de clientes no formato CSV para gerar comunicações customizadas e direcionadas de forma automatizada, respeitando limites de taxa (rate limits) e garantindo resiliência na execução.

### 🔄 Fluxo de Funcionamento (ETL + IA)
1. **Autenticação Segura**: Leitura da chave de API (`GOOGLE_API_KEY`) utilizando o repositório de segredos do Google Colab (`userdata`).
2. **Extração de Dados**: Leitura da base de clientes a partir do arquivo `UserID.csv` com Pandas.
3. **Engenharia de Prompts & IA**: Utilização do modelo `gemini-pro-latest` configurado para atuar como um **especialista em marketing bancário**, gerando mensagens personalizadas de até 100 caracteres sobre a importância dos investimentos.
4. **Tratamento de Exceções & Rate Limiting**:
   - Controle de requisições com intervalos de pausa de 4 segundos entre clientes (respeitando o limite de RPM da API).
   - Tratamento do erro de cota `429` com *pausa inteligente* de 30 segundos em caso de limite atingido.
5. **Carga de Dados**: Exportação da base atualizada com as mensagens geradas para o arquivo `UserID_com_MensagemAI.csv`.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **Python 3.x**
- **Google Generative AI SDK** (`google-generativeai`)
- **Pandas** (manipulação de DataFrames e arquivos CSV)
- **Google Colab Userdata** (gestão segura de credenciais/API Key)

---

## 🚀 Como Executar o Projeto

1. Clone este repositório para o seu ambiente ou abra diretamente no **Google Colab**.
2. Adicione sua chave de API do Gemini nos **Secrets** (ícone de chave no menu lateral do Colab) com o nome:
   ```text
   GOOGLE_API_KEY
