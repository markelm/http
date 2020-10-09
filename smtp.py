import smtplib
import smtpd #bib do servidor
import asyncore #multiplas conexoes

#tabela com 
domainTable = {'rivendell.com': ['127.0.0.2', 1026]}
destination = None

#simula request para o DNS e caso nao encontrado return a string 'Not Found'
def DNSrequest(domain):
    return domaninTable.get('rivendell', 'Not Found')

#classe herdada para sobrescrita do metido de processamento de mensagens
class CustomsSMTPServer(smtpd.SMTPServer):
    
    #metodo de processamento de mensagens
    def process_message(self, peer, mailfrom, rcpttos, data, mail_options=None, rcpt_options=None):
        print("Mensagem enviada pelo IP {}".format(peer))
        print("Mensagem enviada pelo e-mail {}".format(mailfrom))
        print("Mensagem destinada ao e-mail {}".format(rcpttos))
        print("Tamanho da mensagem: {}".format(len(data)))
        print(f'{data}')
        destination = rcpttos[0]
        destination = destination[destination.find('@') + 1:]
        print(destination)
        print(domainTable[destination])

        if destination != None:
            print('DESTINATION ACQUIRED!!!')
            server_to = smtplib.SMTP(domainTable[destination][0], domainTable[destination][1])
            server_to.sendmail(mailfrom, rcpttos, data)

server = CustomsSMTPServer(("127.0.0.1", 1025), None)

print("Servidor em execucao")
asyncore.loop()#entra em loop para aceitar multiplas conexoes(se necessario)


