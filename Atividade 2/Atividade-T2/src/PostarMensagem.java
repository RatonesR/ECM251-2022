public class PostarMensagem {
    public String nome;
    public boolean atividade;
    public Membro membro;

    public String getNome() {
        return nome;
    }
    public boolean isAtividade() {
        return atividade;
    }
    public Membro getMembro() {
        return membro;
    }

    @Override
    public String toString() {
        return "PostarMensagem [atividade=" + atividade + ", membro=" + membro + ", nome=" + nome + "]";
    }


}
