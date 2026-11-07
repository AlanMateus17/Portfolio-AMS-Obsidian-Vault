# Modelo de CLI e firmware em Rust

Rust entra onde ele é o melhor: binário pequeno e rápido, e firmware (ESP32-C3/C6 e STM32, gravados e depurados pelo probe-rs). `rust` e `cargo-dist` vêm do mise.

    cp -r ~/dev/dev-setup/infra/templates/rust-cli ~/dev/minha-cli && cd ~/dev/minha-cli && cargo run -- Alan
    dist init        # gera o workflow de release multiplataforma

Firmware: comece pelo `esp-generate` (ESP32) ou pelos exemplos do Embassy (STM32) e grave com `probe-rs run`.
