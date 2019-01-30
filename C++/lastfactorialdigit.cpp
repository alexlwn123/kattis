#include <iostream>
using namespace std;

int fact(int n);

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        cout << fact(n) % 10 <<"\n"; 
    }
}

int fact(int n){
    if (n == 1) {
        return 1;
    }
    return n * fact(n-1);
}
