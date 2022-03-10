public class App {
    public static void main(String[] args) throws Exception {
        //Declara um objeto Caneta e instancia ele
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("BIC", "Azul", 1.0);
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Stabillo", "Vermelha", 0.4);
        System.out.println("Minha caneta C1:" + c1.pegarDados());
        System.out.println("Minha Caneta C2:" + c2.pegarDados());
        c1.escrever("O hashira do Som é um cara diferenciado, mas não é o melhor hashira. Contudo, ninguém nega que o Musan, parece o Michel Jackson rsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrs é o Musan");
        c2.escrever("Qual é o melhor hashira?");
        System.out.println("Minha caneta C1:" + c1.pegarDados());
        System.out.println("Minha Caneta C2:" + c2.pegarDados());
    }
}