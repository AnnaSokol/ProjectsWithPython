def create_record(name, telephone, address):
    '''create record'''
    record = {
        'name': name,
        'telephone': telephone,
        'address': address,
    }
    return record

user1 = create_record("Monica", "+498765443", "Musterstrasse 2")
user2 = create_record("Bill", "+4987222443", "Muster Weg 6")

print(user1)
print(user2)
#----------------------------------------------------------------------------
def give_avard(present, *persons):
    """Give present to persons"""
    for person in persons:
        print("Herr "+ person.title()+ " bekommt " + present)

give_avard("TV set", "Mauermann", "Mastermann")
give_avard("das Handy", "Dietrih", "Kolb")
# Herr Mauermann bekommt TV set
# Herr Mastermann bekommt TV set
# Herr Dietrih bekommt das Handy
# Herr Kolb bekommt das Handy
