
# Backend Calculadora

¡Bienvenido al proyecto **Backend Calculadora**! Este repositorio contiene el código fuente de un sistema backend que realiza cálculos matemáticos y genera gráficos. Está diseñado para ser utilizado junto con el proyecto **Banco Calculadora**, el cual proporciona un frontend intuitivo para interactuar con este backend.

## 📖 Propósito del Proyecto

El propósito de **Backend Calculadora** es servir como la base lógica y computacional para aplicaciones que requieren cálculos avanzados y visualización gráfica. Junto con el proyecto relacionado **Banco Calculadora**, este sistema permite:

- Realizar cálculos financieros y matemáticos.
- Generar gráficos interactivos.
- Proporcionar una experiencia completa de backend y frontend.

---

## 📂 Estructura del Proyecto

El proyecto incluye los siguientes archivos y carpetas:

```
backend-calculadora-main/
├── app.py                 # Archivo principal de la aplicación
├── chart.py               # Generación de gráficos matemáticos
├── interes.py             # Cálculo de intereses matemáticos
├── requirements.txt       # Dependencias del proyecto
├── static/                # Recursos estáticos como imágenes generadas
│   └── grafico_funcion.png
├── .idea/                 # Configuración del entorno de desarrollo
├── __pycache__/           # Archivos compilados de Python
└── README.md              # Documentación del proyecto
```

---

## 🚀 Instrucciones de Uso

1. **Clonar el repositorio**:
   ```bash
   git clone <URL del repositorio>
   cd backend-calculadora-main
   ```

2. **Instalar dependencias**: Asegúrate de tener Python instalado y ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**: Inicia la aplicación con:
   ```bash
   python app.py
   ```

4. **Conectar con el frontend**: Usa el proyecto **Banco Calculadora** para interactuar con este backend.

---

## 🔗 Relación con Banco Calculadora

El proyecto **Banco Calculadora** sirve como el frontend de este backend. Los usuarios pueden interactuar con las funcionalidades de **Backend Calculadora** a través de la interfaz gráfica que ofrece **Banco Calculadora**. Asegúrate de seguir las instrucciones de configuración en ambos proyectos para una integración correcta.

---

## ❓ Preguntas Frecuentes

1. **¿Cómo configuro ambos proyectos para trabajar juntos?**  
   Ejecuta primero el backend con `python app.py`. Luego, abre el proyecto de frontend **Banco Calculadora** y actualiza las rutas en los archivos `.js` para apuntar al servidor donde está corriendo el backend.

---

¡Gracias por explorar el proyecto Backend Calculadora! 🚀
