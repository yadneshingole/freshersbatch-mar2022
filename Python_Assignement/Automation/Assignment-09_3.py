import imaplib
import email
import email.header
import sys
import bs4
import os

userEmail = ''
userEmailAppPass = ''
emailProviderImap = 'imap.gmail.com'
userEmailFolder = '"[Gmail]/All Mail"'
subLinksFileName = 'unsubscribeLinks'
# We only care about this many emails
# Set to 0 if need to process unlimited emails
limit = 100

mail = imaplib.IMAP4_SSL(emailProviderImap)

try:
    rv, data = mail.login(userEmail, userEmailAppPass)
except imaplib.IMAP4.error:
    print("LOGIN FAILED!!! ")
    sys.exit(1)

rv, data = mail.select(userEmailFolder, readonly=True)
if rv == 'OK':
    print('Processing mailbox...')
else:
    print('ERROR: Unable to open mailbox ', rv)
    mail.logout()
    sys.exit(1)

# TODO: add multi filters to search
# for example SENTSINCE
rv, data = mail.search(None, "TEXT unsubscribe")
emailCount = 0

unsubLinks = []
subLinksFile = open(subLinksFileName, 'w')

for num in data[0].split():
    try:
        if limit != 0 and emailCount > limit:
            print('Reached the maximum of emails we want to process')
            break

        print('Processing email id = ', num, '...', sep='')

        rv, data = mail.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            continue

        msg = email.message_from_bytes(data[0][1])
        if msg.is_multipart():
            for payload in msg.get_payload():
                body = payload.get_payload()
        else:
            body = msg.get_payload()

        soup = bs4.BeautifulSoup(body, "html.parser")
        links = soup.find_all('a', text='unsubscribe')
        for link in links:
            if 'href' not in link.attrs:
                continue
            href = link['href']
            if href not in unsubLinks:
                unsubLinks.append(href)
                print('Found new link to unsubscribe from: ', href)
                # Write to csv file on drive, in case of memory overflow
                subLinksFile.write(href + os.linesep)
    except Exception as e:
        print('We encountered an exception but we decided to keep going.')
        print('The exception was: ', e)
        pass

    emailCount += 1

print('Emails processed: ', emailCount)
print('Unsubscribe links found: ', len(unsubLinks))

subLinksFile.close()
mail.close()
mail.logout()
