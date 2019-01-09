/*
Title:

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time:

Course:332:503 Programming Finance
**/
#include "stdafx.h"
#include <iostream>
using namespace std;
#define MAXIMUN 20
void insert(int mylist[ ], int* num_in_list, int new_element);
void insert_at(int mylist[ ], int* num_in_list, int at_position, int new_element);
int find_linear(int mylist [ ], int num_in_list, int element);
int find_binary(int mylist [ ], int num_in_list, int element);
void delete_item_position(int mylist [ ], int* num_in_list, int position) ;
void delete_item_isbn(int mylist [ ], int* num_in_list, int element) ;
void sort_list_selection(int mylist [ ], int num_in_list);
void sort_list_bubble(int mylist [ ], int num_in_list);
void print (int mylist[ ], int num_in_list);
int menuFun();
//use global variable to record weather the list is sorted.
int sorted=0;
int main(){
    cout << "Welcome to the Book List Program!" << endl;
    int arr[MAXIMUN] = {0};
 	int choice = menuFun();
 	int item = 0;
 	int num_in_list=0;
 	int position =0;
 	while(choice!=0){
        //get the ISBN of book
        if(choice==1 || choice==2 || choice==3 || choice==4 || choice==6){
            cout<<"Please type in the element"<<endl;
            cin>>item;
        }
        //get the position
        if(choice==2 || choice==5){
            cout<<"At what position?"<<endl;
            cin>>position;
        }
         switch(choice){
            case 1: insert(arr,&num_in_list,item);break;
            case 2: insert_at(arr,&num_in_list,position,item);break;
            case 3: find_linear(arr,num_in_list,item); break;
            case 4: {
                if(sorted)
                    find_binary(arr,num_in_list,item);
                else
                    cout<<"Sorry, your have to sort the list before binary search."<<endl;
                }break;
            case 5: delete_item_position(arr,&num_in_list,position);break;
            case 6: delete_item_isbn(arr,&num_in_list,item);break;
            case 7: sort_list_selection(arr,num_in_list);break;
            case 8: sort_list_bubble(arr,num_in_list);break;
            case 9: print(arr,num_in_list);break;
            case 0: choice=0;break;
            default: cout<<"Not supported!"<<endl;break;
        }
        choice=menuFun();
 	}
    system("pause");
    return 0;
}
//show menu
int menuFun(){
    int choice = 0;
	cout << "What would you like to do?" << endl;
	cout << "\t1. Add an book to the end of the list" << endl;
	cout << "\t2. Add an book at a position" << endl;
	cout << "\t3. Find a book by ISBN number (linear search)" << endl;
	cout << "\t4. Find a book by ISBN number (binary search)" << endl;
	cout << "\t5. Delete a book at a position" << endl;
	cout << "\t6. Delete a book by ISBN number" << endl;
	cout << "\t7. Sort the list (using selection sort)" << endl;
	cout << "\t8. Sort the list (using bubble sort)" << endl;
	cout << "\t9. Print the list" << endl;
	cout << "\t0. Exit" << endl;
	cout << "your choice --- "<<endl;
	cin >> choice;
	cin.clear();
	return choice;
}

//insert the new book to the end of the list.
void insert(int mylist[ ], int * num_in_list, int new_element){
    insert_at(mylist,num_in_list,(*num_in_list)+1,new_element);

}
//insert the new book at special position;
void insert_at(int mylist[ ], int* num_in_list, int position, int new_element){
    if (*num_in_list<MAXIMUN){
        if(position>=1&&position<=(*num_in_list)+1){
            for(int i = *num_in_list;i>=position;i--){
                *(mylist+i)= *(mylist+i-1);
            }
            *num_in_list+=1;
            *(mylist+position-1)=new_element;
            print(mylist,*num_in_list);
            sorted = 0;
        }
        else{
            cout<<"Error: Wrong position!"<<endl;
        }
    }
    else{
        cout<<"Error: You can not buy more than 20 books"<<endl;
    }
}

//use linear search to find a book.
int find_linear(int mylist [ ], int num_in_list, int element){
    //use result to store the position.
    int result = 0;
    for(int i=0;i<num_in_list;i++){
        if(*(mylist+i)==element){
            result = i+1;
            break;
        }
    }
    if(result){
            cout<<"The book you search is in position "<<result<<endl;
    }
    else{
            cout<<"Sorry, Book not found"<<endl;

    }
    return result;
}
//use binary search to find a book.
int find_binary(int mylist [ ], int num_in_list, int element){
    //use result to store the position.
    int result = 0;
    if(sorted){
        //initial the parameters. hp is the high position, lp is the low position.
        int lp=0, hp = num_in_list -1;
        int mp = (lp+hp)/2;
        //do the binary search.
        while(lp<=hp){
            if(element==*(mylist+mp)){
                result = mp+1;
                break;
            }
            else{
                if (element>*(mylist+mp)){
                    lp = mp +1;
                    mp=( lp + hp )/2;
                }
                else
                {
                    hp=mp-1;
                    mp=(hp+lp)/2;
                }
            }
        }
        sorted = 1;
    }

    if (result){
        cout<<"The book your search is in position "<<result<<endl;
    }
    else{
        cout<<"Sorry, book not found"<<endl;
    }
    return result;

}
//delete a book by position
void delete_item_position(int mylist [ ], int * num_in_list, int position){
    if(position >=1 && position<=*num_in_list){
        //move the element in list
        for (int i = position;i<*num_in_list;i++){
            *(mylist+i-1)=*(mylist+i);
        }
        (*num_in_list)-=1;
        print(mylist,*num_in_list);
    }
    else{
        cout<<"Error: Wrong position!"<<endl;
    }
}
//use book's ISBN to delete
void delete_item_isbn(int mylist [ ], int *num_in_list, int element){
    //find the position of the book.
    int position = 0;
    for(int i=0;i<* num_in_list;i++){
        if(*(mylist+i)==element){
            position = i+1;
            break;
        }
    }
    if(!position){
            cout<<"Sorry, Book not found"<<endl;

    }
    else
        delete_item_position(mylist,num_in_list,position);
}
//find the book by selection sort
void sort_list_selection(int mylist [ ], int num_in_list){
    //selection sort
    int temp=0;
    for (int i = 0; i < num_in_list - 1; i++)
    {
            int min_pos = i;
            for (int j = i; j < num_in_list; j++)
            {
                if (*(mylist + j) < *(mylist + min_pos))
                {
                    min_pos = j;
                }
            }
            temp = *(mylist + min_pos);
            *(mylist + min_pos) = *(mylist + i);
            *(mylist + i) = temp;
    }


	cout << "Selection sort successfully!" << endl;
	sorted=1;
	print(mylist, num_in_list);
}

void sort_list_bubble(int mylist [ ], int num_in_list){
    int temp=0;
    //do the bubble.
    for(int i=0;i<num_in_list-1;i++){
        for(int j=0;j<num_in_list-i-1;j++){
            if(*(mylist+j)>*(mylist+j+1)){
                temp = *(mylist+j);
                *(mylist+j)=*(mylist+j+1);
                *(mylist+j+1)= temp;
            }
        }
    }
    cout<<"Bubble sort successfully!"<<endl;
    sorted=1;
    print(mylist,num_in_list);
}

void print (int mylist[ ], int num_in_list){
    cout<<"Your list is now:"<<endl;
    //if their is no book in the list.
    if(!num_in_list){
        cout<<"No book"<<endl;
    }
    else{
        for(int i=0;i<num_in_list;i++){
            cout<<i+1<<". "<<*(mylist+i)<<endl;
        }
        cout<<endl;
    }
}
