from multiprocessing import Process, Lock, Manager


class WarehouseManager:
    def __init__(self, data, lock):
        self.lock = lock
        self.data = data

    def process_request(self, list_1: tuple):
        product, action, quantity = list_1
        with self.lock:
            if action == "receipt":
                if product in self.data:
                    self.data[product] += quantity
                else:
                    self.data[product] = quantity
            elif action == "shipment":
                if product in self.data and self.data[product] >= quantity:
                    self.data[product] -= quantity

    def run(self, list_new):
        processes = []
        for list_1 in list_new:
            proc = Process(target=self.process_request, args=(list_1,))
            processes.append(proc)
            proc.start()
        for proc in processes:
            proc.join()


if __name__ == "__main__":
    list_new = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    with Manager() as manager:
        data = manager.dict()
        lock = Lock()
        warehouse_manager = WarehouseManager(data, lock)
        warehouse_manager.run(list_new)

        print(data)
