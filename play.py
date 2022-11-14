a = '''123,Robinson Ave, Newburgh, NY 12550, United States
Washington Ave, Albany, NY 12210, United States
Old Collamer Rd S, East Syracuse, NY 13057, United States
East Ave, Rochester, NY 14610, United States
Pine Ridge Rd, Buffalo, NY 14225, United States'''

address_list = a.split('\n')



def get_pin(str):
    pin = ''
    for i in str:
        if i.isdigit():
            pin = pin+i
    return pin


pin_list = []
for i in address_list:
    pin_list.append(get_pin(i))

D = {}
i = 0
while i < len(address_list):
    D.update({pin_list[i]: address_list[i]})
    i = i+1
print(D)