import gizeh
import moviepy.editor as mpy



class lattice
    self.SignatureRows = list()
    self.MyDictionary = Dictionary()
    self.StemToCurrentSignature = dict()
    self.MySignatureCollection = SignatureCollection()
    self.FromSignaturesToRowColumn = dict()
    def add_word(self, word):
        if word not in self.Lexicon:
            return
        this_stem, this_affix = self.Lexicon.GetStemAndAffix(word)
        if this_affix not in self.Lexicon.StemToAffix[this_stem]:
            return
        if this_stem not in self.StemToCurrentSignature:
            self.StemToCurrentSignature[this_stem] = list()
        this_sig = self.StemToCurrentSignature[this_stem]
        if this_sig.contains(this_affix):
            this_sig.blink()
            this_sig.grow()
            return
        new_sig_string = this_sig.add(this_affix)
        new_sig = self.FindOrMakeSignature(new_sig_string)
        self.StemToCurrentSignature[this_stem] = new_sig
        new_sig.blink()
        self.arrow(this_sig, new_sig)
        this_sig.shrink()
        new_sig.grow()
    def PrintImage(self):
        
    self.FindOrMakeSignature(self, new_sig_string):
        if new_sig_string not in self.MySignatureCollection.Signatures:
            this_new_sig = Signature(this_sigstring)
            self.MySignatureCollection.MySignatures[new_sig_string] = this_new_sig
            sig_length = new_sig_string.count("=") + 1
            row_no = sig_length
            column_no = len(self.SignatureRows[row_no])
            self.SignatureRows[row_no].append(this_new_sig)
            return this_new_sig
        else:
            return self.MySignatureCollection[new_sig_string]
class Dictionary:
    self.WordToStem = dict()
    self.WordToAffix = dict()
    self.StemToAffix = dict()

    def __init__(self):
    def GetStemAndAffix(self,word):
        return (self.WordToStem(word), self.WordToAffix(word))

class Signature:
    self.MyAffixes = list()
    def AddAffix(self, this_affix):
        self.MyAffixes.append(this_affix)
    def Blink(self):
    def Grow(self):
    def Shrink(self):

class SignatureCollection
    self.MySignatures = dict()

class Arrow:
    self.FromSig = Signature()
    self.ToSig   = Signature()
    def __init__(self, from_sig, to_sig):
        self.FromSig = from_sig
        self.ToSig = to_sig

def make_frame(t)
    surface = gizeh.Surface(W,H)
    m_lattice.add word( m_lattice.get_next_word() )
    m_lattice.print_image()



W = 128
H = 128
duration = 2

my_lattice = lattice()
clip = mpy.Videoclip(make_frame, duration = duration)
clip.write_gif("lattice.gif", fps = 15, opt = "OptimizePlus", fuzz = 0)
