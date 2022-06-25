import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        final int TREES = Integer.parseInt(br.readLine());
        List<Integer> growDays = Arrays.stream(br.readLine().split(" ")) // 공백으로 나누어 String 배열을 만들고
            .map(Integer::valueOf) // 각 String을 Integer로 변환하여
            .collect(Collectors.toList()); // List<Integer>로 최종 변환

        sortByPlantOrder(growDays);
        
        int theDayAllGrown = 0;
        for (int i = 0; i < TREES; i++) {
            int today = i + 2;
            int theDayGrown = today + growDays.get(i);

            theDayAllGrown = Math.max(theDayGrown, theDayAllGrown);
        }

        System.out.print(theDayAllGrown);

        br.close();
    }

    public static void sortByPlantOrder(List<Integer> growDays) {
        Collections.sort(growDays);
        Collections.reverse(growDays);
    }
}

////굳굳