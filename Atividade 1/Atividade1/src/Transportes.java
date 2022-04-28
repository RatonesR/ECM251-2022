import java.util.concurrent.ThreadLocalRandom;

public class Transportes {
    protected Double custoHr;
    protected int id;

    public static int gerarId(String usuario, double custoHr){
        int numeroAleatorio = ThreadLocalRandom.current().nextInt(10000, 100000);
        return String.format("%s;%.2f;%d", 
        usuario,
        custoHr, 
        numeroAleatorio);
    }
}