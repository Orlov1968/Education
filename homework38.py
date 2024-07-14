import inspect


def introspection_info(obj):
    type_object = type(obj).__name__
    print(f"Тип объекта: {type_object}")
    print("-----------------------------------------------------")
    method_and_attribute = dir(obj)
    print(f"Методы и атрибуты объекта: {method_and_attribute}")
    print("-----------------------------------------------------")
    module_of_type = type(obj).__module__
    print(f"Модуль типа объекта = {module_of_type}")
    print("-----------------------------------------------------")
    methods_of_object = inspect.getmembers(obj, lambda attr: not (inspect.ismethod(attr)))
    print(f"Методы объекта: {methods_of_object}")


introspection_info([1, 2, 3])
