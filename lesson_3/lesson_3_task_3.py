from lesson_6.Address_1 import Address
from lesson_4.mailing_1 import Mailing

to_address = Address("234512", "Волгоград", "Хиросима", "12", "33")
from_address = Address("237812", "Пермь", "Ленина", "15", "1")

mailing = Mailing(to_address=to_address,
                  from_address=from_address,
                  cost=250000,
                  track="Track123")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей")
