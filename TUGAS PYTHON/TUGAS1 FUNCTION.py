def apakah_prima(a):
    if a <= 1:
        print('Bukan bilangan prima')
        return False
    if a == 2: 
        return True
    if a % 2 == 0 and a > 2:
        return False
    return apakah_prima (a,2+1)

bilangan = int(input('Masukkan bilangan yang akan dicek: '))

if apakah_prima(bilangan):
    print('Bilangan yang anda masukkan adalah bilangan prima')
else: 
    print('Bilangan yang anda masukkan bukan bilangan prima')