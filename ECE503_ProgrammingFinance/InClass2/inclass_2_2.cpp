/*
Title: InClass 2_2

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 15/9/2018

Course:332:503 Programming Finance
**/

#include "stdafx.h"
#include <iostream>
using namespace std;

int main(void)
{
	//Get the user's input to make the shape.
	int num=0;
	//Ensure the number is positive and odd.
	while(num<=0||num%2!=1){
	 cout<<"Input a maximum number of spaces in each line(Please input a positive and odd integer):";
	 //Get the number from buffer
	 cin>>num;
	};

	//The length of each line would be space's number plus two
	int line=num+2;
	//Draw the top half part of shape
	for(int top_line=1;top_line<=line/2+1;top_line++){
		//i is each line's length, it help to do calculate
		for(int i=1;i<=line;i++)
		{
			//Judge when print the star in each line
			if(i==line/2+top_line||i==line/2-top_line+2)
				cout<<"*";
			else
				cout<<" ";
		}
		//Print the enter when at each line's end
		cout<<endl;
	}

	//Draw the down half part of shape
	for(int top_line=line/2;top_line>=1;top_line--){
		//i is each line's length, it help to do calculate
		for(int i=line;i>=1;i--)
		{
			//Judge when print the star in each line
			if(i==line/2+top_line||i==line/2-top_line+2)
				cout<<"*";
			else
				cout<<" ";
		}
		//Print the enter when at each line's end
		cout<<endl;
	}
	system("pause");
	return 0;
}

s