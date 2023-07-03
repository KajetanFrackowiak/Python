spin = str(input())
electric_charge = str(input())

if spin == "1/2" and electric_charge == "-1/3":
    print('Strange Quark')
elif spin == "1/2" and electric_charge == "2/3":
    print("Charm Quark")
elif spin == "1/2" and electric_charge == "-1":
    print("Electron Lepton")
elif spin == "1/2" and electric_charge == "0":
    print("Neutrino Lepton")
elif spin == "1" and electric_charge == "0":
    print("Photon Boson")
