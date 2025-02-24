import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("Give url:\t")  # προσδιορισμός του url
if not url.startswith("https://"):
    url = 'https://' + url
print(url)

<<<<<<< HEAD
# with requests.get(url) as response:  # το αντικείμενο response
#     html = response.text
#     print(html)
    # more(html)
=======
with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    #more(html)
>>>>>>> get
