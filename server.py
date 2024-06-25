from flask import Flask, request, redirect, url_for, send_from_directory
import os

# autor i-100-user

greenColour = "\033[0;32m\033[1m"
endColour = "\033[0m\033[0m"
redColour = "\033[0;31m\033[1m"
blueColour = "\033[0;34m\033[1m"
yellowColour = "\033[0;33m\033[1m"
purpleColour = "\033[0;35m\033[1m"
turquoiseColour = "\033[0;36m\033[1m"
grayColour = "\033[0;37m\033[1m"

os.system("cls")

def __x__():
    x = f"""{yellowColour}

                                                        
                                                        
 >===>    >==>    >> >==> >=>     >=>   >==>    >> >==> 
>=>     >>   >=>   >=>     >=>   >=>  >>   >=>   >=>    
  >==>  >>===>>=>  >=>      >=> >=>   >>===>>=>  >=>    
    >=> >>         >=>       >=>=>    >>         >=>    
>=> >=>  >====>   >==>        >=>      >====>   >==>    
                                                        

                                        
{endColour}       
"""
    # Imprimir el mensaje
    print(x)

# Llamar a la función
__x__()


# Configuración de la carpeta donde se guardarán los archivos subidos
UPLOAD_FOLDER = './uploads'
# Extensiones permitidas para los archivos subidos
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Creación de la aplicación Flask
app = Flask(__name__)
# Configuración de Flask para usar la carpeta de subida
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Función para verificar si el archivo tiene una extensión permitida
def allowed_file(filename):
    # Verifica si el archivo tiene una extensión y si está en la lista de permitidas
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ruta principal para subir archivos
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica si la solicitud POST tiene la parte del archivo
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # Si no se seleccionó ningún archivo
        if file.filename == '':
            return 'No selected file'
        # Si el archivo es permitido, se guarda en la carpeta de subida
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File successfully uploaded'
    # Formulario HTML para subir archivos
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

# Ruta para acceder a los archivos subidos
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Envía el archivo desde la carpeta de subida
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    # Crea la carpeta de subida si no existe
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    # Ejecuta la aplicación Flask en todas las interfaces disponibles en el puerto 80
    app.run(host='0.0.0.0', port=80)
