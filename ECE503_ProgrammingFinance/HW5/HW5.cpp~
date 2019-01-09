//author ciuji

#include <iostream>
#include <vector>
using namespace std;
#define MAX_NUM 50
void recursive(int , vector<int> *);

int main(){
	int num=0;
	//use a loop to get user's input
	for(;;){
		cout<<"please input an integer(Enter 0 to quit):";
		cin>>num;
		if(num==0) break; //judge weather break the loop;
		//use a vecotr to store the numbers.
		vector <int> arr;
		//call the recursive function
		recursive(num,&arr);
		cout<<"output is:";
		//print the output
		for(int i =0;i<arr.size();i++){
			cout<<arr[i];
			if(i+1<arr.size())
				cout<<",";
			else 
				cout<<endl;
		}
	}
	return 0;
}

void recursive(int num,vector<int> *arr){
	//when num is odd ,use this function.
	if(num%2==1 && num >=1){
		//add the odd number to the arr.
		arr->push_back(num*num);
		//do the recursion.
		recursive(num-2,arr);
		//add the even to the arr.
		if(num-1>0)
			arr->push_back((num-1)*(num-1));
	}
	//when num is even, use this function.
	else if(num%2==0&&num>0){
		//add the odd number to the arr.
		arr->push_back((num-1)*(num-1));
		//do the recursion.
		recursive(num-2,arr);
		//add the even number to the arr.
		arr->push_back(num*num);		
	}

}
