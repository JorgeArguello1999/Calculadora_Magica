import sys #Acceso a las opciones del sistema
import ctypes #Geometrias del Sistema Operativo
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox 
from PyQt5 import uic #Para procesar el diseño de QtDesigner
from PyQt5.QtGui import QFont #Importa las fuenters
from PyQt5.QtCore import Qt

#Clase que hereda de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
   
    #Metodo constructor de clase
    def __init__(self):
        
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        
        #Con esta linea cargamos el formato .ul a el objeto
        uic.loadUi("Interface.ui", self)
        self.setWindowTitle("Calculadora Magica")
        
        #fijar tamaño de la ventana
        self.setMaximumSize(500, 500)
        self.setMinimumSize(500,500)
        
        #Colocamos la ventana en el centro
        """
        ESta funcion es solo para Windows ya que usa las librerias en User32
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = (resolucion_ancho/2) - (self.frameSize().width()/2)
        top = (resolucion_alto/2) - (self.frameSize().height()/2)
        self.move(left, top)
        """

        #Asignar un tipo de fuente 
        qfont = QFont("FreeMono", 14)
        self.setFont(qfont)

        #Para asignar colores se puede usar css
        self.boton_Start.setStyleSheet("background-color: black; color: #fff; font-size 14")

        #Como modificar objetos en especifico
        #self.nombre_del_objeto.Funcion()

        #Evento para mensaje de bienvenida
        def showEvent(self, event):
            self.StartedMessage.setText("Como estas?")

        #Evento para cuando se cierre el programa
        def closeEvent(self, event):
            resultado = QMessageBox.question(self, "Salir....", "Muchas gracias por usar la aplicacion.\nCreada por Jorge Arguello\nUnidad Educativa Pompeya\nPrimero Bachillerato Sistemas", QMessageBox.Yes | QMessageBox.No)
            
            """Tengo que usar un Desktop porque en Qtile no mata la aplicacion no la cierra del todo"""
            #Aqui se decide lo que a presiona el usuario
            if resultado == QMessageBox.Yes:
                event.acept()

            #Si el usuario presina no pues no sales del programa
            else:
                event.ignore()


       


#Instancia para iniciar el programa
app = QApplication(sys.argv)
#Crear un objeto que contenga la clase
_ventana = Ventana()
#Mostrar ventana
_ventana.show()
#Ejecuta la aplicacion
app.exec_()
