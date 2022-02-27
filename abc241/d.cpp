#include <bits/stdc++.h>
#define INF ((long long)1e19)

using namespace std;

int main(void)
{
    multiset<long long> s;

    for(int i = 0; i < 5; i++) {
        s.insert(0);
        s.insert(INF);
    }

    int q;
    cin >> q;
    while(q--) {
        int c, k;
        long long x;
        
        cin >> c;

        switch(c) {
        case 1:
            {
                cin >> x;
                s.insert(x);
                break;
            }
        case 2:
            {
                cin >> x >> k;
                auto it = s.upper_bound(x);
                while(k--) {
                    it--;
                }
                if(*it == 0) {
                    cout << -1 << endl;
                } else {
                    cout << *it << endl;
                }
                break;
            }
        case 3:
            {
                cin >> x >> k;
                auto it = s.lower_bound(x);
                while(--k) {
                    it++;
                }
                if(*it == INF) {
                    cout << -1 << endl;
                } else {
                    cout << *it << endl;
                }
                break;
            }
        }
    }
    return 0;
}