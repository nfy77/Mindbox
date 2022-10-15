import array
import time
from matplotlib import pyplot as plt
    
# сумма цифр числа
def dig_sum(n):
    if n < 10 :
        return n
    return n % 10 + dig_sum( n // 10 )

# целевая функция - можно использовать с 1 или 2 аргументами
def grp_dist(n_customers, n_first_id = 0):
    # максимальное кол-во групп = 9 * кол-во разрядов верхней границы id
    ab_dist = array.array('i', [0]) * (9 * len(str(n_first_id + n_customers)))
    for i in range(n_first_id, n_first_id + n_customers, 1):
        ab_dist[dig_sum(i)] += 1
    return ab_dist

ts = time.time()
ab_dist0 = grp_dist(7412567)
print(ab_dist0, time.time() - ts)

ab_dist1 = grp_dist(741, 2567)
print(ab_dist1)

plt.bar(range(len(ab_dist1)), ab_dist1)