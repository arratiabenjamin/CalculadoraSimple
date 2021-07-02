#Variables
operation = ''
confirm = ''
a = ''
b = ''

#Inicio de todo
def operationC():

    def operationAB():

        #7.Confirmacion de operacion y si no se vuelve a pedir todo nuevamente, si no se escribe bien se pide responder nuevamente
        def confirmation():
            #Preguntar si esta bien y como escribir la respuesta
            print('\r\nSOLO ESCRIBIR "si" o "no"\r\n')
            confirm = input('Esto estaria bien?\r\n')

            if confirm == 'si' and operation == 'suma':
                print(f'El resultado es: {a + b}')
            elif confirm == 'si' and operation == 'resta':
                print(f'El resultado es: {a - b}')
            elif confirm == 'si' and operation == 'multiplicacion':
                print(f'El resultado es: {a * b}')
            elif confirm == 'si' and operation == 'division':
                print(f'El resultado es: {a / b}')
            elif confirm == 'no':
                operationC()
            else:
                print('\r\nEquivocacion al escribir, escribir nuevamente:')
                confirmation()

        #4.Segunda expliacion
        print('\r\nPORFAVOR SOLO ESCRIBA NUMEROS\r\n')

        a = input('Escriba el primer numero: \r\n')
        b = input('Escriba el segundo numero: \r\n')
        
        #5.Convertir a int
        a = int(a)
        b = int(b)

        #6.Informar cual será la operacion
        if operation == 'suma':
            print(f'Su operacion sera: {a} + {b}')
            confirmation()
        elif operation == 'resta':
            print(f'Su operacion sera: {a} - {b}')
            confirmation()
        elif operation == 'multiplicacion':
            print(f'Su operacion sera: {a} * {b}')
            confirmation()
        elif operation == 'division':
            print(f'Su operacion sera: {a} ÷ {b}')
            confirmation()

    #1.Explicacion
    print('\r\nPORFAVOR INTRODUCIR:')
    print('suma\r\nresta\r\nmultiplicacion\r\ndivision\r\n')

    #2.Pedir tipo de operacion
    operation = input('Porfavor introcuzca el tipo de operacion: \r\n')

    #3.Confirmar si escribió bien el nombre de la operacion, si no se vuelve a pedir
    if operation == 'suma' or operation == 'resta' or operation == 'multiplicacion' or operation == 'division':
        operationAB()
    else:
        print('\r\nEquivocacion al escribir el tipo de operacion, escribir nuevamente:')
        operationC()

operationC()