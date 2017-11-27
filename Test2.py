def main():
    try:
        bestand = "alpaca.fa"
        headers, seqs = lees_inhoud(bestand)
        
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:",headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")

    except FileNotFoundError:
        print("Bestand is niet aanwezig")
    except KeyboardInterrupt:
        print ()
        print ("Programma werd onderbroken")
    
def lees_inhoud(bestands_naam):
     bestand = open(bestands_naam)
     headers = []
     seqs = []
     seq = ""
     for line in bestand:
         line=line.strip()
         if ">" in line:
             if seq != "":
                 seqs.append(seq)
                 seq = ""
             headers.append(line)
         else:
             seq += line.strip()
     seqs.append(seq)
     return headers, seqs

    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna

# bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken
def knipt(alpaca_seq):
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^","")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except FileNotFoundError:
        print ('Enzym bestand is niet aanwezig')


main()
