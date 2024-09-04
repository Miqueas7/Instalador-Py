from shutil import copyfile
import os
import sys

from tkinter import  messagebox  as  MessageBox
from tkinter import Tk

#Codigo para enlazar con el archivo .spec
def resolver_ruta(ruta_relativa):
    if hasattr(sys,'_MEIPASS'):
        return os.path.join(sys._MEIPASS,ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

def proceso_completo():
    user_root = os.path.expanduser("~")

    if not os.path.exists(os.path.join(user_root,"ShiftGamma")):
        os.mkdir(os.path.join(user_root,"ShiftGamma"))

    def generar_archivo(nombre,destino):
        copyfile(resolver_ruta(nombre),os.path.join(destino,nombre))

    generar_archivo("JR_COMPLEMENTO.xlam",os.path.join(user_root,"AppData/Roaming/Microsoft/AddIns"))
    generar_archivo("JR_COMPLEMENTO.xlsx",os.path.join(user_root,"ShiftGamma"))

def mensaje():
    ventana = Tk()
    ventana.withdraw()
    MessageBox.showinfo("SHIFT GAMMA","© JR GEOCONSULTORES E INGENIEROS S.R.L. \n         COMPLEMENTO GEOTÉCNICO \n                       Versión 1.0 \n         INSTALADO CORRECTAMENTE \n\n   Desarrollado por Miqueas Quintanilla")

def cargar_proceso_interfaz(): 
    while True:
        proceso_completo()
        mensaje()
        break

cargar_proceso_interfaz()