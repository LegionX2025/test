import re

def extract_data(context):
    usernames = re.findall(r"@[\w]+", context)
    emails = re.findall(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", context, re.I)
    phones = re.findall(r'\b\d{10}\b', context)
    wallet_addresses = re.findall(r'1[a-zA-HJ-NP-Z0-9]{25,39}', context)  # Bitcoin as example
    
    return {
        "usernames": usernames,
        "emails": emails,
        "phones": phones,
        "wallet_addresses": wallet_addresses
    }
