public class RolaDados {

    private Dado[] dados;
    private int qtdDados;
    private int[] valores;

    public RolaDados(int n) {

        dados = new Dado[n];
        qtdDados = n;
        valores = new int[n];
        
        for (int i = 0; i < n; i++) {
            dados[i] = new Dado();
        }

    }

    public int[] rolar() {

        for (int i = 0; i < qtdDados; i++) {
            valores[i] = dados[i].rolar();
        }
        
        return valores;
    }
    
    public int[] rolar(boolean[] quais) {
        
        for (int i = 0; i < qtdDados; i++) {
            if (quais[i]) 
                valores[i] = dados[i].rolar();
        }

        return valores;
    }

    public int[] rolar(String s) {

        if (s.length() == 0)
            return valores;

        boolean quais[] = new boolean[qtdDados];

        for (int i = 0; i < s.length() && i < qtdDados * 2; i += 2) {
            int posicao = Integer.parseInt(s.substring(i, i + 1));
            quais[posicao - 1] = true;
        }

        rolar(quais);
        return valores;
    }

    public int[] getValores() {
        return valores;
    }

    @Override
    public String toString() {

        // cria uma string com os indices dos dados
        String indices = new String();
        for (int i = 0; i < qtdDados; i++)
            indices += (i + 1) + "\t";
        indices += "\n";
        
        // separa as linhas de cada dado em substrings
        String aux[][] = new String[qtdDados][];
        for (int i = 0; i < qtdDados; i++)
            aux[i] = dados[i].toString().split("\n");
    
        // concatena na ordem correta as substrings obtidas em uma nova string
        String str = new String();
        for (int i = 0; i < aux.length; i++) {
            for (int j = 0; j < qtdDados; j++) 
                str += aux[j][i] + " ";
            str += "\n";
        }
    
        return indices + str;
    }
}
