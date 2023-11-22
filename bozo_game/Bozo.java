public class Bozo {

    private static int qtdRodadas = 10;
    private static int qtdDados   = 5;

    public static void main(String args[]) throws java.io.IOException {

        RolaDados rolaDados = new RolaDados(qtdDados);
        Placar placar = new Placar();
        int valores[] = new int[qtdDados];

        for (int i = 0; i < qtdRodadas; i++) {

            // começando a rodada
            System.out.printf("Aperte ENTER para começar a rodada %d ", i + 1);
            EntradaTeclado.leString();

            // rolando e exibindo os dados pela primeira vez
            valores = rolaDados.rolar();
            System.out.println("\n" + rolaDados.toString());

            // escolhendo os dados a serem rolados de novo
            boolean aux = true;
            for (int j = 0; j < 2 && aux; j++) {
                boolean leituraValida = false;
                while (!leituraValida) {
                    leituraValida = true;
                    try {
                        System.out.print("Digite os dados que quer rolar de novo: ");
                        String str = EntradaTeclado.leString();
                        if (str.length() == 0) {
                            aux = false;
                            continue;
                        }
                        valores = rolaDados.rolar(str);
                    }
                    catch (Exception e) {
                        System.out.println("Entrada invalida");
                        leituraValida = false;
                    }
                }
                System.out.println("\n" + rolaDados.toString());
            }

            // mostrando o placar atual
            System.out.println("\n" + placar.toString());
            
            // escolhendo a posicao a ser ocupada
            int posicao = 0;
            boolean posicaoValida = false;
            while (!posicaoValida) {
                posicaoValida = true;
                try {
                    System.out.print("Qual posicao quer ocupar? ");
                    posicao = EntradaTeclado.leInt();
                    placar.add(posicao - 1, valores);
                }
                catch (Exception e) {
                    System.out.println("Posicao invalida, tente novamente");
                    posicaoValida = false;
                }
            }
            
            // mostrando o placar atualizado
            System.out.println("\n" + placar.toString() + "\n");
        }

        System.out.printf("\nA pontuação final foi de %d pontos\n", placar.getScore());
    }
}
