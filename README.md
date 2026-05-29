# Análisis Deportivo - TP OE

## 📋 Visión General del Proyecto
Este proyecto fue desarrollado con el objetivo de procesar y analizar estadísticamente los datos de rendimiento de un torneo deportivo. A través de scripts reproducibles en Python, el sistema automatiza la lectura de métricas de partidos y genera reportes visuales.

## Integrantes(ficcticios para cumplir con las consignas):
Nombre (utilizo los de la consigna) - ID de JIRA:
**Hugo (KAN-1) - Líder y Organizador:** Responsable del repositorio, estructura del entorno y documentación del proyecto.
**Paco (KAN-2) - Desarrollador Técnico:** Responsable del diseño algorítmico, procesamiento de datos y generación de gráficos estadísticos.
**Luis (KAN-3) - Revisor y QA:** Responsable del control de calidad del código, seguridad de credenciales, revisión por pares (Peer Review) y gestión del flujo de integración.

## Estructura del Repositorio:
**`/datos`:** Contiene los datos que seran usados para el analisis.(`datos_torneo.csv`).
**`/scripts`:** Aloja el código fuente ejecutable desarrollado en Python (`analisis.py`).
**`/resultados`:** Carpeta de salida donde se guardan los gráficos generados (`goles_por_equipo.png`).

## Requerimientos e Instalación:
El entorno de ejecución principal está diseñado para ejecutarse de forma transparente en Google Colab. 

### Requisitos previos de librerías en Python:
* pandas
* matplotlib
* seaborn

### Reproducibilidad de Rutas
El código de este proyecto está optimizado para ejecutarse sin depender de rutas absolutas locales. Todas las llamadas a archivos se realizan utilizando rutas relativas que conectan directamente las carpetas internas del repositorio:
* Lectura de datos: `../datos/datos_torneo.csv`
* Exportación de imágenes: `../resultados/goles_por_equipo.png`

---

## Trazabilidad del Desarrollo en Jira:
Para asegurar el vínculo mandatorio entre la gestión del proyecto y el código fuente, la célula utilizó el estándar **Conventional Commits** vinculando cada aporte al tablero de Jira. (Proyecto Analisis deportivo):
**Hugo KAN-1:** Inicialización de estructura de carpetas y documentación base.
**Paco KAN-2:** Implementación del script técnico de análisis y exportación de visualizaciones.
**Luis KAN-3:** Revisión de código, control de seguridad del token de acceso (PAT) y cierre de Pull Request.
