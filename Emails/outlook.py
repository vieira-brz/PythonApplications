import win32com.client as win32

# Inicializa a aplicação do Outlook
outlook = win32.Dispatch('outlook.application')

# Cria um novo e-mail
email = outlook.CreateItem(0)

# Define o nome que será exibido no corpo do e-mail
my_name = 'Código Python'

# Configura o destinatário do e-mail
email.To = "someone@gmail.com; someone2@gmail.com"

# Define o assunto do e-mail
email.Subject = "E-mail automático do Python"

# Cria o corpo do e-mail em formato HTML
email.HTMLBody = f"""
    <p>Olá, este é o {my_name}!</p>
    <p>Seja bem vindo ao seu novo ambiente de desenvolvimento.</p>
    <p>Abs,</p>
    <p>{my_name}</p>
"""

# Adiciona um anexo ao e-mail
anexo = "C://Users/user/Downloads/arquivo.xslx"
email.Attachments.Add(anexo)

# Envia o e-mail
email.Send()