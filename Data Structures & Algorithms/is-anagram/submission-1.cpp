class Solution {
public:
    bool isAnagram(string s, string t) {
        
        map<char, int> mymap;

        if(s.size() != t.size()) {
            return false;
        }

        for(int i = 0; i < s.size(); i++) {

            if(!mymap.contains(s[i])) {
                mymap.insert({s[i], 1});
            } else {
                mymap[s[i]]++;
            }
        }


        for(int j = 0; j < t.size(); j++) {

            if(mymap.contains(t[j]) && mymap[t[j]] > 0) {
                mymap[t[j]]--;
                continue;
            } else {
                return false;
            }
        }

        return true;

    }
};
