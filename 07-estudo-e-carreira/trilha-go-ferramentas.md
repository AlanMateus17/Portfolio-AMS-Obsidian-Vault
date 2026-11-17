---
tags: [estudo, go, ferramentas, portfolio-ams]
tipo: trilha
status: ativo
atualizado: 2026-11-13
---

# 🛠️ Go para as suas ferramentas — passo a passo

> **Em palavras simples:** Go é a linguagem com que você vai fabricar as **suas próprias ferramentas** — programinhas de linha de comando que automatizam o seu dia (organizar arquivos, gerar relatório, fazer backup, falar com a impressora fiscal). Go gera **um único arquivo executável**, sem instalar nada no computador de ninguém. É isso que faz dela perfeita pra ferramenta.

> **Por que Go e não TS/Python aqui:** TS e Python precisam de runtime instalado (Node, Python) pra rodar. Go compila pra um binário só, que você copia e roda — no seu PC, no servidor ou no balcão do cliente. Pra ferramenta e pro agente fiscal, isso vale ouro. O núcleo (TS+Python+SQL) continua sendo o centro; Go é a oficina de ferramentas.

---

## Como esta trilha roda no plano

- **Entra no Mês 2** (depois que você já tem lógica + TS básico — aí Go fica fácil).
- **Volta sempre** que você precisar de uma ferramenta nova (uma por vez, resolvendo um problema real seu).
- **Culmina no agente fiscal** do AM Gestão (Mês 4) e nas ferramentas do dev-setup.
- Ritmo: **1 bloco por semana** (sábado ou quinta), sem roubar o foco do AM Gestão.

**Regra de ouro:** você nunca estuda Go "no vazio". Cada bloco **entrega uma ferramenta que você vai usar de verdade.**

---

## Pré-requisito

- Lógica e um pouco de TS já vistos (variáveis, funções, condições, laços). Go é simples: se você entende lógica, aprende a sintaxe em dias.
- Instalar Go: [go.dev/doc/install](https://go.dev/doc/install). Conferir: `go version`.

---

## Os 6 passos (cada um = uma ferramenta de verdade)

### Go-1 · "Olá, ferramenta": a base da linguagem
**Objetivo:** escrever, compilar e rodar seu primeiro binário.
**Estudar (passo a passo):**
1. [Tour of Go](https://go.dev/tour/) — partes 1 a 3 (tipos, funções, laços, condições).
2. `go mod init` (criar o módulo), `go run` (rodar), `go build` (gerar o binário).
3. Ler argumentos da linha de comando com o pacote `flag`.

**Exemplo — uma saudação com argumento:**
```go
package main

import (
	"flag"
	"fmt"
)

func main() {
	nome := flag.String("nome", "mundo", "a quem saudar")
	flag.Parse()
	fmt.Printf("Olá, %s! Sua primeira ferramenta.\n", *nome)
}
```
Rodar: `go run . -nome Alan` → `Olá, Alan!`. Gerar binário: `go build -o saudar` → agora existe um arquivo `saudar` que roda sozinho.

**✅ Pronto quando:** você gera um binário e roda ele sem `go run`, passando um argumento.

---

### Go-2 · Organizador de arquivos (ler e mexer em pastas)
**Objetivo:** uma ferramenta que varre uma pasta e organiza por tipo/data.
**Estudar:**
1. Pacote `os` (ler pasta, mover arquivo) e `path/filepath` (caminhos, extensão).
2. `os.ReadDir`, `os.Rename`, `filepath.Ext`.
3. Tratamento de erro idiomático (`if err != nil`).

**Exemplo — listar arquivos de uma pasta:**
```go
entradas, err := os.ReadDir(".")
if err != nil {
	log.Fatal(err)
}
for _, e := range entradas {
	fmt.Println(e.Name(), filepath.Ext(e.Name()))
}
```
**✅ Pronto quando:** sua ferramenta organiza a pasta de Downloads (ou os gabaritos de aula) em subpastas por extensão.

---

### Go-3 · Relatório a partir de dados (ler CSV/JSON, escrever arquivo)
**Objetivo:** ler um CSV (ex.: vendas, notas de alunos) e gerar um resumo.
**Estudar:**
1. `encoding/csv` e `encoding/json`.
2. `structs` e `slices` (listas) para guardar os registros.
3. Escrever um arquivo de saída (`os.Create`, `fmt.Fprintf`).

**✅ Pronto quando:** você joga um CSV e sai um `.md` ou `.txt` com totais — algo que você usaria nas aulas ou no financeiro.

---

### Go-4 · Backup e automação (rodar comandos, agendar)
**Objetivo:** ferramenta que faz backup 3-2-1 (ligado ao seu dev-setup).
**Estudar:**
1. `os/exec` (rodar comandos do sistema: `rsync`, `tar`, `git`).
2. `time` (datas, carimbar o backup).
3. Variáveis de ambiente (`os.Getenv`) para segredos — nunca no código.

**✅ Pronto quando:** um binário faz o backup dos seus repositórios e anota a data num log. Entra no setup como ferramenta fixa.

---

### Go-5 · Servir HTTP e falar com a web (API simples)
**Objetivo:** entender o `net/http` — base do agente fiscal e de ferramentas que expõem dados.
**Estudar:**
1. `net/http` (servidor mínimo, rotas, handlers).
2. Consumir uma API (`http.Get`, ler JSON).
3. Concorrência básica: `goroutines` e `channels` (o grande diferencial de Go).

**Exemplo — servidor mínimo:**
```go
http.HandleFunc("/status", func(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, `{"ok": true}`)
})
log.Fatal(http.ListenAndServe(":8080", nil))
```
**✅ Pronto quando:** você sobe um servidor local que responde em `localhost:8080/status`.

---

### Go-6 · Agente fiscal do AM Gestão (o projeto real)
**Objetivo:** o binário que roda no balcão do cliente e fala com a impressora fiscal.
**Estudar/aplicar:**
1. Expor uma API HTTP local (`localhost`) que o PDV (TypeScript) chama — você já sabe de Go-5.
2. Comunicação serial/USB com a impressora (ESC/POS), gaveta de dinheiro, TEF.
3. Distribuir: `go build` para Windows e Linux (cross-compile com `GOOS`/`GOARCH`).
4. Instalar como serviço em background.

**✅ Pronto quando:** o Caixa (TS) manda imprimir e o agente em Go imprime no hardware. É o ponto em que Go deixa de ser estudo e vira peça do produto.

---

## Documentação oficial (fonte da verdade)
- [Tour of Go](https://go.dev/tour/) — interativo, comece aqui.
- [Effective Go](https://go.dev/doc/effective_go) — como escrever Go idiomático.
- [Go by Example](https://gobyexample.com/) — exemplos curtos por tópico (ótimo pra consulta rápida).
- [Documentação dos pacotes](https://pkg.go.dev/std) — `flag`, `os`, `net/http`, etc.
- Livro (quando quiser aprofundar): *The Go Programming Language* (Donovan & Kernighan).

## Como medir
Cada passo entrega **um binário que você usa**. Ao fim dos 6, você tem: organizador, relatório, backup e o agente fiscal — e sabe fabricar qualquer ferramenta nova sozinho. Isso já é um portfólio de ferramentas em Go.

## 🔗 Relacionados
- [PLANO-PASSO-A-PASSO](PLANO-PASSO-A-PASSO.md) · [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md) · [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md)
