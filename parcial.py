import os
os.system('cls')

var_totalFlt = 0
cons_desto = 2500 
cons_ceme = 50000 
cons_lad = 1500 
cons_llave = 5000 
cons_clav = 4000 
cons_pint = 75000 

cons_trap = 3500
cons_esco = 3200
cons_jabon = 4000
cons_dete = 3700
cons_espon = 2000

cons_cand = 40000 
cons_cama = 80000 
cons_alar = 110000 

cons_arroz = 2500 
cons_azu = 2000
cons_lech = 3400
cons_pane = 2500
cons_acei = 8000
cons_sal = 1700

cons_tv = 5200000 * 0.12
cons_compu = 1500000 * 0.12
cons_neve = 2800000 * 0.12
cons_estu = 1900000 * 0.12
cons_horn = 950000 * 0.12
cons_lava = 1400000 * 0.12


var_controlBln = True
while var_controlBln == True:
    os.system('cls')
    print('<<<<< WELCOME >>>>>')
    var_opcion = int(input('<<<< Elige categoria >>>> \n\n1. Ferreteria\n2. Áseo\n3. Seguridad\n4. Alimentos\n5. Electrodomesticos\n6. SALIR\n ->'))
    if var_opcion >= 1 and var_opcion <= 5:
        os.system('cls')
        if var_opcion == 1:
            var_ferreStr = int(input('<<< Agrega a la canasta >>> \n\n1. destornillador\n2. cemento\n3. ladrillos\n4. llave expancion\n5. clavos\n6. pintura\n7. salir\n ->'))
            if var_ferreStr >= 1 and var_ferreStr <= 6:
                var_cantidadInt = int(input('cantidad ->'))
            if var_ferreStr == 1:
                var_totalFlt += (var_cantidadInt * cons_desto)
            if var_ferreStr == 2:
                var_totalFlt += (var_cantidadInt * cons_ceme)
            if var_ferreStr == 3:
                var_totalFlt += (var_cantidadInt * cons_lad)
            if var_ferreStr == 4:
                var_totalFlt += (var_cantidadInt * cons_llave)
            if var_ferreStr == 5:
                var_totalFlt += (var_cantidadInt * cons_clav)
            if var_ferreStr == 6:
                var_totalFlt += (var_cantidadInt * cons_pint)
        os.system('cls')
        if var_opcion == 2:
            var_aseoStr = int(input('<<< Agrega a la canasta >>> \n\n1. trapera\n2. escoba\n3. jabon\n4. detergente\n5. esponjas\n ->'))
            if var_aseoStr >= 1 and var_aseoStr <= 5:
                var_cantidadInt = int(input('cantidad ->'))
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_trap)
            if var_aseoStr == 2:
                var_totalFlt += (var_cantidadInt * cons_esco)
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_jabon)
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_dete)
            if var_aseoStr == 1:
                var_totalFlt += (var_cantidadInt * cons_espon)
        os.system('cls')
        if var_opcion == 3:
            var_seguridadStr = int(input('<<< agrega a la canasta >>> \n\n1. candados\n2. camaras\n3. alrma contra incendios\n ->'))
            if var_seguridadStr >= 1 and var_aseoStr <= 3:
                var_cantidadInt = int(input('cantidad ->'))
            if var_seguridadStr == 1:
                var_totalFlt += (var_cantidadInt * cons_cand)
            if var_seguridadStr == 2:
                var_totalFlt += (var_cantidadInt * cons_cama)
            if var_seguridadStr == 3:
                var_totalFlt += (var_cantidadInt * cons_alar)
        os.system('cls')
        if var_opcion == 4:
            var_alimentosStr = int(input('<<< Agregar a la canasta >>> \n\n1. arroz\n2. azucar\n3. leche\n4. panela\n5. aceite\n6. sal\n ->'))
            if var_alimentosStr >= 1 and var_alimentosStr <= 6:
                var_cantidadInt = int(input('cantidad ->'))
            if var_alimentosStr == 1:
                var_totalFlt += (var_cantidadInt * cons_arroz)
            if var_alimentosStr == 2:
                var_totalFlt += (var_cantidadInt * cons_azu)
            if var_alimentosStr == 3:
                var_totalFlt += (var_cantidadInt * cons_lech)
            if var_alimentosStr == 4:
                var_totalFlt += (var_cantidadInt * cons_pane)
            if var_alimentosStr == 5:
                var_totalFlt += (var_cantidadInt * cons_acei)
            if var_alimentosStr == 6:
                var_totalFlt += (var_cantidadInt * cons_sal)
        os.system('cls')
        if var_opcion == 5:
            var_electrodomesticos = int(input('<<< Agregar a la canasta >>> \n\n1. TV\n2. computador\n3. nevera\n4. estufa\n5. horno\n6. lavadora\n ->'))
            if var_electrodomesticos >= 1 and var_electrodomesticos <= 6:
                var_cantidadInt = int(input('cantidad ->'))
            if var_electrodomesticos == 1:
                var_totalFlt += (var_cantidadInt * cons_tv) 
            if var_electrodomesticos == 2:
                var_totalFlt += (var_cantidadInt * cons_compu)
            if var_electrodomesticos == 3:
                var_totalFlt += (var_cantidadInt * cons_neve)
            if var_electrodomesticos == 4:
                var_totalFlt += (var_cantidadInt * cons_estu)
            if var_electrodomesticos == 5:
                var_totalFlt += (var_cantidadInt * cons_horn)
            if var_electrodomesticos == 6:
                var_totalFlt += (var_cantidadInt * cons_lava)
    if var_opcion == 6:
        print('el total a pagar:______________________________________________$', var_totalFlt)
        var_controlBln = False
