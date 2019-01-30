#include <iostream>
using namespace std;

int main() {
    int x, n, total;
    cin >> x;
    cin >> n;
    total = x * (n + 1);

    int data [n];
    for (int i = 0; i < n; i++){
        cin >> data[i];
        total -= data[i];
    }
    cout << total;

}
