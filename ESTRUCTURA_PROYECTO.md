# Estructura del Proyecto MateAPP

## Descripción General

MateAPP es una aplicación web educativa para el aprendizaje de matemáticas. La estructura sigue un patrón MVC (Model-View-Controller) con AngularJS como framework frontend.

## Árbol de Directorios

```
MateAPP/
├── index.html                 # Archivo HTML principal
├── README.md                  # Documentación principal
├── CONTRIBUCION.md           # Guía de contribución
├── CHANGELOG.md              # Historial de cambios
├── COMMITS_LOG.md            # Registro de commits
├── ESTRUCTURA_PROYECTO.md    # Este archivo
│
└── app/                       # Carpeta principal de la aplicación
    ├── app.module.js         # Módulo principal de AngularJS
    ├── app.routes.js         # Configuración de rutas
    │
    ├── controllers/          # Controladores de AngularJS
    │   ├── loginController.js        # Lógica de autenticación
    │   ├── homeController.js         # Lógica de página principal
    │   └── exerciseController.js     # Lógica de ejercicios
    │
    ├── services/             # Servicios compartidos
    │   ├── authService.js           # Servicio de autenticación
    │   ├── exerciseService.js       # Servicio de ejercicios
    │   └── userService.js           # Servicio de usuario
    │
    ├── views/                # Vistas HTML (plantillas)
    │   ├── login.html               # Página de login
    │   ├── home.html                # Página principal
    │   └── exercises.html           # Página de ejercicios
    │
    ├── css/                  # Estilos CSS
    │   ├── style.css                # Estilos principales
    │   ├── responsive.css           # Media queries
    │   └── animations.css           # Animaciones
    │
    └── img/                  # Imágenes y assets
        ├── logo.png
        ├── icons/
        └── backgrounds/
```

## Descripción de Componentes

### Archivos Raíz

| Archivo | Propósito |
|---------|-----------|
| `index.html` | Punto de entrada de la aplicación |
| `README.md` | Documentación principal y objetivos |
| `CONTRIBUCION.md` | Guía para contribuyentes |
| `CHANGELOG.md` | Historial de versiones |

### Carpeta `/app`

#### `app.module.js`
Define el módulo principal de AngularJS y sus dependencias.
```javascript
angular.module('mathApp', ['ngRoute'])
```

#### `app.routes.js`
Configura las rutas de la aplicación:
- `/login` - Página de autenticación
- `/home` - Página principal
- `/exercises` - Módulo de ejercicios

### `/app/controllers`

**loginController.js**
- Validación de credenciales
- Autenticación de usuario
- Redirección post-login

**homeController.js**
- Información del usuario
- Acceso a módulos
- Estadísticas generales

**exerciseController.js**
- Generación de ejercicios
- Validación de respuestas
- Cálculo de puntuación

### `/app/services`

**authService.js**
- Gestión de tokens
- Verificación de autenticación
- Logout

**exerciseService.js**
- Generación de problemas
- Cálculo de respuestas
- Almacenamiento de resultados

**userService.js**
- Datos del usuario
- Estadísticas
- Configuraciones

### `/app/css`

**style.css** - Estilos principales
- Colores corporativos
- Tipografía
- Componentes base

**responsive.css** - Diseño adaptable
- Breakpoints para mobile, tablet, desktop
- Flexbox y Grid

**animations.css** - Efectos visuales
- Transiciones suaves
- Animaciones de carga
- Interacciones

## Tecnologías Utilizadas

### Frontend
- **HTML5** - Estructura semántica
- **CSS3** - Estilos y responsive design
- **JavaScript (ES5)** - Lógica de negocio
- **AngularJS 1.8** - Framework web

### Herramientas
- **Git** - Control de versiones
- **GitHub** - Repositorio remoto
- **Markdown** - Documentación

## Flujo de Datos

```
Usuario → Formulario → Controller → Service → API
                                    ↓
                            Local Storage / Backend
                                    ↑
Respuesta ← Vista ← Controller ← Service ← Datos
```

## Convenciones de Nomenclatura

### Archivos
- Controllers: `*Controller.js`
- Services: `*Service.js`
- Vistas: `*.html` (nombre descriptivo)
- Estilos: `*.css`

### Variables y Funciones
- camelCase para variables y funciones
- UPPERCASE para constantes
- $scope para objetos de AngularJS

### Ramas Git
- `main` - Rama de producción
- `dev-desarrollo` - Desarrollo backend
- `dev-diseno` - Desarrollo frontend
- `feat/*` - Nuevas funcionalidades

## Estándares de Código

### HTML
- Indentación: 2 espacios
- Tags cerrados correctamente
- Atributos en minúsculas

### CSS
- BEM (Block Element Modifier) para clases
- Mobile-first approach
- Variables CSS donde sea posible

### JavaScript
- Punto y coma al final de líneas
- Comments en español
- Funciones documentadas con JSDoc

## Escalabilidad Futura

Se plantea migrar a:
- **Angular** (versión moderna)
- **TypeScript** - Tipado estático
- **RxJS** - Programación reactiva
- **Backend API** - Node.js / Express
- **Base de Datos** - MongoDB / PostgreSQL

---

**Última Actualización:** 9 de junio de 2026  
**Responsable:** Equipo de Desarrollo MateAPP  
**Versión:** 1.0.0
