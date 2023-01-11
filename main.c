#include <stdio.h>
#include <time.h>
#include "hyperLibSanya.h"
#include "hyperLibMax.h"
int main() {
    clock_t start, end;
    double execution_time, execution_time1;

    int num1, num2, grade;
    num1 = 2;
    num2 = 15;
    grade = 3;

    start = clock();
    printf("result = %d\n",hyper_n(num1,num2,grade));
    end = clock();
    execution_time = ((double)(end - start));
    printf("time1: %f\n", execution_time);
    start = clock();
    printf("result = %d\n", hyperN(num1,num2,grade));
    end = clock();
    execution_time1 = ((double)(end - start));
    printf("time2: %f\n", execution_time1);
    printf("how much first func faster than second = %f",execution_time1/execution_time);
    return 0;
}
