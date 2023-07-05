#include <bits/stdc++.h>

using namespace std;

int main(void) {
    set<int> table;

    int q;
    cin >> q;
    while(q--) {
        int cmd, x;
        cin >> cmd >> x;

        if(cmd == 1) {
            table.insert(x);
        } else {
            int ans = INT_MAX;

            auto it = table.lower_bound(x);
            if(it != table.end()) {
                ans = min(ans, abs(*it - x));
            }

            if(it != table.begin()) {
                auto jt = it;
                jt--;
                ans = min(ans, abs(*jt - x));
            }

            if(ans == INT_MAX) {
                ans = -1;
            }
            cout << ans << endl;
        }
    }
    return 0;
}