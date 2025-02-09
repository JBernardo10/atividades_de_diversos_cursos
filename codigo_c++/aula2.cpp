#include <iostream>

using namespace std;

int main(){
    //tipo nome;
    //tipo nome = valor;

    int vidas = 10;
    char letra = 'j';
    double decimal = 1.123456789101112131415; //2.49999999999
    float decimal2 = 0.123456789101112131415;//2.5
    bool vivo = false;
    string nome = "joao";

    cout <<"digite o numero de vidas: ";
    cin >>vidas;


    cout <<"vidas = " << vidas <<"\n";
    cout <<"letra = " <<letra <<"\n";
    cout <<"decimal double = "<< decimal <<"\n";
    cout <<"decimal float = " <<decimal2 <<"\n";
    cout <<"vivo = " <<vivo <<"\n";
    cout <<"nome = " <<nome <<"\n";

    return 0;
}
