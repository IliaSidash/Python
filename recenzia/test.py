
for count_analog in range(16, 32):
    count_analog_board = round(count_analog/16)
    print(count_analog / 16, count_analog_board)
    print(count_analog // 16, count_analog_board)
    print(count_analog % 16, count_analog_board, '\n')