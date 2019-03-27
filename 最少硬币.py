'''
-* coding:: utf-8 *-
找零钱问题：假设只有 1 分、 2 分、五分、 1 角、二角、 五角、 1元的硬币。
在超市结账 时，如果 需要找零钱， 收银员希望将最少的硬币数找给顾客。
那么，给定 需要找的零钱数目，如何求得最少的硬币数呢？

'''


def greedy():
    # 存数量面值
    document = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1]
    document_num = []
    s = 0

    # 计算收银员有多少钱
    temp = input("请分别输入7种零钱的数量(用空格隔开)：")
    document_num0 = temp.split(" ")

    for i in range(0, len(document_num0)):
        document_num.append(int(document_num0[i]))
        s += document[i] * document_num[i]

    # 输入要找的零钱数
    sum = float(input("请输入需要找的零钱金额："))

    # 判断够不够找钱
    if sum > s:
        print("收银员的钱不够")
        return 0

    # 贪心算法
    else:
        i = 6
        while i >= 0:
            if sum >= document[i]:
                n = int(sum / document[i])
                if n >= document_num[i]:
                    n = document_num[i]
                sum -= n * document[i]
                print("用了%d个%s元硬币" % (n, document[i]))
            i -= 1


# 主函数
if __name__ == '__main__':
    while True:
        greedy()
