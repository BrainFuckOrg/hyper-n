//
// Created by kosenko on 11.01.23.
//

#include "hyperLibSanya.h"
int hyper_n(int num1, int num2, int grade){
    //for(int i=0; i<num2; i++){
        if(grade==1)return num1+num2;
        else{
            int result=num1;
            for(int i=1; i<num2; i++){
                result= hyper_n(num1, result, grade-1);
            }
            return result;
        }
    //}
}
