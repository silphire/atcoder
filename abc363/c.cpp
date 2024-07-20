#include <bits/stdc++.h>

using namespace std;

int main(void) {
    int n, k;
    cin >> n >> k;

    string s;
    cin >> s;
    std::sort(s.begin(), s.end());

    set<string> found;
    int ans = 0;

    do {
        if(found.find(s) != found.end()) {
            continue;
        }
        found.insert(s);
        
        bool f = true;
        for(int i = 0; i < n; i++) {
            int l = i;
            int r = l + k - 1;
            if(r >= n) {
                break;
            }

            bool fc = true;
            while(l < r) {
                if(s[l] != s[r]) {
                    fc = false;
                    break;
                }
                l++; r--;
            }
            if(fc) {
                f = false;
                break;
            }
        }
        if(f) {
            ans++;
        }

    }while(next_permutation(s.begin(), s.end()));

    cout << ans << endl;
    return 0;
}