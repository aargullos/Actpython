import random
import functions

def main():

    x = functions.introdueix_num()
    num_random = [random.randint(15,200) for i in range(x)]
    num = functions.adivinar_num()

    if num in num_random:
        print("Esta")
    else:
        print("No esta")

if __name__ == '__main__':
    main()
