/*
 * Crackme da aula: um "programa pago" que confere a chave de licença NO CLIENTE.
 * Escrito para ser quebrado em sala, com binário que os próprios alunos compilam.
 *
 * Compile (Ubuntu):   gcc -O0 -g -o licenca licenca.c
 * Rode:               ./licenca
 * Desafio 1 (5 min):  strings licenca | less          -> a chave aparece em texto puro?
 * Desafio 2 (15 min): abra no Ghidra, ache main e chave_valida, leia o pseudo-C.
 * Desafio 3 (20 min): compile com -O2 e compare o assembly no Compiler Explorer (godbolt.org).
 * Discussão:          por que a checagem de licença tem que ficar no servidor?
 *
 * Regra da turma: só analisamos binários que nós mesmos compilamos ou desafios feitos para isso.
 */
#include <stdio.h>
#include <string.h>

/* Erro de propósito: segredo dentro do programa que vai para o usuário. */
static const char CHAVE[] = "AMTECH-2027-AULA";

static int chave_valida(const char *digitada)
{
    return strcmp(digitada, CHAVE) == 0;
}

int main(void)
{
    char entrada[64];

    printf("Chave de licenca: ");
    if (fgets(entrada, sizeof entrada, stdin) == NULL) {
        return 1;
    }
    entrada[strcspn(entrada, "\n")] = '\0';

    if (chave_valida(entrada)) {
        puts("Licenca ativada. Bem-vindo a versao completa!");
        return 0;
    }
    puts("Chave invalida.");
    return 1;
}
