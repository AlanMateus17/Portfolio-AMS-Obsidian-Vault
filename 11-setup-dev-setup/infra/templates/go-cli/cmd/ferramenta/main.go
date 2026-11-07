// Modelo de CLI em Go com tela interativa (bubbletea). Troque "ferramenta" pelo nome real.
//   go mod tidy && go run ./cmd/ferramenta
package main

import (
	"fmt"
	"os"

	tea "github.com/charmbracelet/bubbletea"
)

type modelo struct {
	opcoes []string
	cursor int
	feito  string
}

func (m modelo) Init() tea.Cmd { return nil }

func (m modelo) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	if k, ok := msg.(tea.KeyMsg); ok {
		switch k.String() {
		case "ctrl+c", "q":
			return m, tea.Quit
		case "up", "k":
			if m.cursor > 0 {
				m.cursor--
			}
		case "down", "j":
			if m.cursor < len(m.opcoes)-1 {
				m.cursor++
			}
		case "enter":
			m.feito = m.opcoes[m.cursor]
			return m, tea.Quit
		}
	}
	return m, nil
}

func (m modelo) View() string {
	s := "O que fazer?\n\n"
	for i, o := range m.opcoes {
		marca := "  "
		if i == m.cursor {
			marca = "> "
		}
		s += marca + o + "\n"
	}
	return s + "\n↑/↓ escolhe, Enter confirma, q sai\n"
}

func main() {
	final, err := tea.NewProgram(modelo{opcoes: []string{"Status", "Backup", "Deploy"}}).Run()
	if err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
	if m := final.(modelo); m.feito != "" {
		fmt.Println("Escolhido:", m.feito)
	}
}
