def draw_star(n, data):
    new_data = []
    if n == 3:
        return data
    else:
        for i in data:
            new_data.append(i * 3)
        for i in data:
            new_data.append(i + ' ' * len(data) + i)
        for i in data:
            new_data.append(i * 3)
        
        return draw_star(n//3, new_data)
    

n = int(input())
default_data = ['***', '* *', '***']
result_data = draw_star(n, default_data)

for i in result_data:
    print(i)
        
