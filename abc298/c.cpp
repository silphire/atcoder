#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int i, j;
    int n, q;
    cin >> n;
    cin >> q;

    map<int, multiset<int>> box;
    map<int, set<int>> card;
    for(int k = 0; k < q; k++) {
        int c;
        cin >> c;
        if(c == 1) {
            cin >> i >> j;
            box[j].insert(i);
            card[i].insert(j);
        } else if(c == 2) {
            cin >> i;
            bool f = false;
            for(auto x : box[i]) {
                if(f) {
                    cout << " ";
                }
                f = true;
                cout << x;
            }
            cout << endl;
        } else {
            cin >> i;
            bool f = false;
            for(auto x : card[i]) {
                if(f) {
                    cout << " ";
                }
                f = true;
                cout << x;
            }
            cout << endl;
        }
    }
    return 0;
}