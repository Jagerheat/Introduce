
def make_country(Ukraine, **Kiev):
    print(f"{Ukraine}")
    for name, capital in Kiev.items():
        print(f"{name}: {capital}")
make_country("Name", Name="Ukraine", Capital="Kiev")
