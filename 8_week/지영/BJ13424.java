
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

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

    public long[] dijkstra(int node) {

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
        return maps[node];

    }
}

public class BJ13424 {

    static int testcase;
    static int[] minVal;
    static int vertex, edges;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Graph graph;
        int member_cnt;

        testcase = Integer.parseInt(br.readLine());

        for (int cnt = 0; cnt < testcase; cnt++) {

            st = new StringTokenizer(br.readLine());
            
            vertex = Integer.parseInt(st.nextToken());
            edges = Integer.parseInt(st.nextToken());

            graph = new Graph(vertex+1);
            minVal = new int[vertex+1];

            for (int idx = 1; idx < vertex + 1; idx++) {
                graph.setRow(idx, Integer.MAX_VALUE);
                graph.input(idx, idx, 0);
                minVal[idx] = 0; 
            }

            for (int idx = 0; idx < edges; idx++) {
                st = new StringTokenizer(br.readLine());
                
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                int dist = Integer.parseInt(st.nextToken());

                graph.input(start, end, dist);
                
            }

            member_cnt = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int member = 0; member < member_cnt; member++) {
                long[] values = graph.dijkstra(Integer.parseInt(st.nextToken()));

                for (int i = 1; i < vertex +1 ; i++) {
                    minVal[i] += values[i];
                }
            }

            int retNode = 1;
            int ret = Integer.MAX_VALUE;
            for (int i = 1; i < vertex +1; i++) {
                if (ret > minVal[i]) {
                    ret = minVal[i];
                    retNode = i;
                }
            }
            System.out.println(retNode);
         

        }
        
    }

}
