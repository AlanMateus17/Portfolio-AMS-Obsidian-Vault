# Pipeline de conteúdo

[← Implantação](../../docs/implantacao/README.md)

`processar.py` lê as pastas de `~/AMtech/entrada`, transcreve áudio e vídeo com o Whisper local, pede as peças ao Claude seguindo `config/marca.md` e deixa tudo em `~/AMtech/fila` para você aprovar.

## Ligar

```bash
bash scripts/wsl/bootstrap.sh --com-whisper     # transcrição local
bash scripts/wsl/ativar-pipeline.sh             # cria ~/.config/amtech/conteudo.env na 1ª vez
# preencha ANTHROPIC_API_KEY (e o Telegram, se quiser) e rode de novo:
bash scripts/wsl/ativar-pipeline.sh
```

## Usar à mão

```bash
python3 tools/conteudo/processar.py --uma-vez             # processa agora
python3 tools/conteudo/processar.py --uma-vez --simular   # sem API, para testar o caminho
journalctl --user -u amtech-conteudo.service -n 50        # o que o timer fez
```

## Regras

- Arquivo copiado há menos de 1 minuto espera a próxima rodada (pode estar sendo copiado ainda).
- Depois de processado, o original vai para `~/AMtech/processados/<tipo>`.
- Três falhas seguidas no mesmo arquivo mandam ele para `entrada/_com-erro`, com o motivo.
- Uma execução por vez (trava em `entrada/.trava`).
- Testes: `python -m unittest discover -s tools/conteudo -v`.
