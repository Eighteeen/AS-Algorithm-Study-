import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final String input = br.readLine();
        
        StringTokenizer st = new StringTokenizer(input, " ");
        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());

        int cutIntoNPieces = N - 1;
        int cutMPiecesForEachPiece = (M - 1) * N;

        System.out.print(cutIntoNPieces + cutMPiecesForEachPiece);

        br.close();
    }
}