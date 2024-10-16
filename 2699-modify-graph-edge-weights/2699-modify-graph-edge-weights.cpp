#include <vector>
#include <algorithm>
#include <limits>

using std::vector;
using std::fill;
using std::min;

constexpr int INF = 2e9; // Define constant for infinity value.

class Solution {
public:
    // Function to modify graph edges such that the shortest path equals the target distance.
    vector<vector<int>> modifiedGraphEdges(int n, vector<vector<int>>& edges, int source, int destination, int target) {
        long long shortestDistance = dijkstra(edges, n, source, destination);
        if (shortestDistance < target) { // If current shortest path is less than target, it's not possible.
            return {};
        }
        bool isEqualToTarget = shortestDistance == target;
        for (auto& edge : edges) {
            if (edge[2] > 0) { // If an edge already has positive weight, skip it.
                continue;
            }
            if (isEqualToTarget) { // If current path length equals target, set the weight to infinity.
                edge[2] = INF;
                continue;
            }
            // Temporarily set weight to 1 and recalculate shortest path.
            edge[2] = 1;
            shortestDistance = dijkstra(edges, n, source, destination);
            if (shortestDistance <= target) { // If path matches or is smaller than target, adjust weight.
                isEqualToTarget = true;
                edge[2] += target - shortestDistance;
            }
        }
        return isEqualToTarget ? edges : vector<vector<int>>{};
    }

    // Dijkstra's algorithm to find the shortest path from src to dest.
    long long dijkstra(const vector<vector<int>>& edges, int n, int src, int dest) {
        long long graph[n][n];
        long long distance[n];
        bool visited[n];
      
        // Initialize all distances to INF and visited to false.
        for (int i = 0; i < n; ++i) {
            fill(graph[i], graph[i] + n, INF);
            distance[i] = INF;
            visited[i] = false;
        }
        distance[src] = 0; // Distance to source is 0.

        // Initialize graph with edges that have non-negative weight.
        for (const auto& edge : edges) {
            int from = edge[0], to = edge[1], weight = edge[2];
            if (weight == -1) {
                continue;
            }
            graph[from][to] = weight;
            graph[to][from] = weight;
        }

        // Applying Dijkstra's algorithm.
        for (int i = 0; i < n; ++i) {
            int closestUnvisitedNode = -1;
            for (int j = 0; j < n; ++j) {
                if (!visited[j] && (closestUnvisitedNode == -1 || distance[j] < distance[closestUnvisitedNode])) {
                    closestUnvisitedNode = j;
                }
            }
            visited[closestUnvisitedNode] = true;
            for (int j = 0; j < n; ++j) {
                distance[j] = min(distance[j], distance[closestUnvisitedNode] + graph[closestUnvisitedNode][j]);
            }
        }

        // Return the shortest distance to the destination.
        return distance[dest];
    }
};
