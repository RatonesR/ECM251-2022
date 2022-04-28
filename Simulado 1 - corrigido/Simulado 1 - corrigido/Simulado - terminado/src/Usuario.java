public class Usuario {
    private String nome;
    private String senha;
    private String email;
    private Conta conta;

//CNTRL + .
//Generate constructors...
//(nome, senha, email)

    public Usuario(String nome, String senha, String email) {
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        this.conta = new Conta();
    }

//CNTRL + .
//Generate getters and setters...
//(conta, nome)

    public String getNome() {
        return nome;
    }
    public Conta getConta() {
        return conta;
    }

//CNTRL + .
//Generate toString()...
//(conta, email, nome, senha)

    @Override
    public String toString() {
        return "Usuario [conta=" + conta + ", email=" + email + ", nome=" + nome + ", senha=" + senha + "]";
    }
}
