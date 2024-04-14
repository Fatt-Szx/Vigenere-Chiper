from cx_Freeze import setup, Executable

setup(name='vegenere hiper',
      version='1.0',
      description='Program Enkripsi - Dekripsi Tugas Pertemuan 3',
      executables=[Executable('vigenere_cipher.py')])
