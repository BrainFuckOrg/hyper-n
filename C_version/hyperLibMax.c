//
// Created by maximus on 11.01.23.
//

#include "hyperLibMax.h"
int hyperN(int number1, int number2, int n){
    if(n==1)
    {
        return number1+number2;
    }
    if(number2 == 1)
        return number1;
    return hyperN(number1,hyperN(number1,number2-1, n), n-1);
}