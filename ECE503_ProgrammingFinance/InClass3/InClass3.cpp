/*
Title: InClass3 (RSC vote Program)

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 21/9/2018

Course:332:503 Programming Finance
**/
#include "stdafx.h"
#include <iostream>
#include <stdio.h>
using namespace std;

//function prototype
inline void voteFunc(int [], int);

int main()
{
    //initial the arrays, one for count each one's vote, one for count the candidates' votes
    int candidate[5]={0};
    int counts[20]={0};

    //get user's input
    for(int i = 0; i<20;i++)
    {
        cout<<"Student " << i+1 << " pleases enter the number of candidate(if you want to change the last input, enter -1):"<<endl;
        cin>> counts[i];
        //if the user input -1, he would go back to the last position and vote again.
        if(counts[i]==-1)
            i-=2;

    }

    //calculate each candidate's vote
    for(int i=0;i<20;i++)
    {
        voteFunc(candidate, counts[i]-1);
    }

    //find the highest voted candidate. Use maxValue and maxPosition to store the data.
    int maxValue = candidate[0];
    int maxPosition = 0;
    for (int i=0;i<5;i++){
        if(maxValue<candidate[i])
        {
            maxValue = candidate[i];
            maxPosition = i;
        }
    }

    //judge whether there have more than 1 people have the same highest vote counts.
    for(int i =0;i<5;i++){
        if(maxPosition != i ){
            //if there is two people have the same votes, break the program.
            if(candidate[i]==maxValue)
            {
                cout<<"There is no winner!"<<endl;
                system("pause");
                return 0;
            }
        }
    }

    //output the result
    cout<<"candidate "<<maxPosition+1<<" is the winner!"<<" He/She got "<<maxValue<<" votes."<<endl;
    system("pause");
    return 0;

}

//calculate each candidate's votes
inline void voteFunc(int candidate[],int vote)
{
    candidate[vote]++;
}
