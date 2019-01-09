
/*
Homework 4 - 16:332:503:02 F17
Author: Zhongze Tang
Email: zhongze.tang@rutgers.edu
Time: 2017/10/5
Description: A Booklist Manager Program
IDE: Visual Studio 2017 Community
Version: 0.0.1
*/

#include<iostream>
#define MAX_NUM 20 //the max number of the books in the list

using namespace std;

int callMenu();
bool insert(int booklist[], int* num, int book); //1, return true when insert successfully
bool insertByPosition(int booklist[], int* num, int position, int book);//2, return true when insert successfully
int findByLinear(int booklist[], int num, int book);//3, return -1 when book not found, or return the position
int findByBinary(int booklist[], int num, int book, bool if_sorted);//4, return -1 when book not found, or return the position
void deleteByPosition(int booklist[], int* num, int position);//5
void deleteByISBN(int booklist[], int* num, int book);//6
void sortBySelection(int booklist[], int num);//7
void sortByBubble(int booklist[], int num);//8
void print(int booklist[], int num);//9


int main()
{
	bool flag = false, if_sorted = false;
	int booklist[MAX_NUM] = { 0 };
	int num = 0;

	//while user doesnt choice to quit the programme
	while (!flag)
	{
		int choice = callMenu();
		int book = 0, position = 0;
		if ((choice >= 1 && choice <= 4) || (choice == 6)) //when user need to add ,find or delete a book using ISBN
		{
			cout << "Please enter the ISBN of the book:" << endl;
			cin >> book;
			cin.clear();
			cin.ignore(1024, '\n');//if the user input more than one number, ignore it.
		}

		if ((choice == 2) || (choice == 5)) //when user need to add or delete a book by position
		{
			cout << "At what position?" << endl;
			cin >> position;
			cin.clear();
			cin.ignore(1024, '\n');
		}

		switch (choice)
		{
		case 1: //add, when insert successfully, set if_sorted as false.
			if(insert(booklist, &num, book)) if_sorted = false;
			break;

		case 2: //add by position
			if(insertByPosition(booklist, &num, position, book)) if_sorted = false;
			break;

		case 3: //find linear
			findByLinear(booklist, num, book);
			break;

		case 4: //find binary
			findByBinary(booklist, num, book, if_sorted);
			break;

		case 5: //delete by position
			deleteByPosition(booklist, &num, position);
			break;

		case 6://delete by isbn
			deleteByISBN(booklist, &num, book);
			break;

		case 7:  //sort by selection
			sortBySelection(booklist, num);
			if_sorted = true;
			break;

		case 8: //sort by bubble
			sortByBubble(booklist, num);
			if_sorted = true;
			break;

		case 9:
			print(booklist, num);
			break;
		case 0:
			flag = true; //quit
			break;
		default:
			cout << "Please enter the right choice!" << endl;
			break;
		}
	}

//	system("pause");
	return 0;
}

int callMenu()
{
	//show the main menu
	int choice = 10;
	cout << endl << "Welcome to the Book List Program!" << endl;
	cout << "What would you like to do?" << endl;
	cout << "\t1: Add an book to the end of the list" << endl;
	cout << "2: Add an book at a position" << endl;
	cout << "3: Find a book by ISBN number (linear search)" << endl;
	cout << "4: Find a book by ISBN number (binary search)" << endl;
	cout << "5: Delete a book at a position" << endl;
	cout << "6: Delete a book by ISBN number" << endl;
	cout << "7: Sort the list (using selection sort)" << endl;
	cout << "8: Sort the list (using bubble sort)" << endl;
	cout << "9: Print the list" << endl;
	cout << "0: Exit" << endl;
	cout << "Please enter your choice: ";
	cin >> choice;
	cin.clear(); //reset cin, in order to prevent the user enter an alphabet, etc.
	cin.ignore(1024, '\n'); //if the user input more than one choice, ignore it.
	return choice;
}

//1 insert the book to the end of the list
bool insert(int booklist[], int* num, int book)
{
	//the end of the list is (*num) + 1, so just call insertByPosition()
	bool result = insertByPosition(booklist, num, (*num)+1, book);
	return result;
}

