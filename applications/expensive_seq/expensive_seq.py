def expensive_seq(x, y, z):
    # cache = {}

    # if x <= 0:
    #     return y + z
    # if x not in cache:
    #     cache[x] = expensive_seq(x-1, y+1,z)

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
