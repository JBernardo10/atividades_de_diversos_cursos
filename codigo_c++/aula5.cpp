#include<iostream>
using namespace std;

//aula incremento e decremento de variaveis

int main(){
    int n1, n2;
    n1 = 5;
    n2 = 10;

    //pos-incremento
    cout << n1 <<"\n\n";//5
    //n1 = n1+1;
    //n1++;
    //n1+=25;
    //n1*=2;
    //n1/=2;
    //cout << n1 << "\n\n";//2

    //pre-incremento
    //++n1;

    cout << n1++ << "\n\n";
    cout << --n1 << "\n\n";
    return 0;
}
