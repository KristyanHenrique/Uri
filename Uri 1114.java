import java.io.IOException;
import java.util.Scanner;
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class Main {
 
    public static void main(String[] args) throws IOException {
 
        Scanner scan = new Scanner(System.in);
        int a = 0;
        while (a != 2002) {
            a = scan.nextInt();
            if (a == 2002) {
                System.out.printf("Acesso Permitido\n");
            } else {
                System.out.printf("Senha Invalida\n");
            }
        }
    }
 
}
