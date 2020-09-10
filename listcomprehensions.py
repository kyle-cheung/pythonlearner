temps = [221, 234, 340, 230, -999]

new_temp = [temp/10 for temp in temps if temp > 0]

print(new_temp)