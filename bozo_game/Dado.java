public class Dado {

    private int qtdLados = 0;
    private int ultimoValor = 0;
    static Random sorteio = new Random();

    public Dado() {
        qtdLados = 6;
    }
    
    public Dado(int n) {
        qtdLados = n;
    }
    
    public int rolar() { 
        // Random r = new Random();
        int valorSorteado = sorteio.getIntRand(qtdLados) + 1;
        ultimoValor = valorSorteado;
        return valorSorteado;
    }

    public int getLado() {
        return ultimoValor;
    }

    @Override
    public String toString() {

        String str = new String();

        if (qtdLados != 6) {
            System.out.println("Dado precisa ser de 6 lados");
            return str;
        }

        if (ultimoValor == 1)
            str = "+-----+\n|     |\n|  *  |\n|     |\n+-----+"; 
        if (ultimoValor == 2)
            str = "+-----+\n|*    |\n|     |\n|    *|\n+-----+"; 
        if (ultimoValor == 3)
            str = "+-----+\n|*    |\n|  *  |\n|    *|\n+-----+"; 
        if (ultimoValor == 4)
            str = "+-----+\n|*   *|\n|     |\n|*   *|\n+-----+"; 
        if (ultimoValor == 5)
            str = "+-----+\n|*   *|\n|  *  |\n|*   *|\n+-----+"; 
        if (ultimoValor == 6)
            str = "+-----+\n|*   *|\n|*   *|\n|*   *|\n+-----+"; 

        return str;
    }
}
