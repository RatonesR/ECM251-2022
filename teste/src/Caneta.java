public class Caneta{
    String modelo;
    String cor;
    double ponta;
    int carga;
    final int CARGA_MAXIMA = 100;

    void escrever(String texto){
        for (int i = 0; i < texto.length(); i++){
            if(carga > 0){
                System.out.print(texto.charAt(i));
                carga -= 1;
            } else{
                System.out.println("CANETA SEM CARGA!");
            }
        }
    }

    void iniciarCaneta(String modelo, String cor, double ponta){
        this.modelo = modelo;
        this.cor = cor;
        this.ponta = ponta;
        this.carga = CARGA_MAXIMA;
    }

    String pegarDados(){
        return "Modelo:" + modelo +
        "- Cor:" + cor +
        "- Ponta:" + ponta +
        "- Carga:" + carga;
    }
}