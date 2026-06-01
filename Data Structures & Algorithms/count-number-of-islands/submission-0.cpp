class Solution {
public:

    void explore(int r, int c, vector<vector<char>>& grid,  set<pair<int,int>>& visited) {

        if(r < 0 || r >= grid.size() || c < 0 || c >= grid[r].size()) {
            return;
        }

        if(visited.count({r, c})) {
            return;
        }

        visited.insert({r, c});

        if(grid[r][c] == '0') {
            return;
        }

        explore(r-1, c, grid, visited);
        explore(r+1, c, grid, visited);
        explore(r, c - 1, grid, visited);
        explore(r, c+1, grid, visited);
    }


    int numIslands(vector<vector<char>>& grid) {
        
        set<pair<int,int>> visited;

        int islands = 0;

        for(int i = 0; i < grid.size(); i++) {
            for(int j = 0; j < grid[i].size(); j++) {

                if(!visited.count({i, j})) {
                    if(grid[i][j] == '1') {

                        islands++;
                        explore(i, j, grid, visited);

                    } else {
                        visited.insert({i, j});
                        continue;
                    }
                } else {
                    continue;

                }
            }
        }

        return islands;




    }
};



