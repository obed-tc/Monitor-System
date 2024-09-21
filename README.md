# Monitor System
![image](https://github.com/user-attachments/assets/bbfb7f55-fa1f-4add-94d4-a857e4b3a43f)

## Descripción

Este script monitorea en tiempo real el uso de recursos de tu PC, como la **CPU**, la **memoria RAM** y el **disco**. Proporciona una interfaz visual en la terminal, mostrando barras de progreso y alertas cuando el uso de los recursos supera ciertos umbrales. Además, guarda un registro de los valores en un archivo de log para un análisis posterior.

## Características

- Monitorea el uso de **CPU**, **memoria RAM** y **disco**.
- Muestra barras de progreso para una visualización clara del uso de recursos.
- Envía alertas cuando el uso de CPU, memoria o disco supera el **90%**.
- Registra el estado del sistema en un archivo de log (`resource_monitor.log`).
- Actualiza la información cada **5 segundos**.

## Requisitos

Este script utiliza las siguientes bibliotecas de Python:

- `psutil`: Para obtener las estadísticas de recursos del sistema.
- `colorama`: Para darle formato de colores a la salida en la terminal.

### Instalación de dependencias

Para instalar las dependencias, puedes utilizar pip:

```bash
pip install -r requirements.txt

```


### Instrucciones de Uso

Clona este repositorio o descarga el archivo principal.
```
git clone https://github.com/obed-tc/Monitor-System
```
Accede al directorio 

```
cd monitor-system
```

Para ejecutar el script

```
python3 main.py
```


### Visualización de datos:

Una vez iniciado, el script mostrará los siguientes datos en la terminal:

- Uso de CPU.
- Uso de Memoria RAM.
- Uso de Disco.
- Alertas si alguno de estos recursos excede el 90%.
Cada recurso tiene una barra de progreso que se actualiza automáticamente cada 5 segundos.


> Para detener el monitor de recursos, presiona Ctrl + C en la terminal.

### Logs:

El script guarda un log con las estadísticas de uso en el archivo `resource_monitor.log`, donde puedes revisar el uso de recursos con las fechas correspondientes.


### Personalización
Puedes modificar algunos aspectos del script para ajustarlo a tus necesidades:

**Intervalo de actualización:** 
> El script actualiza la información cada 5 segundos, pero puedes cambiar este valor modificando el argumento en time.sleep(5) dentro de la función monitor_resources().

**Umbrales de alerta:**
> Las alertas están configuradas para activarse cuando el uso de recursos supera el 90%, pero puedes ajustar este valor dentro de la función check_thresholds().

### Créditos
**Autor:** @obed-tc
**GitHub:** [@obed-tc](https://github.com/obed-tc)

> [!NOTE]  
> Este script está inspirado en la necesidad de monitorear el rendimiento de los recursos de manera eficiente y con un formato visual fácil de interpretar.
