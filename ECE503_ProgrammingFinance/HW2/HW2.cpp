/*
Title: Homework 2: Monte Carlo Assignment

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 9/18/2018

Course:332:503 Programming Finance
**/

#include <iostream>
#include <math.h>
#include <ctime>
#include <cstdlib>
#include <fstream>


using namespace std;

//use a function to calculate
double getPi(int);
int main()
{

    //initial the rounds
    int num=0;

    //use a loop to calculate
    while(num<=0){
        //ask user to input a value
        cout<<"Please enter how many rounds you want to calculate the Pi(enter 0 to exit):";
        //get the value from the buffer
        cin>>num;

        //judge whether to break the loop
        if(num==0)
            break;

        //calculate the pi and print its value
        cout<<getPi(num)<<endl;

        //reset the rounds
        num=0;
    }
    return 0;
}

double getPi(int num)
{
    ofstream file;
    //opens the file record.txt
	file.open("record.txt");

    //initial the random number function
    srand(time(0));
    double x=0;
    double y=0;
    double pi=0;
    int inCircle=0,outCircle=0;

    //a loop to simulate the points in Monte Carlo methods
    for(int i=0;i<num;i++){
        x = rand() * 1.0 / RAND_MAX;
		y = rand() * 1.0 / RAND_MAX;

		//judge whether the point is in the circle
        if(y<=sqrt(1-pow(x,2)))
            inCircle++;
        else
            outCircle++;

        //write the values to the file
        file<<x<<","<<y<<"\n";

    }

    //calculate the pi by records of points
    pi=(double)4.0*inCircle/(double)num;

    //return the result to main function
    return pi;
}

