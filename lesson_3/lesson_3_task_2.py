from lesson_4.smartphone import Smartphone

smartphone1 = Smartphone("Smart", "10", "7-988-123-43-23")
smartphone2 = Smartphone("Smart", "13", "7-988-543-13-53")
smartphone3 = Smartphone("Smart", "7", "7-945-431-53-34")
smartphone4 = Smartphone("Smart", "16", "7-978-563-46-14")
smartphone5 = Smartphone("Smart", "5", "7-933-645-23-76")

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]

for phone in catalog:
    print(phone.список())
