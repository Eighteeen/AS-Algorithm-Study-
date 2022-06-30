import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    final static int DWARFS = 9;
    static int sumOfHeights;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        List<Integer> heights = new ArrayList<>();

        for (int i = 0; i < DWARFS; i++) {
            int height = Integer.parseInt(br.readLine());
            heights.add(height);
            sumOfHeights += height;
        }

        exceptFakeDwarfHeights(heights);
        Collections.sort(heights);

        StringBuilder result = new StringBuilder();
        for (int height : heights) {
            result.append(height).append('\n');
        }
        System.out.print(result);

        br.close();
    }

    public static void exceptFakeDwarfHeights(List<Integer> heights) {
        for (int i = 0; i < DWARFS - 1; i++) {
            for (int j = i + 1; j < DWARFS; j++) {
                int height1 = heights.get(i);
                int height2 = heights.get(j);

                boolean isFake = (sumOfHeights - height1 - height2) == 100;
                if (isFake) {
                    heights.remove(i);
                    heights.remove(j - 1);
                    return;
                }
            }
        }
    }
}
