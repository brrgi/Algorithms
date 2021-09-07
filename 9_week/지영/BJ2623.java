import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

class Graph {
    private Boolean[][] maps;
    private int[] in;
    private int size;

    public Graph(int size) {
        maps = new Boolean[size][size];
        in = new int[size];
        this.size = size;
    }

    public void input(int v1,  int v2) {
        // 단방향 그래프
        if (!maps[v1][v2]) {
            maps[v1][v2] = true;
            in[v2] += 1;
        }

    }

    public List<Integer> getStartIdx() {
        /**
         * 진입차수가 0인 노드를 반환합니다.
         */

        List<Integer> ret = new ArrayList<>();

        for (int i = 1; i < size; i++) {
            if (in[i] == 0) {
                ret.add(i);
            }
        }

        return ret;
    }

    public List<Integer> removeOut(int node) {
        /**
         * node에 연결된 간선을 제거합니다.
         * 연결이 제거된 노드 중, 진입차수가 0인 노드 리스트를 반환힙니다.
         */

        List<Integer> ret = new ArrayList<>();

        for (int i = 1; i < size; i++) {
            if (maps[node][i]) {
                in[i] -= 1;
                if (in[i] == 0) {
                    ret.add(i);
                }
            }
        }

        return ret;
    }

    public void setRow(int v1, Boolean val) {
        Arrays.fill(maps[v1], val);
    }

}
public class BJ2623 {
    public static void main(String[] args) throws IOException {
        Queue<Integer> queue = new LinkedList<Integer>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] ans;
        StringTokenizer st;
        Graph graph;
        // List<Integer> ans = new ArrayList<>();


        // 가수의 수, 보조 PD
        st = new StringTokenizer(br.readLine());
            
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        graph = new Graph(N+1);
        ans = new int[N+1];

        for (int i = 1; i < N+1; i++) {
            graph.setRow(i, false);
        }

        for (int i = 0; i < M; i++ ) {
            st = new StringTokenizer(br.readLine());

            int end;
            int num = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());

            for (int j = 0; j < num - 1; j++ ) {
                end = Integer.parseInt(st.nextToken());
                graph.input(start, end);
                start = end;
            }
        }


        // 시작 큐 초기화
        List<Integer> startIdx = graph.getStartIdx();
        for (int idx: startIdx) {
            queue.offer(idx);
        }

        // 전체 노드 수만큼 정렬된 노드 추출
        for (int i = 1; i < N+1; i++) {

            // 만약 중간에 queue가 빈 경우, 노드가 사이클이 발생한 경우임으로 return
            if(queue.isEmpty()){
                System.out.println(0);
                return;
            }

            int node = queue.poll();
            ans[i] = node;

            startIdx = graph.removeOut(node);

            for (int idx: startIdx) {
                queue.offer(idx);
            }


        }
        for (int i = 1; i < N+1; i ++) {
            System.out.printf("%d ",ans[i]);
        }
        
    }
    
}
