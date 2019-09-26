import xlrd
import array3d

def main():
	a3d=array3d(35,32,12)

	for año in range(1985,2020,1):
		archivo= xlrd.open_workbook(filename=str(año)+'Precip.xls')
		hoja=archivo.sheet_by_index(0)
		for estado in range(2,34,1):
			for mes in range(1,13,1):
				lista=hoja.cell_value(estado,mes)
				a3d.set_item(año-1985,estado-2,mes-1,lista)

	a3d.to_String()
	anio=int(input("Dame el año 1985 a 2019"))
	estado2=int(input("Dame el estado: 1 a 32 "))
	Mes=int(input("Dame el mes: 1 a 12 "))
	promedio= a3d.get_item(estado2-1,Mes-1,anio-1985)
	print("El promedio de las lluvias es:",promedio)


main()

