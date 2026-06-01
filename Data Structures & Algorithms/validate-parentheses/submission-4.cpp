using namespace std;
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        if(s.size() > 0) {
            if(s[0] != ')' && s[0] != '}' && s[0] != ']') {
                st.push(s[0]);
            } else {
                return false;
            }
        } else {
            return true;
        }

        for(int i = 1; i < s.size(); i++) {
            char x = st.empty() ? ' ' : st.top();
            if(s[i] != ')' && s[i] != '}' && s[i] != ']') {
                st.push(s[i]);
            } else if (s[i] == ')') {
                if(x == '(') {
                    st.pop();
                    continue;
                } else {
                    return false;
                }
            } else if (s[i] == '}') {
                if(x == '{') {
                    st.pop();
                    continue;
                } else {
                    return false;
                }
            } else if (s[i] == ']') {
                if(x == '[') {
                    st.pop();
                    continue;
                } else {
                    return false;
                }
            }
        }

        return st.empty();

    }
};
