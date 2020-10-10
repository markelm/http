#cliente SMTP que se comunica sem nenhum protocolo de seguranca

import smtplib #biblioteca para implementar o clinete
import email.utils #provem funcoes utilitarias para formatacao/geracao
from email.mime.text import MIMEText#classe de mensagens

#criando mensagem a ser enviada

msg = MIMEText("Bilbo esta com saudades. Pediu para vc trazer o anel.")
msg["To"] = email.utils.formataddr(("Aragorn", "aragorn@rivendell.com"))
msg["From"] = email.utils.formataddr(("Frodo", "frodo@gondor.com"))
msg["Subject"] = "Quando voce vem pra ca?"

#Agora criamos o servidor SMTP que roda do lado do cliente para enviar
server = smtplib.SMTP("127.0.0.1", 1025)
server.set_debuglevel(True)#debug para ver a interacao de msgs

#enviamos a msg
server.sendmail("frodo@gondor.com", ["aragorn@rivendell.com"], msg.as_string())

#encerra
server.quit()
