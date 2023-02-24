/**
 * main
 */

public class Main {
    public static void main(String[] args) {
        final int delay = 1; // mill second
        int[] world_size = {30,10};
        final int generation = 1000;    // generation世代までシュミュレーションすることができる

        LifeGame lg = new LifeGame(world_size);
        lg.createGrider(5, 5);
        // System.out.println("\u001b[2J");
        System.out.print("\u001b[2J");
        for (int i = 0; i < generation; i++) {
            // CLI画面を更新するために、ANSI文字コードで全画面削除
            System.out.println(String.format("\u001b[%sA",world_size[1]+1));
            // 
            lg.printWorld();
            lg.update();
            try {
                Thread.sleep(delay);
            } catch (InterruptedException e) {
            }
        }
    }
}
