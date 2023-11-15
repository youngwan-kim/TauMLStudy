from ROOT import TLorentzVector
from ROOT import TMath

class Particle(TLorentzVector):
    def __init__(self, pt, eta, phi, mass):
        TLorentzVector.__init__(self)
        self.SetPtEtaPhiM(pt, eta, phi, mass)
        self.charge = 0
        self.btagScore = 0.
        self.decaymode = 0
        self.genpartflav = 0
        self.isMuon = False
        self.isElectron = False
        self.isJet = False
        self.isFatJet = False
        self.lsf3 = 0.
        self.tau3 = 0.
        self.isTau = False

    def Charge(self):
        return self.charge
    
    def BtagScore(self):
        return self.btagScore
    
    def MT(self, part):
        dPhi = self.DeltaPhi(part)
        return TMath.Sqrt(2*self.Pt()*part.Pt()*(1.-TMath.Cos(dPhi)))

    def IsMuon(self):
        return self.isMuon
    
    def IsElectron(self):
        return self.isElectron
    
    def IsTau(self):
        return self.isTau
    
    def DecayMode(self):
        return self.decaymode
    
    def GenPartFlav(self):
        return self.genpartflav
    
    def IsJet(self):
        return self.isJet
    
    def IsFatJet(self):
        return self.isFatJet
    
    def LSF3(self):
        return self.lsf3
    
    def Tau3(self):
        return self.tau3

class Lepton(Particle):
    def __init__(self, pt, eta, phi, mass):
        Particle.__init__(self, pt, eta, phi, mass)
        
    def SetCharge(self, charge):
        self.charge = charge
    
    
class Muon(Lepton):
    def __init__(self, pt, eta, phi, mass):
        Lepton.__init__(self, pt, eta, phi, mass)
        self.isMuon = True
        

class Electron(Lepton):
    def __init__(self, pt, eta, phi, mass):
        Lepton.__init__(self, pt, eta, phi, mass)
        self.isElectron = True
        
class Tau(Lepton):
    def __init__(self, pt, eta, phi, mass) :
        Lepton.__init__(self, pt, eta, phi, mass)
        self.isTau = True
        self.decaymode = 0
        self.genpartflav = 0
    
    def SetDecayMode(self, decaymode):
        self.decaymode = decaymode

    def SetGenPartFlav(self, genpartflav):
        self.genpartflav = genpartflav

class Jet(Particle):
    def __init__(self, pt, eta, phi, mass):
        Particle.__init__(self, pt, eta, phi, mass)
        self.isJet = True
        self.isBtagged = False
        
    def SetCharge(self, charge):
        self.charge = charge
        
    def SetBtagScore(self, btagScore):
        self.btagScore = btagScore
        
    def SetBtagging(self, isBtagged):
        self.isBtagged = isBtagged
        
    def IsBtagged(self):
        return self.isBtagged 
    
class FatJet(Particle):
    def __init__(self, pt, eta, phi, mass):
        Particle.__init__(self, pt, eta, phi, mass)
        self.isFatJet = True

    def SetCharge(self, charge):
        self.charge = charge

    def SetLSF3(self):
        return self.lsf3
    
    def SetTau3(self):
        return self.tau3