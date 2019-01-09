/*
Title: InClass 2_1

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 15/9/2018

Course:332:503 Programming Finance
**/
#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	//Get the user's input to make the shape.
	int num=0;
	//Ensure the number is positive.
	while(num<=0){
	 cout<<"How many lines you want in the shape?(Please input a positive integer):";
	 //Get the number from buffer
	 cin>>num;
	};

	//Draw the shape
	for(int line=1;line<=num;line++){
		//i is each line's number of star
		for(int i=1;i<=line;i++)
		{
			//print a star
			cout<<"*";
		}
		//print the enter when at each line's end
		cout<<endl;
	}

	system("pause");
	return 0;
}

