#nama : Rahma Divina
#tanggal : 17/02/2023
#version : v.01

import pickle
import os
kontak = {}

def tampilMenu():
    print("\n+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("+   PHONEBOOK PROGRAM   +")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("+ 1.Lihat Semua Kontak  +")
    print("+ 2.Tambah Kontak Baru  +")
    print("+ 3.Hapus Kontak        +")
    print("+ 4.Update Kontak       +")
    print("+ 5.Cari Kontak         +")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    pilih = input("Inputkan pilihanmu (1-5) : ")
    return pilih
    
def lihatKontak():
    phone = open("PhoneBook.txt", "r")
    print(phone.read())
    phone.close()
    

def tambahKontak():
    global kontak
    nama = input ("Masukkan nama : " )
    nomor = input ("Masukkan nomor : ")
    kontak[nama] = nomor
    phone = open("PhoneBook.txt", "a")
    phone.write("\n" + nama + " -- " + nomor )
    phone.close()

def hapusKontak ():
    nama = input("Masukkan nama yang akan dihapus: ")
    with open("PhoneBook.txt", "r") as phone:
        lines = phone.readlines()
    with open("PhoneBook.txt", "w") as phone:
        removed = False
        for line in lines:
            if not nama.lower() in line.lower():
                phone.write(line)
            else:
                removed = True
        if removed:
            print(f"Kontak dengan nama '{nama}' berhasil dihapus.")
        else:
            print(f"Tidak ditemukan kontak dengan nama '{nama}'.")

def updateNamaKontak():
    global kontak 
    cariNama = input ("Masukkan nama kontak yang ingin diupdate : ")
    namaBaru = input ("Masukkan nama kontak baru : ")
    phone = open("PhoneBook.txt", "r")
    text = phone.read()
    new_text = text.replace(cariNama,namaBaru)
    phone = open("PhoneBook.txt", "w")
    phone.write(new_text)
    phone.close()

def updateNomorKontak():
    global kontak 
    cariNomor = input ("Masukkan nomor yang ingin diupdate : ")
    nomorBaru = input ("Masukkan nomor kontak baru : ")
    phone = open("PhoneBook.txt", "r")
    text = phone.read()
    new_text = text.replace(cariNomor,nomorBaru)
    phone = open("PhoneBook.txt", "w")
    phone.write(new_text)
    phone.close()

def pilihUpdate():
    print("Pilih Update : ")
    print("1. Update nama kontak ")
    print("2. Update nomor kontak ")
    select = input ("input pilihan : ")
    if select == "1" :
        updateNamaKontak()
    else :
        updateNomorKontak()

def cariKontak():
    nama = input("Masukkan nama kontak yang ingin dicari: ")
    with open("PhoneBook.txt", "r") as f:
        for line in f:
            if nama in line:
                print(line)
                return
    print("Kontak tidak ditemukan.")
    

    
while True :
    pilih = tampilMenu()
    if pilih == "1":
        lihatKontak()
    elif pilih == "2" :
        tambahKontak()
    elif pilih == "3" :
        hapusKontak()
    elif pilih == "4":
        pilihUpdate()
    else :
        cariKontak()
        



    



