import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.BufferedInputStream;
import java.util.PriorityQueue;
import java.util.AbstractCollection;
import java.io.FilterInputStream;
import java.util.Collections;
import java.io.InputStream; 

public class Main {
  public static void main(String[] args) {
    new Thread(null, new Runnable() {
      public void run() {
        new Main().solve();
      }
    }, "1", 1 << 26).start();
  }
  void solve() {
    InputStream inputStream = System.in;
    OutputStream outputStream = System.out;
    ScanReader in = new ScanReader(inputStream);
    PrintWriter out = new PrintWriter(outputStream);
    Plindromicgrid solver = new Plindromicgrid();
    int testCount = in.scanInt();
    for (int i = 1; i <= testCount; i++) solver.solve(i, in, out);
    out.close();
  }
  static class Plindromicgrid {
    int[] freq;
    private int findIndex(int required) {
      int max = -1;
      int index = -1;
      for (int i = 0; i < 26; i++) {
        if (freq[i] >= max) {
          max = freq[i];
          index = i;
        }
      }
      if (max < required) return -1;
      return index;
    }
    public void solve(int testNumber, ScanReader in , PrintWriter out) {
      int n = in.scanInt();
      int m = in.scanInt();
      freq = new int[26];
      for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) freq[(int) in.scanChar() - 97]++;
      boolean ans = true;
      boolean[][] visited = new boolean[n][m];
      PriorityQueue < Integer > priorityQueue = new PriorityQueue < > (Collections.reverseOrder());
      out: for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          if (visited[i][j]) continue;
          int required = 4;
          if (i == n - i - 1) required -= 2;
          if (j == m - j - 1) required -= 2;
          required = Math.max(required, 1);
          priorityQueue.add(required);
          visited[i][j] = true;
          visited[n - i - 1][j] = true;
          visited[i][m - j - 1] = true;
          visited[n - i - 1][m - j - 1] = true;
        }
      }
      while (!priorityQueue.isEmpty()) {
        int required = priorityQueue.poll();
        int index = findIndex(required);
        if (index == -1) ans = false;
        else freq[index] -= required;
      }
      if (ans) out.println("YES");
      else out.println("NO");
    }
  }
  static class ScanReader {
    private byte[] buf = new byte[4 * 1024];
    private int index;
    private BufferedInputStream in ;
    private int total;
    public ScanReader(InputStream inputStream) {
      in = new BufferedInputStream(inputStream);
    }
    private int scan() {
      if (index >= total) {
        index = 0;
        try {
          total = in.read(buf);
        } catch (Exception e) {
          e.printStackTrace();
        }
        if (total <= 0) return -1;
      }
      return buf[index++];
    }
    public char scanChar() {
      int c = scan();
      while (isWhiteSpace(c)) c = scan();
      return (char) c;
    }
    public int scanInt() {
      int integer = 0;
      int n = scan();
      while (isWhiteSpace(n)) n = scan();
      int neg = 1;
      if (n == '-') {
        neg = -1;
        n = scan();
      }
      while (!isWhiteSpace(n)) {
        if (n >= '0' && n <= '9') {
          integer *= 10;
          integer += n - '0';
          n = scan();
        }
      }
      return neg * integer;
    }
    public String next() {
      int c = scan();
      if (c == -1) return null;
      while (isWhiteSpace(c)) c = scan();
      StringBuilder res = new StringBuilder();
      do {
        res.appendCodePoint(c);
        c = scan();
      } while (c != '\n' && c != -1);
      return res.toString();
    }
    private boolean isWhiteSpace(int n) {
      if (n == ' ' || n == '\n' || n == '\r' || n == '\t' || n == -1) return true;
      else return false;
    }
  }
}