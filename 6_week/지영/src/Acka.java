import java.util.Arrays;
import java.util.Scanner;

public class Acka {

    static Long[][][][] cache;
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int songs = sc.nextInt();
        int dotorya = sc.nextInt();
        int kesakiyo = sc.nextInt();
        int hongjun = sc.nextInt();
        
        cache = new Long[songs+1][songs+1][songs+1][songs+1];
        for (int i = 0; i < songs +1; i++){
            for (int j = 0; j < songs +1; j++){
                for(int z = 0; z < songs+1; z++){
                    Arrays.fill(cache[i][j][z], -1L);
                }
            }
        }
        Long cases = dynamic(songs, dotorya, kesakiyo, hongjun);
        System.out.println(cases);

    }

    public static Long dynamic(int songs, int d, int k, int h){
        if (songs == 0){
            if (d == 0 && k == 0 && h == 0){
                return 1L;
            }
            else {
                return 0L;
            }
        }
        if ( d < 0 || k < 0 || h < 0){
            return 0L;
        }
        if (cache[songs][d][k][h] != -1){
            return cache[songs][d][k][h];
        } 
        Long ret = 0L;

        ret += dynamic(songs-1, d-1, k, h);
        ret += dynamic(songs-1, d, k-1, h);
        ret += dynamic(songs-1, d, k, h-1);
        ret += dynamic(songs-1, d-1, k-1, h);
        ret += dynamic(songs-1, d-1, k, h-1);
        ret += dynamic(songs-1, d, k-1, h-1);
        ret += dynamic(songs-1, d-1, k-1, h-1);

        ret %= 1000000007;
        cache[songs][d][k][h] = ret;
        return cache[songs][d][k][h];

    }
}
