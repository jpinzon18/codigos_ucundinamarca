Algoritmo SistemaCafetera

	// --- Variables de objetos ---
	Definir marca, modelo, tamaño_cafetera, capacidad_cafetera Como Cadena
	Definir temperaturaMaxEx, temperaturaMinEx, material, tiempo_prepa Como Cadena
	Definir placa_tempMax Como Cadena
	Definir resis_potencia, resis_temperatura Como Cadena
	Definir sensor1_tipo, sensor2_tipo, sensor2_exactitud Como Cadena
	Definir filtro_tipo Como Cadena
	Definir jarra_capacidad Como Cadena
	Definir jarra_nivel Como Entero
	Definir nombre Como Cadena
	Definir respJarra Como Cadena
	Definir jarraOk, verificado Como Logico

	// --- Inicialización de valores ---
	marca              <- "Oster"
	modelo             <- "BVSTEM7301"
	tamaño_cafetera    <- "34.5cm x 27.8cm x 30cm"
	capacidad_cafetera <- "2.8 litros"
	temperaturaMaxEx   <- "96 C"
	temperaturaMinEx   <- "88 C"
	material           <- "ACERO Y PLASTICO"
	tiempo_prepa       <- "3-4 MINUTOS"
	placa_tempMax      <- "55 y 60 grados"
	resis_potencia     <- "1380W - 1450W"
	resis_temperatura  <- "88C - 96C"
	sensor1_tipo       <- "nivel de agua"
	sensor2_tipo       <- "nivel de peso"
	sensor2_exactitud  <- "85%"
	filtro_tipo        <- "filtro de canasta"
	jarra_capacidad    <- "600 ml"
	jarra_nivel        <- 80

	// --- Inicio del sistema ---
	Escribir ""
	Escribir "====== SISTEMA DE CAFETERA ======"

	// Encendido
	Definir en Como Cadena
	en <- ""
	Mientras en <> "S" Hacer
		Escribir "La cafetera esta conectada a corriente? (S/N): "
		Leer en
		Si en = "S" Entonces
			Escribir "Cafetera conectada correctamente."
		SiNo
			Si en = "N" Entonces
				Escribir "Por favor conecta la cafetera."
			SiNo
				Escribir "Opcion no valida"
			FinSi
		FinSi
	FinMientras

	// Pedir nombre
	nombre <- ""
	Mientras nombre = "" Hacer
		Escribir "Ingresa tu nombre de usuario: "
		Leer nombre
	FinMientras
	Escribir "Hola, ", nombre, "! Bienvenido."

	// Boton de inicio
	Definir respBoton Como Cadena
	respBoton <- ""
	Mientras respBoton <> "S" Hacer
		Escribir ""
		Escribir "Presiono el boton de inicio? (S/N): "
		Leer respBoton
		Si respBoton = "S" Entonces
			Escribir "Iniciando proceso..."
		SiNo
			Si respBoton = "N" Entonces
				Escribir "Esperando que se presione el boton..."
			SiNo
				Escribir "Opcion no valida"
			FinSi
		FinSi
	FinMientras

	// Comprobar agua
	Definir respAgua Como Cadena
	respAgua <- ""
	Escribir ""
	Escribir "Sensor utilizado: ", sensor1_tipo
	Mientras respAgua <> "S" Hacer
		Escribir "El deposito tiene agua? (S/N): "
		Leer respAgua
		Si respAgua = "S" Entonces
			Escribir "Hay agua suficiente."
		SiNo
			Si respAgua = "N" Entonces
				Escribir "No hay agua."
				Escribir "Agrega agua para continuar."
			SiNo
				Escribir "Opcion no valida"
			FinSi
		FinSi
	FinMientras

	// Llenar jarra
	Definir validoJarra Como Logico
	validoJarra <- Falso
	Mientras validoJarra = Falso Hacer
		Escribir ""
		Escribir "Ingresa el nivel de la jarra (0 a 100): "
		Leer jarra_nivel
		Si jarra_nivel >= 0 Y jarra_nivel <= 100 Entonces
			Escribir "Nivel actualizado: ", jarra_nivel, "%"
			validoJarra <- Verdadero
		SiNo
			Escribir "El nivel debe estar entre 0 y 100."
		FinSi
	FinMientras

	// Comprobar posicion de jarra
	Definir respSensor Como Cadena
	respSensor <- ""
	jarraOk <- Falso
	Escribir ""
	Escribir "Sensor utilizado: ", sensor2_tipo
	Escribir "Exactitud: ", sensor2_exactitud
	Escribir "Capacidad de la jarra: ", jarra_capacidad
	Escribir "Nivel actual: ", jarra_nivel, "%"
	Mientras respSensor = "" Hacer
		Escribir "El sensor detecta la jarra colocada? (S/N): "
		Leer respSensor
		Si respSensor = "S" Entonces
			Si jarra_nivel >= 90 Entonces
				Escribir "La jarra esta demasiado llena."
				jarraOk <- Falso
			SiNo
				Si jarra_nivel <= 10 Entonces
					Escribir "La jarra esta muy vacia."
					jarraOk <- Falso
				SiNo
					Escribir "Jarra detectada y en nivel adecuado."
					jarraOk <- Verdadero
				FinSi
			FinSi
		SiNo
			Si respSensor = "N" Entonces
				Escribir "El sensor no detecta la jarra."
				Escribir "Colócala correctamente."
				respSensor <- ""
			SiNo
				Escribir "Opcion no valida."
				respSensor <- ""
			FinSi
		FinSi
	FinMientras

	Si jarraOk = Falso Entonces
		Escribir ""
		Escribir "Entrando en modo seguro..."
		Escribir "Apagando sistema..."
	SiNo
		// Verificacion general
		Definir respVerif Como Cadena
		respVerif <- ""
		verificado <- Falso
		Mientras respVerif = "" Hacer
			Escribir ""
			Escribir "Todo se verifico correctamente? (S/N): "
			Leer respVerif
			Si respVerif = "S" Entonces
				Escribir "Se iniciara el proceso de preparacion..."
				verificado <- Verdadero
			SiNo
				Si respVerif = "N" Entonces
					Escribir "Entrando en modo seguro..."
					Escribir "Apagando sistema..."
					verificado <- Falso
				SiNo
					Escribir "Opcion no valida"
					respVerif <- ""
				FinSi
			FinSi
		FinMientras

		Si verificado = Verdadero Entonces

			// Activar resistencia
			Escribir ""
			Escribir "Activando resistencia..."
			Escribir "Potencia: ", resis_potencia
			Escribir "Temperatura: ", resis_temperatura

			// Hervir agua
			Definir respHervir Como Cadena
			respHervir <- ""
			Mientras respHervir <> "S" Hacer
				Escribir ""
				Escribir "El agua ya hirvio? (S/N): "
				Leer respHervir
				Si respHervir = "S" Entonces
					Escribir "Agua caliente lista."
				SiNo
					Si respHervir = "N" Entonces
						Escribir "Calentando agua..."
					SiNo
						Escribir "Opcion no valida."
					FinSi
				FinSi
			FinMientras

			// Filtrar cafe
			Escribir ""
			Escribir "Filtrando cafe..."
			Escribir "Filtro utilizado: ", filtro_tipo
			Escribir "Preparando cafe..."

			// Verificar si jarra esta llena
			Si jarra_nivel >= 100 Entonces
				Escribir ""
				Escribir "La jarra esta completamente llena."
			SiNo
				Escribir ""
				Escribir "La jarra aun no esta llena."
			FinSi

			// Activar calefactor
			Escribir ""
			Escribir "Activando calefactor..."
			Escribir "Manteniendo temperatura entre ", placa_tempMax

			// Verificar si jarra sigue colocada
			Escribir ""
			Escribir "La jarra sigue colocada? (S/N): "
			Leer respJarra
			Si respJarra = "N" Entonces
				Escribir ""
				Escribir "La jarra fue retirada."
				Escribir "Apagando calefactor..."
			FinSi

			// Finalizar
			Escribir ""
			Escribir "La cafetera esta en funcionamiento..."
			Escribir "Cafe preparado correctamente."

		FinSi
	FinSi

FinAlgoritmo