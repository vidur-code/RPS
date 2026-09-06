import java.util.Random;
import java.util.Scanner;
public class RPSV1 {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        Random r = new Random();
        String x = "tung";
        System.out.println("This a rock paper sccisors game");
        while (!x.equals("n")){
            System.out.println("Rock, Paper or Scissors= ");
            String a = s.nextLine();
            a = a.toLowerCase();
            if (a.equals("rock")){
                Integer[] arr = {2,3};
                Integer c1= arr[r.nextInt(arr.length)];
                if(c1==2){
                    System.out.println("I picked Paper and Paper beats Rock!");
                }else{
                    System.out.println("I picked Scissors, and Scisors loses to Rock!");
                }
            }else if(a.equals("paper")){
                Integer[] arr = {1,3};
                Integer c1=arr[r.nextInt(arr.length)];
                if(c1==1){
                    System.out.println("I picked Rock, and Rock loses to Paper!");
                }else{
                    System.out.println("I picked Scissors, and Scissors beats Paper");
                }
            }else{
                Integer[] arr = {1,2};
                Integer c1 = arr[r.nextInt(arr.length)];
                if(c1==1){
                    System.out.println("I picked Rock, and Rock beats Scissors!");
                }else{
                    System.out.println("I picked Paper, and Paper loses to Scissors!");
                }
            }
            System.out.println("Would you like to play again?(Y/n)= ");
            x = s.nextLine().toLowerCase();
        }
    System.out.println("Ok, thanks for playing!!!");
    s.close();
    } 
}