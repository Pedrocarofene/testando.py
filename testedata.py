print("teste data")

from datetime  import datetime

data_namoro = datetime(2025,3,22) #ano #mes #data

data_atual = datetime.today()

data_usuario = input ("qual a data de namoro de Monyke e Pedro? (dd/mm/aaaa): ")
data_usuario = datetime.strptime(data_usuario, "%d/%m/%Y")

if data_usuario == data_namoro:
    print ("você acertou!!😄❤️")
else:
    print ("você errou!!!😡")