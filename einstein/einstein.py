def main():
    m = int(input('enter mass: '))
    print(energy(m))


def energy(m):
    c  = 300000000
    E = m * (c ** 2 )
    return E


if __name__ == '__main__':
    main()


