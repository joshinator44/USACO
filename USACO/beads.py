"""
ID: joshua.31
PROG: beads
LANG: PYTHON3
"""

beads = open('beads.in', 'r').read().split('\n')[1]
count = len(beads)

max_num = 0
for i in range(count):
    combined = beads[count - i:] + beads + beads[0:count - i]
    left_count = 0
    left_letter = None
    l_num = [x for x in range(count)]
    l_num.reverse()
    right_count = 0
    right_letter = None
    r_c = 0
    r_num = [x for x in range(count, count * 2)]
    for i2 in l_num:
        if combined[i2] == 'w':
            left_count += 1
            continue
        elif combined[i2] == 'r':
            if left_letter is None:
                left_letter = 'r'
                left_count += 1
                continue
            elif left_letter != 'r':
                break
            else:
                left_count += 1
                continue
        elif combined[i2] == 'b':
            if left_letter is None:
                left_letter = 'b'
                left_count += 1
                continue
            elif left_letter != 'b':
                break
            else:
                left_count += 1
                continue

    for i2 in r_num:
        if r_c + left_count == count:
            break
        r_c += 1
        if combined[i2] == 'w':
            right_count += 1
            continue
        elif combined[i2] == 'r':
            if right_letter is None:
                right_letter = 'r'
                right_count += 1
                continue
            elif right_letter != 'r':
                break
            else:
                right_count += 1
                continue
        elif combined[i2] == 'b':
            if right_letter is None:
                right_letter = 'b'
                right_count += 1
                continue
            elif right_letter != 'b':
                break
            else:
                right_count += 1
                continue

    if max_num < left_count + right_count:
        max_num = left_count + right_count

out = open('beads.out', 'w')
out.write(f'{max_num}\n')
out.close()