import random

def sampah_organik():
    nama_sampah = ['daun','sayur',
                   'buah', 'nasi',
                   'tai', 'kotoran',
                   'ranting', 'kertas',
                   'limbah dapur', 'tulang',
                   'cangkang telur', 'ampas kopi',
                   'ampas teh']
    
    return random.choice(nama_sampah)

def sampah_anorganik():
    nama_sampah = ['bungkus plastik', 'botol plastik',
                   'kresek', 'kotak', 
                   'kardus', 'kertas',
                   'baterai', 'besi', 'kaleng',
                   'DVD', ] 
    
    return random.choice(nama_sampah)
