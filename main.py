
field = [[-4,-4,-4],[-4,-4,-4],[-4,-4,-4]]
step = 0

run = True

def print_field(field):
    print('\t1\t2\t3', end='')
    ln_num = 1
    for line in field:
        print(f'\n{ln_num}\t', end='')
        for column in line:
            if column == 1:
                print('X', end='\t')
            elif column == 0:
                print('O', end= '\t')
            else:
                print('.', end='\t')
        ln_num += 1

def x(field):
    print()
    empty = True
    while empty:
        x_place = input('Координаты x:')
        x_place = x_place.split()
        x_place = list(map(int,x_place))
        empty = check_place(field,x_place)
    field[(x_place[0]-1)][(x_place[1]-1)] = 1

def o(field):
    print()
    empty = True
    while empty:
        o_place = input('Координаты o:')
        o_place = o_place.split()
        o_place = list(map(int, o_place))
        x_place = list(map(int, o_place))
        empty = check_place(field, x_place)
    field[(o_place[0] - 1)][(o_place[1] - 1)] = 0

def check_place(field,space):
    if field[(space[0] - 1)][(space[1] - 1)] == 1:
        print('На этом месте уже стоит Х, введите еще раз')
        return True
    elif field[(space[0] - 1)][(space[1] - 1)] == 0:
        print('На этом месте уже стоит O, введите еще раз')
        return True
    else:
        return False

def check_win(field):
    for i in range(0,3):
        if (field[i][0]+field[i][1]+field[i][2]==3) or (field[i][0]+field[i][1]+field[i][2]==0):
            return False
        if (field[0][i]+field[1][i]+field[2][i]==3) or (field[0][i]+field[1][i]+field[2][i]==0):
            return False
    if (field[0][0]+field[1][1]+field[2][2]==3) or (field[0][0]+field[1][1]+field[2][2]==0):
        return False
    if (field[0][2]+field[1][1]+field[2][0]==3) or (field[0][2]+field[1][1]+field[2][0]==0):
        return False
    return True


print('Координаты вводятся через пробел')
while run:
    print_field(field)
    x(field)
    step +=1
    run = check_win(field)
    if (run is False) or step  == 9:
        break
    print_field(field)
    o(field)
    step += 1
    run = check_win(field)
print('Игра окончена')