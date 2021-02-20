import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder


try:
    inp = input("Write mobile number here: ")
    number = "+91" + inp

    ch_number = phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(ch_number, "en"))

    service_nmber =phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_nmber, "en"))
except:
    print("You'll need to install 'pip install phonenumbers'.")
