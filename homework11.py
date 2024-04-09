def test_function():
    def inner_function():
        string_ = "Я в области видимости функции test_function"
        print(string_)

    inner_function()

# inner_function() - среда не видит эту ф-цию вне test_function()
# чтобы распечатать string_, надо вызвать ф-цию test_function()
