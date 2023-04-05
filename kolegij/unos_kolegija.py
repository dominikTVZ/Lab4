def unos_kolegija(redni_broj):
    kolegij = {}
    kolegij['ime'] = input("Unesite ime kolegija: ").upper()
    kolegij['ECTS'] = int(input(f"Unesite ECTS bodove za {redni_broj}. kolegij: "))
    return kolegij
