
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ2016 {
    static int N;
    static int M;
    static int[] customers;
    static int[] sum;
    static int[][] store;
    
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        customers =  new int[N+1];
        sum = new int[N+1];
        store = new int[N+1][4];
        
        st = new StringTokenizer(br.readLine());

        for(int i = 1; i <= N; i ++) {
            customers[i] = Integer.parseInt(st.nextToken());
            sum[i] = sum[i-1] + customers[i];
        }

        M = Integer.parseInt(br.readLine());

        for (int idx = 1; idx < 4; idx++ ) {

            for (int idx1 = idx*M; idx1 <= N; idx1++) {
                
                if (idx == 1) store[idx1][idx] = Math.max(store[idx1-1][idx], sum[idx1] - sum[idx1-M]);

                else store[idx1][idx] = Math.max(store[idx1-1][idx], store[idx1-M][idx-1] + sum[idx1] - sum[idx1-M]);
                
                
            }
        }


        System.out.println(store[N][3]);

        
    }    
}
