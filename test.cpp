#include<iostream>
#include<vector>

using namespace std;

class Foo {
    public:

    int bar(int * arr, int n) {
        for (int i = 0; i < n; i++) {
            arr[i] *= arr[i];
        }
    }

    int bar2(vector<int> * arr, int n) {
        for (int i = 0; i < n; i++) {
            (*arr)[i] *= (*arr)[i];
        }
    }

    int bar3(vector<int> arr) {
        for (int i = 0; i < arr.size(); i++) {
            cout << arr[i];
        }
    }
};


int main () {

    int arr[3] = {1, 2, 3};
    vector<int> vec (arr, arr+3);
    vector<int> vec2 (arr, arr+3);

    Foo foo;
    foo.bar(arr, 3);
    foo.bar2(&vec, 3);
    foo.bar3(vec);

    for (int i = 0; i < 3; i++) cout << arr[i] << " ";
    for (int i = 0; i < 3; i++) cout << vec[i] << " ";

    return 0;
}

