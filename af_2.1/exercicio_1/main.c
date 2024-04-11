#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

//       (pai)      
//         |        
//    +----+----+
//    |         |   
// filho_1   filho_2


// ~~~ printfs  ~~~
// pai (ao criar filho): "Processo pai criou %d\n"
//    pai (ao terminar): "Processo pai finalizado!\n"
//  filhos (ao iniciar): "Processo filho %d criado\n"

// Obs:
// - pai deve esperar pelos filhos antes de terminar!

/*************************************************
 * Dicas:                                        *
 * 1. Leia as intruções antes do main().         *
 * 2. Faça os prints exatamente como solicitado. *
 * 3. Espere o término dos filhos                *
 *************************************************/

int main(int argc, char** argv) {
    pid_t pid;

    for(int i = 0; i < 2; i++)
    {
        if((pid = fork()) == 0) break;
        printf("Processo pai criou %d\n", wait(NULL));
    }

    if(pid >= 0)
    {
        if(pid == 0)
            printf("Processo filho %d criado\n", getpid());
        else
            printf("Processo pai finalizado!\n");
    }
    else 
        return 1;
}
