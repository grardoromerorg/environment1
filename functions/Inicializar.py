import os

class Inicializar():
    # Directorio Base (buscar ruta abs del path donde se encuentra el archivo inicializar, dentro de funct)
    # en basedir, busca el archivo y genera una ruta "../..' es para q se eleve un nivel arriba.
    basedir = os.path.abspath(os.path.join(__file__, '../..'))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    Environment = 'Dev'

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'CHROME'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/Data.xlsx'

    if Environment == 'Dev':
        URL = 'https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp'
        User = 'grardo'
        Pass = 'gr4029'


    if Environment == 'Test':
        URL = 'https://www.despegar.com'
        User = 'grardo1'
        Pass = 'gr4029'