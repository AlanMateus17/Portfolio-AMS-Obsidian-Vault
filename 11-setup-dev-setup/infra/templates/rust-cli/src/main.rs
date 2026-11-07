// Modelo de CLI em Rust. Release multiplataforma com cargo-dist: dist init (uma vez) e depois tag v*.
fn main() {
    let nome = std::env::args().nth(1).unwrap_or_else(|| "mundo".into());
    println!("Olá, {nome}!");
}
