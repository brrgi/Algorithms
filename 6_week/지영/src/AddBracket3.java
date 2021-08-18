package Week6.src;
import java.util.Arrays;
import java.util.Scanner;


public class AddBracket3 {
    static int[][][] store;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        char[] expression = sc.next().toCharArray();
        store = new int[N][N][2];
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                store[i][j][0] = Integer.MIN_VALUE;
                store[i][j][1] = Integer.MAX_VALUE;
            }
        }
        for(int i = 0; i < N; i++) {
            if(Character.isDigit(expression[i])) {
                store[i][i][0] = expression[i] - '0';
                store[i][i][1] = expression[i] - '0';
            }
        }
        for(int j = 2; j < N; j+=2) {
            for(int i = 0; i < N - j; i+=2) {
                for(int k = 2; k <= j; k+=2) {
                    int[] num = new int[4];
                    int op = i + k - 1;
                    num[0] = calculate(store[i][i + k - 2][0], store[i + k][i + j][0], expression[op]);
                    num[1] = calculate(store[i][i + k - 2][0], store[i + k][i + j][1], expression[op]);
                    num[2] = calculate(store[i][i + k - 2][1], store[i + k][i + j][0], expression[op]);
                    num[3] = calculate(store[i][i + k - 2][1], store[i + k][i + j][1], expression[op]);

                    Arrays.sort(num);
                    store[i][i + j][0] = Math.max(store[i][i + j][0], num[3]);
                    store[i][i + j][1] = Math.min(store[i][i + j][1], num[0]);
                }
            }
        }
        System.out.println(store[0][N - 1][0]);
    }

    public static int calculate(int prev, int next, char operator) {
        switch(operator){
        case '*':
            return prev * next;
        case '+':
            return prev + next; 
        case '-':
            return prev - next;
        }
        return 0;
    }
}
