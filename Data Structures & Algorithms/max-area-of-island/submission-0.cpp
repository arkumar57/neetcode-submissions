class Solution {
public:

    int explore(int r, int c, vector<vector<int>>& grid, set<pair<int, int>>& visited) {

        int result = 0;
        if(r < 0 || r >= grid.size() || c < 0 || c >= grid[r].size()) {

            return 0;
        }

        if(visited.count({r, c})) {
            return result;
        }

        visited.insert({r, c});

        if(grid[r][c] == 1) {
            result++;
            result += explore(r - 1, c, grid, visited);
            result += explore(r + 1, c, grid, visited);
            result += explore(r, c - 1, grid, visited);
            result += explore(r, c + 1, grid, visited);
        } else {
            return result;
        }

        return result;


    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        
        set<pair<int, int>> visited;
        
        int max = 0;

        for(int i = 0; i < grid.size(); i++) {

            for(int j = 0; j < grid[i].size(); j++) {
                

                if(!visited.count({i, j})) {

                    if(grid[i][j] == 1) {

                        int r = explore(i, j, grid, visited);

                        cout << r << endl;
                        if(r >= max) {
                            max = r;
                        } else {
                            continue;
                        }

                    } else {
                        continue;
                        // visited.insert({i, j});
                    }

                } else {
                    continue;
                }

            }
        }

        return max;


    }
};
