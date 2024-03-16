// Purpose : Game 3 (Subtract A Square) here two players play each of them must choose a square number to take it from
//           pile of money and first player reach 0  win!
// Author : Aly El-Deen Yasser Ali
// ID : 20231109       Section : Registration has not opened yet on College Web(S15|S16 in Futrue)
// Version : 3 (Final Version)
// Date : 28|2|2024

#include <iostream>
#include <random>
#include <string.h>

#define ll long long 

using namespace std;

// Defining some functions
// check square function
bool check_square(ll num)
{
    if (num < 0)
        return false;
    if (num == 1 || num == 0)
        return true;
    ll i = 1;
    while (i * i <= num)
    {
        if (i * i == num)
            return true;
        i++;
    }
    return false;
}

// check string function
ll check_string(string word)
{
    while (true)
    {
        cout<<word<<"Enter the number of coins:";
        string pile_choose;
        cin>>pile_choose;
        bool check = true;
        for (char i : pile_choose)      // To check that it is a number not an string
        {
            if(i != '0' && i != '1' && i != '2' && i != '3' && i != '4' && i != '5' && i != '6' && i != '7' && i != '8' && i != '9')
            {
                check = false;
                break;
            }
        }
        if(check == true)
            return stoll(pile_choose);
        else
            cout<<"Invalid!\n";
    }

}

//======================================================= Main Code=========================================================================
int main()
{
    // Showing Game Rules For user
    cout<<"==Welcome To Subtract A Square Game=="<<endl;
    cout<<"Its Description:"<<endl;
    cout<<"================"<<endl;
    cout<<"There are two players that have a pile of coins(input or random)."<<endl;
    cout<<"Each player at his/her turn will choose a number of coins that is square numbers."<<endl;
    cout<<"And so on until you reach 0 first player reach zero will win!"<<endl;
    cout<<"=================================================================================================="<<endl;
    cout<<"=================================================================================================="<<endl;
    cout<<"It's Rules:"<<endl;
    cout<<"==========="<<endl;
    cout<<"1. You have to chose only a square number of numbers like 1, 4, 9, 16, 25, 36,...."<<endl;
    cout<<"2. You can't use a fraction number"<<endl;
    cout<<"3. You cant use an string or char"<<endl;
    cout<<"4. The player who remove the last coin from the pile win"<<endl;
    cout<<"===================================================================="<<endl;

    // To see if user want the number of coins in pile random or he enter it 
    string choice;
    while (true)
    {
        cout<<"How you want the number of coins in pile to be?\n[A] Random number\n[B] Input number\nYour choice: ";
        cin>>choice;
        if (choice == "A" || choice == "a" || choice == "b" || choice == "B") // To check that he choose A or B only
            break;
        else
            cout<<"Enter a valid option\n";
    }

    ll pile ;
    // if he want number of coins to be random
    if (choice == "A" || choice == "a")
    {
        // using random number engine
        random_device rd;
        uniform_int_distribution<int> dist(1,1000);
        // To check that user cant take the whole number in one time
        while (true) 
        {
            ll pile_random = dist(rd);
            if (!check_square(pile_random))
                pile = pile_random;
                break;
        }
    }
    // if he want to input it
    else
    {
        pile = check_string("");
    }

    ll player1 , player2;
    cout << "the number of coins: " << pile <<endl;
    while(true)
    {
        // player 1
        while (true)
        {
            player1 = check_string("Player 1 :");
            if (check_square(player1) && pile - player1 >= 0) //check number is a squared number 
                break;
            else
                cout<<"Invalid!"<<endl;
        }
        pile -= player1;
        // check winner
        if (pile == 0)
        {
            cout<<"==player 1 win!=="<<endl;
            break;
        }
        cout << "the number of coins: " << pile <<endl;
        
        // player 2
        while (true)
        {
            player2 = check_string("Player 2 :");
            if (check_square(player2) && pile - player2 >= 0)//check number is a squared number 
                break;
            else
                cout<<"Invalid!"<<endl;
        }
        pile -= player2;
        
        // check winner
        if (pile == 0)
        {
            cout<<"==player 2 win!=="<<endl;
            break;
        }
        cout << "the number of coins: " << pile <<endl;

    }
    return 0;
}