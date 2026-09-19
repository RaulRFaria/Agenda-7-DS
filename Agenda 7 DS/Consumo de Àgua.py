print("=" * 45)
print("  Saiba seu Consumo de água com o AGC ")
print("=" * 45)

Qual_seria_seu_imovel = input(
    "Qual seria o seu tipo de imóvel? (comercial, casa ou apartamento): "
).strip().lower()

consumo = float(input("Digite o consumo mensal de água em m³: "))

if Qual_seria_seu_imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif Qual_seria_seu_imovel in ["casa", "apartamento"] and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif Qual_seria_seu_imovel in ["casa", "apartamento"] and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print(
        "Consumo excessivo – adote medidas de economia "
        "e verifique vazamentos."
    )