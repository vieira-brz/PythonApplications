import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

email = outlook.CreateItem(0)

my_name = 'Código Python'

email.To = "someone@gmail.com; someone2@gmail.com"
email.Subject = "E-mail automático do Python"
email.HTMLBody = f"""
    <p>Olá, este é o {my_name}!</p>
    <p>Seja bem vindo ao seu novo ambiente de desenvolvimento.</p>
    <p>Abs,</p>
    <p>{my_name}</p>
"""

anexo = "C://Users/user/Downloads/arquivo.xslx"
email.Attachments.Add(anexo)

email.Send()