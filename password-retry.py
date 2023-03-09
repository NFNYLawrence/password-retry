correct_password = 'a123456'
X = 3
while X > 0:
    X = X - 1
    password = input('請輸入密碼: ')
    if password == correct_password:
        print('登入成功!')
        break
    else:
        print('密碼錯誤!')
        if X > 0:
            print('還有', X, '次機會')
        else:
            print('最多輸入3次密碼, 你的帳號已被鎖定')