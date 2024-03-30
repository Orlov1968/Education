immutable_var = (8, "string", False, 4)
print(immutable_var)
#immutable_var[0] = 7 print(immutable_var). Выполнить замену объекта, внесённого в кортеж,
# не разрешит среда разработки. В языке программирования python объекты кортежа - неизменяемые
mutable_list = [True, 5, "Accept", 9]
mutable_list[0] = False
mutable_list[1] = 8
mutable_list[2] = "Ария"
mutable_list[3] = 2
print(mutable_list)