#include <bits/stdc++.h>

using namespace std;

int main(void) {
    set<int> s;
    int q;
    int i;

    cin >> q;
    for(i = 0; i < q; i++) {
        int op;
        int x;

        cin >> op >> x;
        if(op == 1) {
            s.insert(x);
        } else if(op == 2) {
            s.erase(x);
        } else {
            const auto it = s.lower_bound(x);
            if(it == s.end()) {
                cout << -1 << endl;
            } else {
                cout << *it << endl;
            }
        }
    }
    return 0;
}