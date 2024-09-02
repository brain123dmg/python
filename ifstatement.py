price = 1000000
Good_crd = True
bad_crd = True

if Good_crd:
    down_payment = 0.1 * price
    print(f'youll have to pay ${down_payment}')
elif bad_crd:
    down_payment = 0.2 * price
    print(f'youll have to pay ${down_payment}')
else:
    print('one must be true')