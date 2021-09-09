import java.io.IOException;
import java.util.Arrays;

class Graph {
    private long[][] maps;
    private int size;

    public Graph(int size) {
        maps = new long[size][size];
        this.size = size;
    }

    public void input(int v1,  int v2, int dist) {
        maps[v1][v2] = dist;
        maps[v2][v1] = dist;
    }

    public void setRow(int v1, int val) {
        Arrays.fill(maps[v1], val);
    }

    public void dijkstra(int node) {

        Boolean[] visited = new Boolean[size];
        Arrays.fill(visited, false);

        for (int i = 0; i < size - 1; i++)
        {        
            // 거리가 최소인 노드 고르기
            int start = 1;
            long dist = Integer.MAX_VALUE;
            for(int idx = 1; idx < size; idx++) {
                if (maps[node][idx] < dist && !visited[idx]) {
                    start = idx;
                    dist = maps[node][idx];
                }
            }
            visited[start] = true;

            for(int idx = 1; idx < size; idx++) {
                if (visited[idx] || idx == node) continue;
                maps[node][idx] = Math.min(maps[node][idx], maps[start][idx] + dist);
            }
        }

    }

    public long getCost(int v1, int v2) {
        return maps[v1][v2];
    }
}

public class Problem04 {

    public static void main(String[] args) throws IOException {
        int[][] fares = {{4, 1, 10}, {3, 5, 24},{5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}};
        int ret = solution(6, 4, 6, 2, fares);

        System.out.println(ret);

        
    }

    static public int solution(int n, int s, int a, int b, int[][] fares) {
        long answer = Integer.MAX_VALUE;
        Graph graph = new Graph(n+1);

        for (int idx = 1; idx < n + 1; idx++) {
            graph.setRow(idx, Integer.MAX_VALUE);
            // minGraph.setRow(idx, Integer.MAX_VALUE);
            graph.input(idx, idx, 0);
        }

        for(int i =0; i < fares.length; i++ ){
            graph.input(fares[i][0], fares[i][1], fares[i][2]);
        }

        // 모든 노드에 대해 dijkstra 해당 노드에서 다른 노드로 가는 최소값

        for (int i =1; i < n+1; i++){
            graph.dijkstra(i);

        }

        for(int i =1; i< n+1; i++) {
            long one = graph.getCost(i, a);
            long theOther = graph.getCost(i, b);

            long common = graph.getCost(s, i);

            answer = Math.min(answer, one+theOther+common);
        }
        



        return (int)answer;
    }

}
