def ispis_kolegija(kolegij):
    print(f"Kolegij {kolegij['ime']} nosi {kolegij['ECTS']} bodova")

def get_kolegij(redni_broj, kolegij):
    return f"{redni_broj}. {kolegij['ime']}"