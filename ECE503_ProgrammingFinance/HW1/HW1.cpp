/*
Title: Homework 1

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 9/9/2018

Course:332:503 Programming Finance
**/
#include "stdfx.h"
#include <iostream>

using namespace std;
int main(void)
{
    //declaration of variables
    double num1,num2,num3,num4,num5,min,max;

    //ask the user to enter five numbers
    cout<<"Please enter five numbers"<<endl;

    //get user's input
    cin>>num1>>num2>>num3>>num4>>num5;

    //find the maximum and minimum of those numbers
    if(num1>num2)
    {
        min=num2;
        max=num1;
    }
    else
    {
        min=num1;
        max=num2;
    }

    if(num3>max)
        max=num3;
    else if(num3<min)
        min=num3;

    if(num4>max)
        max=num4;
    else if(num4<min)
        min=num4;

    if(num5>max)
        max=num5;
    else if(num5<min)
        min=num5;

    //display the maximum and minimum as result
    cout<<"Maximum of these numbers: "<<max<<endl;
    cout<<"Minimum of these numbers: "<<min<<endl;

    system("pause");
    return 0;


}
