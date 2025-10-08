num_1, dist_1, vel_1 = map(int, input().split())
num_2, dist_2, vel_2 = map(int, input().split())

dist_f_1 = dist_1 / vel_1
dist_f_2 = dist_2 / vel_2

if (dist_f_1 > dist_f_2):
    print(num_2)
elif (dist_f_1 < dist_f_2):
    print(num_1)