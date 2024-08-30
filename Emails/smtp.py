import smtplib
import email.message

def enviar_email():
    # Corpo do e-mail em formato HTML
    corpo_email = """
        <p>Hello World!</p>
    """

    # Criação do objeto de mensagem
    msg = email.message.Message()
    msg['Subject'] = "Assunto"          # Assunto do e-mail
    msg['From'] = "my_email@gmail.com"  # Remetente do e-mail
    msg['To'] = "my_email@gmail.com"    # Destinatário do e-mail

    password = "my_email_2_auth_password"  # Senha de autenticação do e-mail

    # Define o tipo de conteúdo como HTML
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # Conecta ao servidor SMTP do Gmail
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()                        # Inicia a conexão segura
    s.login(msg['From'], password)      # Autentica com as credenciais fornecidas
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))  

    print('Email enviado') 

# Chama a função para enviar o e-mail
enviar_email()
