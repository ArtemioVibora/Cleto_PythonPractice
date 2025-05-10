class Atom:

    def __init__(self, name, numberOfProtons, numberOfNeutrons, numberOfElectrons,
        atomicWeight, atomicMass):
        self.name = name;
        self.numberOfProtons = numberOfProtons
        self.numberOfNeutrons = numberOfNeutrons
        self.numberOfElectrons = numberOfElectrons
        self.atomicWeight = atomicWeight
        self.atomicMass = atomicMass
        
    def display(self):
        print(f"Name of Element: {self.name}")
        print(f"Number of Protons: {self.numberOfProtons}")
        print(f"Number of Neutrons: {self.numberOfNeutrons}")
        print(f"Number of Electrons: {self.numberOfElectrons}")
        print(f"Atomic Weight: {self.atomicWeight}")
        print(f"Atomic Mass: {self.atomicMass}")
        
        
