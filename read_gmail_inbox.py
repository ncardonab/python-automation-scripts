import imaplib
import email

import yaml

with open("credentials.yml") as f:
    content = f.read()

credentials = yaml.load(content, Loader=yaml.FullLoader)

user, password = credentials["user"], credentials["password"]

imap_url = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(imap_url)

mail.login(user, password)

mail.select('Inbox')

key = 'FROM'
value = '****'
_, data = mail.search(None, key, value)

mail_id_list = data[0].split()

messages = []

for number in mail_id_list:
    typ, data = mail.fetch(number, '(RFC822)')
    messages.append(data)

for message in messages[::-1]:
    for response_part in message:
        print(response_part)
        my_message = email.message_from_bytes((response_part[1]))
        print("_____________________________")
        print("subj:", my_message['subject'])
        print("from:", my_message['from'])
        print("body:")
        for part in my_message.walk():
            if part.get_content_type() == 'text/plain':
                print(part.get_payload())

# SERVER = "pop.gmail.com"huimvwajjfjxfqrr
