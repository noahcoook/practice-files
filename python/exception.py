x = 0

try:
    



    print(x/1)
except NameError:
    print('theres a name error')
except ZeroDivisionError:
    print('zero error')
except Exception as err:
    print(err)
else:
    print('no errors')
finally:
    print('IM GOUNG TO PRINT W OR WOUT ERROER')