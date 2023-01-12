import time
import hyper_n_Sanya
import hyper_n_Max


def main():
    start = time.perf_counter()

    num1 = 4
    num2 = 3
    grade = 4
    print("norecursion result = ", hyper_n_Sanya.hyper_n_norecursion(num1,num2,grade))
    print("result1 =",hyper_n_Sanya.hyper_n(num1,num2,grade))
    #print("result2 =",hyper_n_Max.hyperN(num1,num2,grade))


if __name__ == '__main__':
    main()
