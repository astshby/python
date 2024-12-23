touhous=['Alice','Reimui','Marisa','Cirno','Yuyuko','Remilia','Flandre']
aa=['Alice','Reimui','Marisa']
for touhou in touhous:
    if touhou.lower() == 'alice' or touhou.lower() == 'marisa':
        print(touhou)
    elif touhou in aa:
        print('aaa')
    else:
        print('ok')

