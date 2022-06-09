import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws Exception {
        List<Membro> Membros = new ArrayList<Membro>();
        Membros.add(new HeavyLifters(0, "Lu1z", new Membro()));
        Membros.add(new ScryptGuys(0, "4manda", new Membro()));
        Membros.add(new MobileMembers(0, "3nzo", new Membro()));
        
        PostarMensagem(List<Membro>);

        Membros.remove[0];
        Membros.remove[1];
        Membros.remove[2];

        Membros.add(new HeavyLifters(1, "Lu1z", new Membro()));
        Membros.add(new ScryptGuys(1, "4manda", new Membro()));
        Membros.add(new MobileMembers(1, "3nzo", new Membro()));

        PostarMensagem(List<Membro>);
        
        Membros.remove[0];
        Membros.remove[1];

        PostarMensagem(List<Membro>);

    }
}
