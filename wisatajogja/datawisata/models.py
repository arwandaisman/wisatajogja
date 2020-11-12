from django.db import models  
class Jenis(models.Model):
    jenis = models.CharField(max_length = 9)
    keterangan = models.TextField()

    def __str__(self):
        return self.jenis        
        

class Datawisata(models.Model):  
    nama_wisata = models.CharField(max_length=100,null=True,blank=False)  
    kabupaten = models.CharField(max_length=20,null=True,blank=False)  
    jml_pengunjung = models.IntegerField(null=True,blank=False) 
    lokasi = models.CharField(max_length=50,null=True,blank=False) 
    jenis_id = models.ForeignKey(Jenis, on_delete=models.CASCADE, null=True) 
    

    def __str__(self) :
        return self.nama_wisata
