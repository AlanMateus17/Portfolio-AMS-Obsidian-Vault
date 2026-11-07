import unittest
from pathlib import Path
import tempfile

import ifc_resumo

IFC = """ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('ViewDefinition [CoordinationView]'),'2;1');
FILE_NAME('casa.ifc','2026-11-02T10:00:00',(''),(''),'Bonsai','Bonsai','');
FILE_SCHEMA(('IFC4'));
ENDSEC;
DATA;
#1=IFCPROJECT('0YvctVUKr0kugbFTf53O9L',$,'Casa Exemplo',$,$,$,$,$,$);
#10=IFCBUILDINGSTOREY('1',$,'Pavimento Superior',$,$,$,$,$,.ELEMENT.,2.85);
#11=IFCBUILDINGSTOREY('2',$,'T\\X2\\00E9\\X0\\rreo',$,$,$,$,$,.ELEMENT.,0.);
#20=IFCWALL('3',$,'Parede 01',$,$,$,$,$,$);
#21=IFCWALL('4',$,'Parede 02',$,$,$,$,$,$);
#22=IFCWALLSTANDARDCASE('5',$,'Parede 03',$,$,$,$,$);
#23=IFCSLAB('6',$,'Laje',$,$,$,$,$,.FLOOR.);
#24=IFCDOOR('7',$,'Porta, sala',$,$,$,$,$,0.8,2.1,$,$,$);
#30=IFCQUANTITYAREA('NetSideArea',$,$,12.5,$);
#31=IFCQUANTITYAREA('NetSideArea',$,$,7.25,$);
#32=IFCQUANTITYVOLUME('NetVolume',$,$,
  3.1E0,$);
ENDSEC;
END-ISO-10303-21;
"""


class TesteIfc(unittest.TestCase):
    def setUp(self):
        self.r = ifc_resumo.resumir(IFC)

    def test_esquema_e_projeto(self):
        self.assertEqual(self.r["esquema"], "IFC4")
        self.assertEqual(self.r["projeto"], "Casa Exemplo")

    def test_pavimentos_em_ordem_e_acento(self):
        self.assertEqual([p["nome"] for p in self.r["pavimentos"]], ["Térreo", "Pavimento Superior"])
        self.assertEqual(self.r["pavimentos"][1]["elevacao"], 2.85)

    def test_elementos(self):
        self.assertEqual(self.r["elementos"]["Paredes"], 3)
        self.assertEqual(self.r["elementos"]["Lajes e pisos"], 1)
        self.assertEqual(self.r["elementos"]["Portas"], 1)

    def test_quantidades_somadas_e_multilinha(self):
        q = {(x["nome"], x["unidade"]): x["total"] for x in self.r["quantidades"]}
        self.assertEqual(q[("NetSideArea", "m²")], 19.75)
        self.assertEqual(q[("NetVolume", "m³")], 3.1)

    def test_argumentos_com_virgula_no_texto(self):
        a = ifc_resumo.argumentos("'7',$,'Porta, sala',(1,2),'It''s'")
        self.assertEqual(len(a), 5)
        self.assertEqual(ifc_resumo.texto_step(a[2]), "Porta, sala")
        self.assertEqual(ifc_resumo.texto_step(a[4]), "It's")

    def test_markdown_e_arquivo_invalido(self):
        md = ifc_resumo.markdown(self.r, "casa.ifc")
        self.assertIn("| Paredes | 3 |", md)
        self.assertIn("| NetSideArea | 19.75 | m² |", md)
        with tempfile.NamedTemporaryFile("w", suffix=".ifc", delete=False) as f:
            f.write("isto não é IFC")
        self.assertEqual(ifc_resumo.main([f.name]), 1)
        Path(f.name).unlink()

    def test_modelo_sem_quantidades(self):
        md = ifc_resumo.markdown(ifc_resumo.resumir(IFC.split("#30=")[0] + "ENDSEC;"), "x.ifc")
        self.assertIn("não exportou quantidades", md)


if __name__ == "__main__":
    unittest.main()
