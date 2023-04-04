from whois import whois

def is_registered(domain):

    try:

        website = whois(domain)

    except Exception:

        return False

    else:

        return bool(website.domain)

domain = input("Enter in domain name: ")

if is_registered(domain):

    info = whois(domain)

    print(f"Domain registrar: {info.registrar}")

    print(f"WhOIS server: {info.whois_server}")

    print(f"Domain creation date: {info.creation_date}")

    print(f"Domain expiration date: {info.expiration_date}")

    print("Other info: ")

    print(info)
