#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        
        int x;
        cin >> x;
        cin >> x;

        int total = 0, odd = 0, even = 0;

        for (int j = 1; j <= x; j++) {
            total += j;
            even += 2*j;
            odd += 2*j-1;
        }
        cout<<i+1<<" "<<total<<" "<<odd<<" "<<even<<endl;

    }

}
