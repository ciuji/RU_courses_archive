/*
Title: InClass4: recursive

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 6/10/2018

Course:332:503 Programming Finance
**/

#include "stdafx.h"
#include <iostream>
//prototype
int recursive(int,int,int,int );
using namespace std;

int main(){
    //use n to get user's input.
    int n=0;
    //use a loop to do get different input.
    for(;;){
        cout<<"Enter a integer(enter 0 to quit):";
        cin>>n;
        //if user input 0, break the loop;
        if(n==0) break;
        //initial the parameters.
        int i = 1;
        int ans=0;

        //call the recursive function.
        ans=recursive(n,1,i,ans);
        //output the result.
        cout<<"The result is:"<<ans<<endl;
    }
    system("pause");
    return 0;
}

//function of recursive.
int recursive(int n,int iszero,int i,int ans)
{
    //judge when should we end the recursive
    if (i<=n){
        //if the i position is 0, the i+1 must be not 0.
        if (iszero==0)
        {
            //call the recursive with i+1 position is 1.
            ans=recursive(n,1,++i,ans);
            //at the end of the list, back to the i-1 position.
            i--;
        }
        //if the i position is 1, the i+1 can be 0 or 1.
        else
        {
            //call the recursive with i+1 position is 1.
            ans=recursive(n,1,++i,ans);
            i--;
            //call the recursive with i+1 position is 0.
            ans=recursive(n,0,++i,ans);
            i--;
            //at the end of the list, back to the i-1 position.
        }
    }
    else
    {
        //every time we get the end of the list. the result plus +1.
        ans++;
        //return the result.
        return ans;
    }
}
