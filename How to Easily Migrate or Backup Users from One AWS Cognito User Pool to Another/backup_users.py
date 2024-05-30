import json
import pandas as pd
import random
import string


with open('users.json', 'r') as f:
        data = json.load(f)


# desired headers standard template
keys=desired_headers =  [
        "profile",
        "address",
        "birthdate",
        "gender",
        "preferred_username",
        "updated_at",
        "website",
        "picture",
        "phone_number",
        "phone_number_verified",
        "zoneinfo",
        "locale",
        "email",
        "email_verified",
        "given_name",
        "family_name",
        "middle_name",
        "name",
        "nickname",
        "cognito:mfa_enabled",
        "cognito:username"
    ]


# Required by new userpool
required_attributes =[
    "sub",
    "email",
    "name"
]

# To generate random strings for required attributes if we have no value from source userpool

def generate_rndm():
    digit_char = random.choices(string.ascii_uppercase, k=9) + random.choices(string.digits, k=2)
    random.shuffle(digit_char)
    return "" + ''.join(digit_char)

# IMPORTANT NOTE :
# At least one of the auto-verified attributes must be true for each user. 
# In simple words, one of the fields must be true from email_verified or phone_number_verified . 

must_be_true = 'email_verified'
must_be_false = 'phone_number_verified'



prepare = {}



# create a dict with desired headers and empty lists
for key in keys:
    prepare[key] = []
prepare

# save the data for headers and values found in  users.json
for d in data:
    prepare['cognito:username'].append(d[0])
    for item in d[1]:
        if item['Name'] in desired_headers:
            if item['Name'] == 'email_verified':
                prepare[item['Name']].append(True)
            else:
                prepare[item['Name']].append(item['Value'])

# save the data for headers and values NOT found in  users.json
for key in prepare:
    if (prepare[key] == [] and key in desired_headers) or (len(prepare[key]) < len(prepare['cognito:username']) and key in desired_headers):
        for i in range(len(prepare[key]),len(prepare['cognito:username'])):
            if key == must_be_false or key == 'cognito:mfa_enabled':
                prepare[key].append(False)
            elif key == must_be_true:
                prepare[key] = [True for j in range(len(prepare['cognito:username']))]
            elif key in required_attributes:
                prepare[key].append(generate_rndm())
            else:
                prepare[key].append('')
            

 # Convert dictionary to DataFrame
df = pd.DataFrame.from_dict(prepare, orient='index').transpose()

# Save DataFrame to CSV
df.to_csv('users.csv', index=False)

print("CSV file 'users.csv' has been created.")
print(df)               
    
                    
        
                    
