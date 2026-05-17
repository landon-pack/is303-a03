''' Landon Pack IS 303 - A03 

Contact Cleaner This program will read a list of contact information, clean the data stripping whitespace,
formatting emails and phone numbers and searching for duplicates 

 
Inputs: - A list of contact information (name, email, phone number)
Processes: 
- Strip whitespace from all fields 
- Format email addresses to be all lowercase 
- Format phone numbers to a standard format (e.g., (123) 456-7890) 
- Search for duplicate entries and remove them 
- Will use the accumulator pattern to log the amount of valid emails and phone numbers 
- Will use the filter pattern to filter out duplicate contacts. 

Outputs: Output a report summarizing the data cleaned and outputting it 

'''

contacts = []

# Inputs
user_input = ""
print("Welcome to the contact cleaner program! Please add your contacts:")

while user_input != "no":
    name = input("What is the contact's name?: ")
    email = input("What is the contact's email?: ")
    phone = input("What is the contact's phone number?: ")

    contacts.append({"name": name, "email": email, "phone": phone})

    user_input = input("Would you like to add another contact? (yes or no): ").lower()

    while user_input != "yes" and user_input != "no":
        print("Please enter yes or no.")
        user_input = input("Would you like to add another contact? (yes or no): ").lower()


# Processing
cleaned_contacts = []

for contact in contacts:

    digits_only = ""
    for char in contact['phone']:
        if char.isdigit():
            digits_only += char

    formatted_phone = f"({digits_only[0:3]})-{digits_only[3:6]}-{digits_only[6:10]}"

    cleaned = {
        "name": contact["name"].strip().title(),
        "email": contact["email"].strip().lower(),
        "phone": formatted_phone
    }

    cleaned_contacts.append(cleaned)


# Email validation (accumulator pattern)
valid_emails = 0
invalid_emails = 0

for contact in cleaned_contacts:
    email = contact["email"]

    if "@" in email and "." in email.split("@")[1]:
        valid_emails += 1
        contact["valid_email"] = True
    else:
        invalid_emails += 1
        contact["valid_email"] = False


# Phone validation (accumulator pattern)
valid_numbers = 0
invalid_numbers = 0

for contact in cleaned_contacts:
    number = contact["phone"]

    digits_only = ""
    for char in number:
        if char.isdigit():
            digits_only += char

    if len(digits_only) == 10:
        valid_numbers += 1
        contact["valid_number"] = True
    else:
        invalid_numbers += 1
        contact["valid_number"] = False


# Duplicate filter
no_duplicates = []
duplicates = []

seen_names = []
seen_emails = []

for contact in cleaned_contacts:

    name = contact["name"]
    email = contact["email"]

    if name not in seen_names and email not in seen_emails:
        seen_names.append(name)
        seen_emails.append(email)
        no_duplicates.append(contact)
    else:
        duplicates.append(contact)

cleaned_contacts = no_duplicates


# Outputs
print("\n--- Contact Cleaner Report ---")
print(f"Original contacts: {len(contacts)}")
print(f"Duplicate contacts found: {len(duplicates)}")
print(f"Valid emails: {valid_emails}")
print(f"Invalid emails: {invalid_emails}")
print(f"Valid phone numbers: {valid_numbers}")
print(f"Invalid phone numbers: {invalid_numbers}")
print(f"Final clean contacts: {len(cleaned_contacts)}")