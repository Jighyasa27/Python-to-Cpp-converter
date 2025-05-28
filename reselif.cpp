#include <iostream>
using namespace std;

int main() {
    int x = 20;
    if (x < 10) {
        cout << "Less than 10" << endl;
    }
    else if (x < 30) {
        cout << "Between 10 and 29" << endl;
    }
    else {
        cout << "30 or more" << endl;
    }
    return 0;
}