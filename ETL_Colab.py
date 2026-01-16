# Importando o SDK do Python para Gemini
import google.generativeai as genai
from google.colab import userdata

# Para obter a chave de API dos segredos do Colab
GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

print("API do Gemini configurada com sucesso!")


# Para inicializar o modelo Gemini
gemini_model = genai.GenerativeModel('gemini-pro-latest')

print("Modelo Gemini 'gemini-pro-latest' inicializado.")

#Para utilizar e visualizar o arquivo utilizado
df = pd.read_csv("UserID.csv")
display(df.head())


# Listando todos os modelos de IA que tenho disponível para utilizar
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


# Garantindo que a autenticação vai funcionar antes de tentar rodar comandos complexos de IA
from google.colab import userdata

try:
    api_key_check = userdata.get('GOOGLE_API_KEY')
    if api_key_check:
        print("GOOGLE_API_KEY está configurada corretamente.")
    else:
        print("GOOGLE_API_KEY foi encontrada, mas está vazia.")
except Exception as e:
    print(f"Erro ao acessar GOOGLE_API_KEY: {e}\nPor favor, certifique-se de que a chave foi adicionada aos segredos do Colab com o nome correto.")



# Gerando o prompt solicitando a mensagem personalizada para o cliente, incluindo alguns retornos caso haja erro
#especificados abaixo

import pandas as pd
import time  

def generate_ai_news(user_data):
  try:
    prompt = (f"Você é um especialista em marketing bancário. Crie uma mensagem "
              f"personalizada para {user_data['Nome']} sobre a importância dos "
              f"investimentos. Use tom profissional, e no máximo 100 caracteres.")
    
    response = gemini_model.generate_content(prompt)
    return response.text.strip()
  except Exception as e:
    # Se o erro for de cota (429), retornamos uma flag para tratar no loop
    return f"ERRO_API: {e}"

if 'df' in locals() and not df.empty:
  df['Mensagem AI'] = ''
  
  for index, user_row in df.iterrows():
    news = generate_ai_news(user_row)
    
    # Tratamento simples para não salvar o erro como mensagem final
    if "ERRO_API" in news and "429" in news:
        print(f"⚠️ Cota atingida no cliente {user_row['Nome']}. Pausando por 30s...")
        time.sleep(30) # Tempo de espera maior se der erro
    else:
        df.loc[index, 'Mensagem AI'] = news
        print(f"Mensagem para {user_row['Nome']}: {news}")
                
        time.sleep(4) #Pausará por 04 segundos entre cada cliente para tentar respeitar o limite de 15 RPM

else:
  print("DataFrame 'df' não encontrado ou está vazio.")


#Salvando o arquivo com inclusão do nome "..._com_MensagemAI", aparecendo mensagem caso seja efetuado com sucesso
df.to_csv('UserID_com_MensagemAI.csv', index=False)
print("DataFrame salvo com sucesso em 'UserID_com_MensagemAI.csv'")
