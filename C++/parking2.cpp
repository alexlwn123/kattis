#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i<t; i++) {
        int n;
        cin >> n;
        
        int s = 100, l = -1; 
        for (int j = 0; j < n; j++) {
            int x;
            cin >> x;
            
            l = max(x, l);
            s = min(x, s);

        }
        cout << 2 * (l-s) << endl;
    }
}
