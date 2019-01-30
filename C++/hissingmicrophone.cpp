#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    if (str.find("ss") != std::string::npos) {
        cout << "hiss";
    } else {
        cout << "no hiss";
    }
}
