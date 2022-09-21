from twilio.rest import Client

def twilio_sms(text = ''):
    try:
        account_sid = 'YOUR SID'
        auth_token = 'YOUR TOKEN'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        body = text,
        from_ = input('Номер Twillo: '),
        to = input('Номер получателя: ')
        )
        return 'Сообщение успешно отправлено!'
    except Exception as ex:
        return 'Что-то пошло не так...', ex
        
def main():
    text = input('Ведите свое сообщение: ')
    print(twilio_sms(text=text))
   
    

if __name__ == '__main__':
    main()