//2 insert the book to a certain position of the list
bool insertByPosition(int booklist[], int* num, int position, int book)
{
	if (*num < MAX_NUM) //when the list is not full
		if (position >= 1 && position <= (*num) + 1) // when position is in the range of list
		{
			for (int i = *num; i >= position; i--)
				*(booklist + i) = *(booklist + i - 1); //move the books behind the position to next one
			*(booklist + position - 1) = book; //add the book to the list
			(*num)++; //the number of books in the list + 1
			print(booklist, *num);
			return true;
		}
		else
		{
			cout << "Error: Invalid postion." << endl;
			return false;
		}
	else
	{
		cout << "Error: The book list is full." << endl;
		return false;
	}
}

//3 find a book by linear search
int findByLinear(int booklist[], int num, int book)
{
	int position = -1; //default result, when book no found return -1
	for(int i = 0; i < num; i++)
		if (*(booklist + i) == book) //compare the ISBN with all the books in the list
		{
			position = i + 1;
			break;
		}
	if (position == -1)
	{
		cout << "Error: Book not found." << endl;
	}
	else
	{
		cout << "The book is in position " << position << "." << endl;
	}
	return position;
}

//4 find a book by binary search
int findByBinary(int booklist[], int num, int book, bool if_sorted)
{
	int position = -1;
	if (if_sorted) //before using findByBinary, user have to sort the list first
	{
		int low = 0, high = num - 1, mid = (low + high) / 2;
		while (low <= high)
		{
			if (book == *(booklist + mid)) //find the book
			{
				position = mid + 1;
				break;
			}
			else  // change the low or the high to reset the range
			{
				if (book > *(booklist + mid))
				{
					low = mid + 1;
					mid = (low + high) / 2;
				}
				else
				{
					high = mid - 1;
					mid = (low + high) / 2;
				}

			}
		}
	}
	else
	{
		cout << "Error: You have to sort the list first." << endl;
		return position;
	}

	if (position == -1)
	{
		cout << "Error: Book not found." << endl;
	}
	else
	{
		cout << "The book is in position " << position << "." << endl;
	}
	return position;
}

//5 delete a book at a certain position
void deleteByPosition(int booklist[], int* num, int position)
{
	if (position >= 1 && position <= *num)
	{
		for (int i = position; i < *num; i++)
			*(booklist + i - 1) = *(booklist + i); //move books to the front
		(*num)--; // number of books in the list - 1
		print(booklist, *num);
	}
	else
	{
		cout << "Error: Invalid postion." << endl;
	}

}

//6 delete a book by ISBN
void deleteByISBN(int booklist[], int* num, int book)
{
	if (num == 0) // no book to delete
	{
		cout << "Error: The list is empty." << endl;
	}
	else
	{
		int position = findByLinear(booklist, *num, book); //find the position of the book
		if (position != -1)// book found
		{
			deleteByPosition(booklist, num, position); //call deleteByPosition()
		}
	}
}

//7 use selection sort to find the book
void sortBySelection(int booklist[], int num)
{
	for (int i = 0; i < num - 1; i++)
	{
		int min_pos = i;
		for (int j = i; j < num; j++)
		{
			if (*(booklist + j) < *(booklist + min_pos))
			{
				min_pos = j;
			}
		}
		int temp = *(booklist + min_pos);
		*(booklist + min_pos) = *(booklist + i);
		*(booklist + i) = temp;
	}


	cout << "The selection sort is done." << endl;
	print(booklist, num);
}

//8 use bubble sort to find the book
void sortByBubble(int booklist[], int num)
{
	for(int i = 0; i < num - 1; i++)
		for (int j = 0; j < num - i - 1; j++)
		{
			if (*(booklist + j) > *(booklist + j + 1))
			{
				int temp = *(booklist + j);
				*(booklist + j) = *(booklist + j + 1);
				*(booklist + j + 1) = temp;
			}
		}

	cout << "The bubble sort is done." << endl;
	print(booklist, num);
}

//9 print the book list
void print(int booklist[], int num)
{
	cout << "Your book list now is:" << endl;
	if(num == 0)
		cout << "Empty." << endl;
	for (int i = 0; i < num; i++)
		cout << i+1 << ". " <<booklist[i] << endl;
	cout << endl;
}
