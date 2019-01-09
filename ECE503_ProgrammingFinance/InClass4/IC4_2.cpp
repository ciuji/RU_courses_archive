/*
Title: InClass4: recursive

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: 6/10/2018

Course:332:503 Programming Finance
**/

#include <iostream>
//prototype
int recursive(int,int,int,int );
using namespace std;

int main(){
    cout<<"Enter a integer(enter 0 to quit):"<<endl;
    int i = 1;
    int ans=0;
    ans=recursive(4,1,i,ans);
    cout<<ans<<endl;
    return 0;
}

int recursive(int n,int iszero,int i,int ans)
{
    if (i<=n){
        cout<<ans<<"    "<<iszero<<"    "<<i<<endl;
        if (iszero==0)
        {
            i++;
            ans=recursive(n,1,i,ans);
            --i;

        }
        else
        {
            ans=recursive(n,1,++i,ans);
            --i;
            ans=recursive(n,0,++i,ans);
            --i;
        }

    }
    else
    {
        ans++;
        cout<<"return here"<<iszero<<"  "<<ans<<endl;
        return ans;
    }
}
