from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
print(guia)

guia_2 = guia.with_name("La_Pedrera.txt")
print(guia_2)

print(guia.parent.parent)
print("")

guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob("**/*.txt"):
    print(txt)

print("")

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_espania)