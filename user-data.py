
import json
import random

def import_json(filename):
    with open(filename, "r") as file:
        file_data = json.load(file)

    return file_data

male_names = "./entities/male_names.json"
dob_file = "./entities/user_dob.json"
city_file = "./entities/city-names.json"
email_file = "./entities/emails.json"
phone_file = "./entities/phone_numbers.json"
aadhar_file = "./entities/aadhar_number.json"
pan_file = "./entities/pan_card.json"
voter_file = "./entities/voter_id.json"
passport_file = "./entities/passport_number.json"
driving_file = "./entities/driving_licence_numbers.json"
bank_details_file = "./entities/bank_details.json"
ip_file = "./entities/ip_addresses.json"

names = import_json(male_names)
dobs = import_json(dob_file)
cities = import_json(city_file)
emails = import_json(email_file)
phones = import_json(phone_file)
aadhars = import_json(aadhar_file)
pans = import_json(pan_file)
voters = import_json(voter_file)
passports= import_json(passport_file)
licenses = import_json(driving_file)
bank_details = import_json(bank_details_file)
ips = import_json(ip_file)


user_data = []
for i in range(1000):
    name = names[i]["name"] if random.choice([True,False]) else ""
    gender = names[i]["gender"] if random.choice([True,False]) else ""
    dob = dobs[i]["dob"] if random.choice([True,False]) else ""
    nationality = names[i]["race"] if random.choice([True,False]) else ""
    city = cities[i]["accentcity"] if random.choice([True,False]) else ""
    email = emails[i]["email"] if random.choice([True,False]) else ""
    phone_number = phones[i]["phone"] if random.choice([True,False]) else ""
    aadhar_number = aadhars[i]["aadhar"] if random.choice([True,False]) else ""
    pan_number = pans[i]["pan_num"] if random.choice([True,False]) else ""
    voter_id_number = voters[i]["voter_id"] if random.choice([True,False]) else ""
    passport_number = passports[i]["passport_num"] if random.choice([True,False]) else ""
    license_number = licenses[i]["license_num"] if random.choice([True,False]) else ""
    bank_account = bank_details[i]["account_number"] if random.choice([True,False]) else ""
    bank_ifsc_code = bank_details[i]["ifsc_code"] if random.choice([True,False]) else ""
    atm_card_number = bank_details[i]["card_number"] if random.choice([True,False]) else ""
    cvv_number = bank_details[i]["cvv"] if random.choice([True,False]) else ""
    ip = ips[i]["ip_address"] if random.choice([True,False]) else ""

    data = {
        "name" : name,
        "gender": gender,
        "dob": dob,
        "nationality": nationality,
        "city" : city,
        "email" : email,
        "phone_number" : phone_number,
        "aadhar_number" : aadhar_number,
        "pan_number" : pan_number,
        "voter_id_number" : voter_id_number,
        "passport_number" : passport_number,
        "license_number" : license_number,
        "bank_account": bank_account,
        "bank_ifsc_code": bank_ifsc_code,
        "atm_card_number": atm_card_number,
        "cvv_number": cvv_number,
        "ip_address" : ip,
    }

    user_data.append(data)

with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent = 4)

print("User data generated successfully!")  