#include <bits/stdc++.h>

using namespace std;

int main(void) {
    set<int> cut;

    int l, q;
    cin >> l >> q;
    for(int i = 0; i < q; i++) {
        int c, x;
        cin >> c >> x;

        if(c == 1) {
            cut.insert(x);
        } else {
            auto it = cut.lower_bound(x);

            int left, right;
            if(it == cut.end()) {
                right = l;
            } else {
                right = *it;
            }

            if(it == cut.begin()) {
                left = 0;
            } else {
                left = *prev(it);
            }
            
            cout << right - left << endl;
        }
    }
    return 0;
}