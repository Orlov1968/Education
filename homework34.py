from multiprocessing import Process, Event

list_1 = [("product1", "receipt", 100),
          ("product2", "receipt", 150),
          ("product1", "shipment", 30),
          ("product3", "receipt", 200),
          ("product2", "shipment", 50),
          ("product1", "receipt", 80)]
dict_1 = {}


def proces_request():
    for i in list_1:
        if i[1] == "receipt":
            key = i[0]
            value = i[2]
            if key in dict_1:
                dict_1[key] += value
            else:
                dict_1[key] = value
   # event.set()
    return dict_1


def shipment():
    dict_2 = {}
    dict_2 = proces_request()
   # event.wait()
    for i in list_1:
        if i[1] == "shipment":
            product = i[0]
            quantity = i[2]
            if product in dict_2 and dict_2[product] >= quantity:
                dict_2[product] -= quantity
            else:
                print("Такого продукта нет на складе")
    print(dict_2)


shipment()

# if __name__ == "__main__":
#     event = Event()
#     proces_request_proc = Process(proces_request)
#     shipment_proc = Process(shipment)
#     proces_request_proc.start()
#     shipment_proc.start()
#     proces_request_proc.join()
#     shipment_proc.join()

