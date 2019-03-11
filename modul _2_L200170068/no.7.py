import LatOOP4            # Atau apapun file-nya yang kamu buat tadi

class MhsTIF(LatOOP4.Mahasiswa):    # perhatikan class induknya : Mahasiswa
    """Class MhsTIF yang dibangun dari class Mahasiswa"""
    def kataKanPy(self):
        print('Python is cool.')

# Pertanyaan:
# Apakah metode / state itu berasal dari class Manusia, Mahasiswa, atau MhsTIF?

# Jawaban :

# Metoode atau state muncul berasal dari semua class baik Manusia, Mahasiswa, atau MhsTIF.
# MhsTIF merupakan anak class dari Mahasiswa, dan itu membuat MhsTIF mewarisi semua properties dari Mahasiswa dan Manusia.
