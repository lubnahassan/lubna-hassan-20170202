
#include <iostream>
#include <string>

using namespace std;
int arr[] = {-1,-1,-1,-1,-1,-1,-1,-1,-1};
bool checkwinner()
{
    if (arr[0] + arr[1] + arr[2] == 15 && arr[0]!=-1 && arr[1]!=-1 && arr[2]!=-1)
        return true;
    if (arr[3] + arr[4] + arr[5] == 15 && arr[3]!=-1 && arr[4]!=-1 && arr[5]!=-1)
        return true;
    if (arr[6] + arr[7] + arr[8] == 15 && arr[6]!=-1 && arr[7]!=-1 && arr[8]!=-1)
        return true;

    if (arr[0] + arr[3] + arr[6] == 15 && arr[0]!=-1 && arr[3]!=-1 && arr[6]!=-1)
        return true;
    if (arr[1] + arr[4] + arr[7] == 15 && arr[1]!=-1 && arr[4]!=-1 && arr[7]!=-1)
        return true;
    if (arr[2] + arr[5] + arr[8] == 15 && arr[2]!=-1 && arr[5]!=-1 && arr[8]!=-1)
        return true;

    if (arr[0] + arr[4] + arr[8] == 15 && arr[0]!=-1 && arr[4]!=-1 && arr[8]!=-1)
        return true;
    if (arr[2] + arr[4] + arr[6] == 15 && arr[2]!=-1 && arr[4]!=-1 && arr[6]!=-1)
        return true;

    return false;
}

//0 | 1 | 2
//3 | 4 | 5
//6| 7 | 8

//
void printarr()
{
    cout << endl;
    for (int i = 0; i < 9; ++i)
    {

        if ((i+1)%3==0)             //if i'm printing the third one
        {
            if (arr[i] == -1)
                cout << " " << "\n";
            else
                cout << arr[i] << "\n";
        }
        else
        {
            if (arr[i] == -1)
                cout << " " << " | ";
            else
                cout << arr[i] << " | ";
        }
    }
}
int main()
{
    printarr();

    int num,pos;
    int i;
    for (i=0; i<9; ++i)
    {
        if (i%2!=0)
        {
            cout << "player 2: ";
        }
        else
        {
            cout << "player 1: ";
        }
        cin >> num >> pos;
        while (true){
            if ( arr[pos-1] != -1 ){
                    cout<<"this position is not empty"<<endl;
                    cin >> pos;
            }
            else{
                break;
            }

        }
        if (i%2==0)
        {
            while (num%2==0)
            {
                cout << " enter odd number: ";
                cin >> num;
            }
        }

        if (i%2!=0)
        {
            while (num%2!=0)
            {
                cout <<" enter even number: ";
                cin >> num;
            }
            /* if (num == num)
             {
                 cin >>num;
             }
             */
        }
        while (true){
          bool check = false;
          for (int i=0 ; i<9 ; ++i){
                if (arr[i]==num)
                {
                    check = true;
                    break;
                }
        }
        if ( check == true ){
            cout<<"opps!! this value is not avaliable";
            cin>> num;
        }
        else{
                break;}

        }

            arr[pos-1] = num;
            printarr();
            if (checkwinner())
            {
                if (i%2!=0)
                {
                    cout << "player 2 won!!";
                }
                else
                {
                    cout << "player 1 won!!";
                }

                break;
            }
    }
    return 0;
}

