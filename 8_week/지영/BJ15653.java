
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;
 

public class BJ15653 {
    static final char BLOCK = '#';
    static final char ENDPOINT = 'O';
    static final char RED = 'R';
    static final char BLUE = 'B';
    
    static class Pair {
        int rr;
        int rc;
        int br;
        int bc;
        int cnt;
 
        public Pair(int rr, int rc, int br, int bc, int cnt) {
            this.rr = rr;
            this.rc = rc;
            this.br = br;
            this.bc = bc;
            this.cnt = cnt;
        }
    }
 
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static Deque<Pair> queue = new ArrayDeque<>();
    static boolean visit[][][][] = new boolean[11][11][11][11];
    static char maps[][] = new char[11][11];
    static int direct[][] = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
    static int N, M;
 
    static void bfs() {
        while (!queue.isEmpty()) {
            int rr = queue.peek().rr;
            int rc = queue.peek().rc;
            int br = queue.peek().br;
            int bc = queue.peek().bc;
            int cnt = queue.poll().cnt;
 
            for (int i = 0; i < 4; i++) {
                // 빨간 구슬 현 위치
                Boolean redFlag = false;
                Boolean blueFlag = false;
                
                int nextRedRow = rr;
                int nextRedCol = rc;
                while(true) {
                // for (int offset = 1; offset < Math.max(N, M); offset ++) {
                    nextRedRow += direct[i][0];
                    nextRedCol += direct[i][1];

                    if (maps[nextRedRow][nextRedCol] == BLOCK) {
                        nextRedRow -= direct[i][0];
                        nextRedCol -= direct[i][1];
                        break;
                    }

                    if (maps[nextRedRow][nextRedCol] == ENDPOINT) {
                        redFlag = true;
                        break;
                    }

                }
 
                int nextBlueRow = br;
                int nextBlueCol = bc;

                while(true) {
                // for (int offset = 1; offset < Math.max(N, M); offset ++) {
                    nextBlueRow += direct[i][0];
                    nextBlueCol += direct[i][1];

                    if (maps[nextBlueRow][nextBlueCol] == BLOCK) {
                        nextBlueRow -= direct[i][0];
                        nextBlueCol -= direct[i][1];
                        break;
                    }

                    if (maps[nextBlueRow][nextBlueCol] == ENDPOINT) {
                        blueFlag = true;
                        break;
                    }

                }
 
                if (blueFlag) continue;
                else if (redFlag) {
                    System.out.println(cnt + 1);
                    return;
                }
                //  다 같이 움직여 놓고 같은 row, col의 경우 어떤 구슬이 앞에 있는가에 따라 값을 교체한다.
                if (nextRedRow == nextBlueRow && nextRedCol == nextBlueCol) {
                    int redDist = Math.abs(nextRedRow - rr) + Math.abs(nextRedCol - rc);
                    int blueDist = Math.abs(nextBlueRow - br) + Math.abs(nextBlueCol - bc);

                    // blue 구슬이 먼저 도착한 상황
                    if (redDist > blueDist) {
                        nextRedRow -= direct[i][0];
                        nextRedCol -= direct[i][1];
                    }else {
                        nextBlueRow -= direct[i][0];
                        nextBlueCol -= direct[i][1];
                    }

                }
 
                if (visit[nextRedRow][nextRedCol][nextBlueRow][nextBlueCol]) continue;
 
                queue.add(new Pair(nextRedRow, nextRedCol, nextBlueRow, nextBlueCol, cnt + 1));
                visit[nextRedRow][nextRedCol][nextBlueRow][nextBlueCol] = true;
            }
        }
 
        System.out.println(-1);
    }
    public static void main(String[] args) throws Exception {
        int redRow = 0, redCol = 0, blueRow = 0, blueCol = 0;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            maps[i] = st.nextToken().toCharArray();
            for (int j = 0; j < M; j++) {
                if (maps[i][j] == RED) {
                    redRow = i;
                    redCol = j;
                } else if (maps[i][j] == BLUE) {
                    blueRow = i;
                    blueCol = j;
                }
            }
        }
 
        queue.add(new Pair(redRow, redCol, blueRow, blueCol, 0));
        visit[redRow][redCol][blueRow][blueCol] = true;
        bfs();
    }
    
}
