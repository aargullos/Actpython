import functions

def main():
    x = functions.valor()
    i = functions.valor()
    x, i = functions.change_val(x, i)
    print(x, i)


if __name__ == '__main__':
    main()
