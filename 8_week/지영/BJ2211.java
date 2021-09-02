package Week8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


class Graph2 {
    private long[][] maps;
    private int size;

    public Graph2(int size) {
        maps = new long[size][size];
        this.size = size;
    }

    public void input(int v1,  int v2, int dist) {
        if (maps[v1][v2] != Integer.MAX_VALUE) 
        {
            maps[v1][v2] = dist;
            return;
        }
        maps[v1][v2] = dist;
        maps[v2][v1] = dist;
    }

    public void setRow(int v1, int val) {
        Arrays.fill(maps[v1], val);
    }

    public void dijkstra(int node) {

        int[][] ret = new int [size][2];
        int total = 0;

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
                if (maps[node][idx] > maps[start][idx] + dist) {
                    maps[node][idx] = maps[start][idx] + dist;
                    ret[idx][0] = start;
                    ret[idx][1] = idx;
                } 
            }
        }
        for (int cnt = 1; cnt < size; cnt ++) {
            if(cnt == node) continue;
            if (ret[cnt][0] == 0 && ret[cnt][1] == 0) {
                ret[cnt][0] = node;
                ret[cnt][1] = cnt;
            }
            total++;
        }

        System.out.println(total);
        for (int idx = 2; idx < size; idx++) {
            if(idx == node) continue;
            System.out.printf("%d %d\n", ret[idx][0], ret[idx][1]);
        }


    }
}

public class BJ2211 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Graph2 graph;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        graph = new Graph2(N+1);

        for (int idx = 1; idx < N + 1; idx++) {
            graph.setRow(idx, Integer.MAX_VALUE);
            graph.input(idx, idx, 0);
        }

        for (int idx = 0; idx < M; idx++) {
            st = new StringTokenizer(br.readLine());
            
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph.input(v1, v2, dist);
            
        }

        graph.dijkstra(1);
   
    }
    
}
