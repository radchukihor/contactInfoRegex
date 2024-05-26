import re

# Define regular expressions for phone numbers, emails, and websites
phone_regex = r'\(?\d{3}\)?[- ]\d{3}[- ]\d{4}'
email_regex = r'([\w\.]+@\w+\.(com|net|org))'
website_regex = r'(^|\s)(\w+\.(com|net|org))'

# Open the example email file and read its contents
with open('example_email.txt', 'r') as file:
    content = file.read()

# Find all matches for phone numbers, emails, and websites in the content
phone_matches = re.findall(phone_regex, content)
email_matches = re.findall(email_regex, content, re.IGNORECASE)
website_matches = re.findall(website_regex, content, re.IGNORECASE)

# Initialize empty lists to store unique phone numbers, emails, and websites
phone_list = []

# Iterate over the matched phone numbers
for phone in phone_matches:
    line = phone + '\n'  # Add a newline character to each phone number

    if line not in phone_list:
        phone_list.append(line)  # Append to the list if it's not already included

# Write the unique phone numbers to a file
with open('phone_numbers.txt', 'w') as file:
    file.writelines(phone_list)

# Initialize an empty list to store unique email addresses
email_list = []

# Iterate over the matched email addresses
for email in email_matches:
    line = email[0] + '\n'  # Add a newline character to each email

    if line not in email_list:
        email_list.append(line)  # Append to the list if it's not already included

# Write the unique email addresses to a file
with open('emails.txt', 'w') as file:
    file.writelines(email_list)

# Initialize an empty list to store unique websites
website_list = []

# Iterate over the matched websites
for website in website_matches:
    line = website[1] + '\n'  # Add a newline character to each website

    if line not in website_list:
        website_list.append(line)  # Append to the list if it's not already included

# Write the unique websites to a file
with open('websites.txt', 'w') as file:
    file.writelines(website_list)
