public class Usuario {
    private String nome;
    private int id;
    private double saldo;

    public Usuario(String nome, double saldo) {
        this.nome = nome;
        this.saldo = saldo;
    }

    public String getNome() {
        return nome;
    }

    public double getSaldo() {
        return saldo;
    }

    public static void aluguel(int id){

        public boolean alugar(double custoHr){
            this.saldo -= custoHr;
            return true;
        }
        public boolean receberAluguel(double custoHr){
            this.saldo += custoHr;
            return true;
        }
        public boolean trocar(double custoHr){
            troca.testar();
        }
    }

    @Override
    public String toString() {
        return "Usuario [nome=" + nome + ", saldo=" + saldo + "]";
    }

}
