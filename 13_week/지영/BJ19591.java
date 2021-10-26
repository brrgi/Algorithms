import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BJ19591 {
    static Deque<Character> operations;
    static Deque<Long> numbers;  
    static Long answer;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // HashSet<Character> opSet = new HashSet<>(Arrays.asList('+', '*', '-', '/'));
        HashMap<Character, Integer> opPriority = new HashMap<Character, Integer>() {{
            put('*', 1); put('/', 1); put('+', 0); put('-', 0);
        }};
        
        operations = new ArrayDeque<>();
        numbers = new ArrayDeque<>();  
        
        st = new StringTokenizer(br.readLine(), "-+*/", true);
        while (st.hasMoreTokens()) {
            String cur = st.nextToken();
            if (numbers.isEmpty() && opPriority.keySet().contains(cur.charAt(0))){
                numbers.add(Long.parseLong(""+cur+st.nextToken()));
                continue;
            }

            if (opPriority.keySet().contains(cur.charAt(0))) operations.add(cur.charAt(0));
            else numbers.add(Long.parseLong(String.valueOf(cur)));

        }

        answer = 0L;
        if (operations.isEmpty()){
            answer = numbers.pollFirst();
        }
        while (!operations.isEmpty()) { 

            if (operations.size() == 1) {
                answer = calculate(numbers.pollFirst(), numbers.pollFirst(), operations.pollFirst());
                break;
            }

            char op1 = operations.getFirst(); 
            char op2 = operations.getLast(); 

            // 연산자 비교
            int firstOp = opPriority.get(op1);
            int lastOp = opPriority.get(op2);

            if (firstOp > lastOp) {
                long calculated = calculate(numbers.pollFirst(), numbers.pollFirst(), operations.pollFirst());
                numbers.addFirst(calculated);
                continue;
            }
            if (firstOp < lastOp) {
                long last = numbers.pollLast();
                // *** 순서 유의
                long calculated = calculate(numbers.pollLast(), last, operations.pollLast());
                numbers.addLast(calculated);
                continue;

            }
            // 값의 대소관계 비교
            long first = numbers.pollFirst();
            long second = numbers.getFirst();

            long secondFromBack = numbers.pollLast();
            long firstFromBack = numbers.getLast();

            long comp1 = calculate(first, second, op1);
            long comp2 = calculate(firstFromBack, secondFromBack, op2);
            
            if (comp1 > comp2 || comp1 == comp2) select_first(secondFromBack, comp1);
            else select_last(first, comp2);

        }

        System.out.println(answer);

    }

    public static long calculate(long prev, long next, char op) {
        if (op == '+') return prev + next;
        if (op == '-') return prev - next;
        if (op == '*') return prev * next;
        return prev / next;

    }

    static void select_first(long lastNum, long res) { 
        numbers.removeFirst();//맨 앞 숫자 
        operations.removeFirst();//맨 앞 연산자 
        numbers.addFirst(res); 
        numbers.addLast(lastNum);//맨 뒤 숫자 
    } 
    static void select_last(long preNum, long res) { 
        numbers.removeLast();//맨 뒤 숫자 
        operations.removeLast();//맨 뒤 연산자 
        numbers.addFirst(preNum);//맨 앞 숫자 
        numbers.addLast(res); 
    } 
}
