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

with requests.get(url) as response:  # το αντικείμενο response
    #for key in response.headers:
    print(f"Server:{response.headers.get('Server')}")
    cookies = response.cookies
    if cookies:
        print("\nΗ σελίδα χρησιμοποιεί cookies:")
        for cookie in cookies:
            print(f"- Όνομα: {cookie.name}")
            print(f"  Τιμή: {cookie.value}")
            print(f"  Λήξη: {cookie.expires if cookie.expires else 'Δεν καθορίζεται'}")
    else:
        print("\nΗ σελίδα δεν χρησιμοποιεί cookies.")
    # more(html)
