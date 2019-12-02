
import geometrifadel

def main():
	m = float(input("masukkan massa : "))
	t = float(input("masukkan percepatan : "))
	v = float(input("masukkan tegangan : "))
	a = float(input("masukkan arus : "))
	g = float(input("masukkan gravitasi : "))
	y = float(input("masukkan waktu : "))
	
	gaya = geometrifadel.gaya(m,t)
	
	print("\nMENGHITUNG GAYA" )

	print("\nhasil : ",gaya,)
	
	
	
	
	
	hambatan = geometrifadel.hambatan(v, a)
	
	print("\nMenghitung HAMBATAN")
	print("\nhasil : ",hambatan,)
	
	print("\nMenghitung gerak jatuh bebas ")
	
	gerak = geometrifadel.gayajatuhbeban(g,y )
	
	print("\nhasil : ",gerak, " " )
	
	
if __name__ =="__main__":
	main()
