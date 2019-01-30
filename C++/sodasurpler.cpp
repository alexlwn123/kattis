#include <iostream>

using namespace std;

int main() {
    int e,f,c;
    cin >> e;
    cin >> f;
    cin >> c;
    
    int count = 0, left = e+f; 
    while(left >= c) {
        count += 1;
        left -= c;
        left += 1;
    }

    cout << count << endl;
    

}
