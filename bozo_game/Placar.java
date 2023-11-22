public class Placar {

    private int[] placar;
    private int tamanhoPlacar = 10;

    public Placar() {

        placar = new int[tamanhoPlacar];

        for (int i = 0; i < tamanhoPlacar; i++) 
            placar[i] = -1;

    }

    private int calculaFrequencia(int[] dados, int valor) {
        
        int frequencia = 0;

        for (int i = 0; i < dados.length; i++) {
            if (dados[i] == valor)
                frequencia++;
        }

        return frequencia;
    }
    
    public void add(int posicao, int[] dados) throws IllegalArgumentException {

        if (placar[posicao] != -1 || posicao < 0 || posicao > tamanhoPlacar)
            throw new IllegalArgumentException();

        boolean valorDuplo = false;
        boolean valorTriplo = false;
        boolean valorQuadruplo = false;
        boolean valorQuintuplo = false;
        switch (posicao) {

            case 0:
                placar[0] = calculaFrequencia(dados, 1);
                break;
                
            case 1:
                placar[1] = calculaFrequencia(dados, 2) * 2;
                break;
                
            case 2:
                placar[2] = calculaFrequencia(dados, 3) * 3;
                break;
                
            case 3:
                placar[3] = calculaFrequencia(dados, 4) * 4;
                break;
                
            case 4:
                placar[4] = calculaFrequencia(dados, 5) * 5;
                break;
                
            case 5:
                placar[5] = calculaFrequencia(dados, 6) * 6;
                break;
            
            case 6: // full hand
                // verifica se algum valor apareceu 3 vezes
                for (int i = 1; i <= 6; i++) {
                    if (calculaFrequencia(dados, i) == 3)
                        valorTriplo = true;
                }
                // verifica se algum valor apareceu 2 vezes
                for (int i = 1; i <= 6; i++) {
                    if (calculaFrequencia(dados, i) == 2)
                        valorDuplo = true;
                }
                // verifica se o full hand foi bem sucedido
                if (valorTriplo  && valorDuplo)
                    placar[6] = 15;
                else
                    placar[6] = 0;
                break;
                
                case 7: // sequencia
                    // verifica se algum numero apareceu duas vezes
                    // se sim, a sequencia nao foi formada
                    for (int i = 1; i <= 6; i++) {
                        if (calculaFrequencia(dados, i) == 2)
                            valorDuplo = true;
                    }
                    if (valorDuplo)
                        placar[7] = 0;
                    else
                        placar[7] = 20;
                    break;
                
                case 8: // quadra
                    for (int i = 1; i <= 6; i++) {
                        if (calculaFrequencia(dados, i) == 4)
                            valorQuadruplo = true;
                    }
                    if (valorQuadruplo)
                        placar[8] = 30;
                    else
                        placar[8] = 0;
                    break;

                case 9: // quina
                    for (int i = 1; i <= 6; i++) {
                        if (calculaFrequencia(dados, i) == 5)
                            valorQuintuplo = true;
                    }
                    if (valorQuintuplo)
                        placar[9] = 40;
                    else
                        placar[9] = 0;
                    break;
        }
    }

    public int getScore() {

        int pontuacao = 0;

        for (int i = 0; i < tamanhoPlacar; i++) {
            if (placar[i] != -1)
                pontuacao += placar[i];
        }

        return pontuacao;
    }

    @Override
    public String toString() {

        String str = new String();

        int i = 0;
        int valoresNaLinha = 0;
        int qtdLinhas = 0;
        boolean aux = true;
        while (i < tamanhoPlacar && qtdLinhas < 3) {

            if (placar[i] == -1) 
                str += "  (" + (i + 1) + ")  |";
            else {
                if (placar[i] < 10)
                    str += " ";                
                str += "  " + placar[i] + "   |";
            }
                
            valoresNaLinha++;
            
            if (valoresNaLinha == 3) {
                str += "\n------------------------\n";
                i -= 2;
                valoresNaLinha = 0;
                qtdLinhas++;
                aux = true;
            }
            else {
                if (aux) {
                    i += 6;
                    aux = false;
                }
                else {
                    i -= 3;
                    aux = true;
                }
            }
        }
            
        str += "       |";
        if (placar[9] == -1)
            str += "  (" + 10 + ") |";
        else {
            if (placar[9] < 10)
                str += " ";
            str += "  " + placar[9] + "   |";
        }
        str += "\n       +-------+ ";

        return str;
    }
}
