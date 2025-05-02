import math

m = int(input())
for _ in range(m):
    r, n, degree, minute, second = map(int, input().split())
    decimal_degree = degree + minute / 60 + second / 3600

    biggest_slice_ref_angle = (n * decimal_degree) % 360

    upper_bound = 360
    lower_bound = 0
    current_degree = 0
    for i in range((n - 1) % (60 * 60 * 360)):
        current_degree = (current_degree + decimal_degree) % 360
        if biggest_slice_ref_angle < current_degree < upper_bound:
            upper_bound = current_degree
        elif biggest_slice_ref_angle >= current_degree > lower_bound:
            lower_bound = current_degree

    area = math.pi * r ** 2 * ((upper_bound - lower_bound) / 360)
    print(area)


