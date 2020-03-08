#include <bits/stdc++.h>

using namespace std;

char ans[600000];
int start = 200000;
int n = 0;

int main(void) {
    string s;
    string qs;
    int qn;
    cin >> s;
    cin >> qn;
    getline(cin, qs);

    for(int i = 0; i < s.length(); i++) {
        ans[start + n] = s[i];
        n++;
    }

    bool mode = true;
    for(int i = 0; i < qn; i++) {
        getline(cin, qs);

        if(qs[0] == '1') {
            mode = !mode;
        } else {
            if(qs[2] == '1') {
                if(mode) {
                    --start;
                    ans[start] = qs[4];
                } else {
                    ans[start + n] = qs[4];
                }
            } else {
                if(mode) {
                    ans[start + n] = qs[4];
                } else {
                    --start;
                    ans[start] = qs[4];
                }
            }
            ++n;
        }
    }

    ans[start + n] = '\0';
    string anss(&ans[start]);    
    if(!mode) {
        reverse(anss.begin(), anss.end());
    }

    cout << anss << endl;
    return 0;
}