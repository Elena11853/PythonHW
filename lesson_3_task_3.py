from address import Address
from mailing import Mailing 

to_address = Address('160001', 'Вологда', 'Мира', '24', '2' )
from_address = Address('162200', 'Харовск', 'Ленградская', '39', '12')
mailing = Mailing(to_address, from_address, 100, "111111111")
print(mailing)