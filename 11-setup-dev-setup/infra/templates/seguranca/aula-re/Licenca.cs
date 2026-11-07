// Mesma aula em C#: mostra que .NET volta quase igual ao código-fonte.
//
//   dotnet new console -n Licenca && cp Licenca.cs Licenca/Program.cs && cd Licenca && dotnet build -c Release
//   ilspycmd bin/Release/net10.0/Licenca.dll        (ou abra a .dll no ILSpy do Windows)
//
// O que os alunos devem perceber: nomes de classe, de método e a constante aparecem inteiros.
// Ofuscador só atrasa. A única defesa real é a checagem rodar no servidor, com a chave fora do binário.
using System;

const string Chave = "AMTECH-2027-AULA"; // erro de propósito: segredo no cliente

Console.Write("Chave de licença: ");
var digitada = Console.ReadLine() ?? "";

Console.WriteLine(ChaveValida(digitada)
    ? "Licença ativada. Bem-vindo à versão completa!"
    : "Chave inválida.");

static bool ChaveValida(string digitada) => string.Equals(digitada, Chave, StringComparison.Ordinal);
