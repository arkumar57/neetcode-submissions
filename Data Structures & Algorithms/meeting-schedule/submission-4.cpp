/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:

    static bool compare(Interval a, Interval b) {

        if(a.start < b.start) {
            return true;
        } else {
            return false;
        }
    }
    bool canAttendMeetings(vector<Interval>& intervals) {
        
        sort(intervals.begin(), intervals.end(), compare);

        int i = 0;

        Interval x = intervals[i];

        for(int j = i + 1; j < intervals.size(); j++) {

            if(intervals[j].start < intervals[i].end) {
                return false;
            } else {
                i = j;
            }
        }

        return true;
        
    }
};

/*





*/