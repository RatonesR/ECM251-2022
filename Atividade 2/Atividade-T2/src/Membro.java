public class Membro {
    public String nome;
    public boolean atividade;
    public Membro membro;

    public Membro(String nome, boolean atividade){
        this.nome = nome;
        this.atividade = atividade;
    }

    public String getNome() {
        return nome;
    }
    public boolean Atividade() {
        return atividade;
    }

    @Override
    public String toString() {
        return "Membro [atividade=" + atividade + ", nome=" + nome + "]";
    }


}
