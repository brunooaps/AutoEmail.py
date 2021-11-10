import smtplib, ssl
import os
from datetime import date
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication

#Conexão com o servidor do gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587 #A porta pode variar para 465

#Preencha com seu email
gmail = '@example.com'
password = 'password'

#Array com os emails
receiver = ['@example.com', '@example,com', '@example.com']

#Pegar a data, não é necessário, apenas uma feature que eu precisava
time = date.today()

#Iniciar o loop para enviar para todos os emails.
i = 0
while i < 4: #Para saber o numero a colocar em i < X - basta pegar todos os emails que precisa enviar + 1, por exemplo, vou enviar para 3 emails, colocaria 4
  
    #Envio da mensagem
    message = MIMEMultipart('mixed')
    message['From'] = 'Example <{sender}>'.format(sender = gmail) #Este campo deve ser preenchido com o nome do remetente
    message['To'] = receiver[i] #campo do destinatário, que está com o array [i], pois mudará conforme vai enviando
    message['Subject'] = 'Example text' #Este é o campo do cabeçalho do seu email.

    #Para quem está enviando
    receiver[i]

    '''
    Este campo não é necessário, serviu para mim apenas para listar todos os anexos que eu precisava.
    for _, _, file in os.walk('C:\Example'):
        print('enviado ' + f'{file[i]}' + 'para email: ')
    '''

    #Mensagem a ser enviada no corpo do email, funciona como um HTML, assim fica mais facil de digitar.
    msg_content = '<p>Example Message</p>\n'
    body = MIMEText(msg_content, 'html')
    message.attach(body)

    #Adicionar o anexo a mensagem, deve ser informado o caminho até o arquivo de anexo desejado.
    attachmentPath = 'C:\\example.pdf'
    try:
        with open(attachmentPath, 'rb') as attachment:
            p = MIMEApplication(attachment.read(),_subtype='pdf')
            p.add_header('Content-Disposition', 'attachment', filename= 'example_name.pdf') #No campo "filename=" pode ser informado o nome desejado para dar ao arquivo na hora do envio
            message.attach(p)
    except Exception as e: #Caso o programa não consiga achar o arquivo, avisará que não foi possivel, e encerrará o programa, senão seria enviado um email sem o anexo.
        print(str(e))
        exit()

    #Converter a mensagem em uma string
    msg_full = message.as_string()

    #Envio do email
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail, password)
        server.sendmail(gmail, receiver[i], msg_full) #neste campo, é informado o email do remetente, o email do destinatário, e a mensagem, que já foi informado nas variaveis acima.
        server.quit() #Após finalizar os envios, o programa será encerrado.
        
    print(f'{receiver[i]}') #Quando o programa fizer um envio, avisará cada vez que enviar um dos emails.

    i += 1 #Código para continuar o loop até a finalização.


























