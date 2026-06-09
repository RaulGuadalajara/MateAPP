# Guía de Instalación y Configuración - MateAPP

## Requisitos Previos

- Git instalado en tu máquina
- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Editor de código (Visual Studio Code recomendado)
- Conexión a Internet

## Instalación Local

### Paso 1: Clonar el Repositorio

```bash
# Clonar repositorio desde GitHub
git clone https://github.com/RaulGuadalajara/MateAPP.git

# Navegar al directorio del proyecto
cd MateAPP
```

### Paso 2: Verificar Ramas Disponibles

```bash
# Listar todas las ramas
git branch -a

# Deberías ver:
# main
# dev-desarrollo
# dev-diseno
```

### Paso 3: Seleccionar tu Rama de Trabajo

```bash
# Para desarrollo backend
git checkout dev-desarrollo

# O para diseño/frontend
git checkout dev-diseno
```

### Paso 4: Iniciar la Aplicación

```bash
# Para usar un servidor local simple (Python 3)
python -m http.server 8000

# O si usas Python 2
python -m SimpleHTTPServer 8000

# O usa Live Server en VS Code
# Extensión: Live Server de Ritwick Dey
```

### Paso 5: Acceder a la Aplicación

Abre tu navegador y ve a:
```
http://localhost:8000
```

## Configuración de Git

### Configurar Usuario Global

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Configurar Usuario Local (solo para este repositorio)

```bash
git config user.name "Tu Nombre"
git config user.email "tu@email.com"
```

## Flujo de Trabajo

### 1. Crear una Rama de Feature

```bash
# Actualizar rama base
git checkout dev-desarrollo
git pull origin dev-desarrollo

# Crear rama nueva
git checkout -b feat/nombre-descriptivo
```

### 2. Realizar Cambios

```bash
# Ver archivos modificados
git status

# Agregar cambios específicos
git add ruta/del/archivo

# O agregar todos los cambios
git add .
```

### 3. Hacer Commits Descriptivos

```bash
# Commit con título y descripción
git commit -m "feat: Descripción clara del cambio

- Detalle 1
- Detalle 2"
```

### 4. Hacer Push

```bash
git push origin feat/nombre-descriptivo
```

### 5. Crear Pull Request

- Ve a GitHub
- Click en "Compare & pull request"
- Completa la descripción del PR
- Solicita revisión de otro integrante
- Espera aprobación
- Mergea a `dev-desarrollo` o `dev-diseno`

### 6. Actualizar tu Rama Local

```bash
git checkout dev-desarrollo
git pull origin dev-desarrollo
```

## Comandos Git Útiles

### Ver Historial de Commits

```bash
# Ver últimos 10 commits
git log --oneline -10

# Ver commits de un usuario
git log --author="Nombre"

# Ver commits de un archivo
git log -- app/controllers/loginController.js
```

### Ver Cambios

```bash
# Ver cambios no staged
git diff

# Ver cambios staged
git diff --staged

# Ver diferencia entre ramas
git diff dev-desarrollo..dev-diseno
```

### Deshacer Cambios

```bash
# Descartar cambios en archivo
git checkout -- app/css/style.css

# Descartar todos los cambios
git reset --hard HEAD

# Deshacer último commit (local)
git reset --soft HEAD~1
```

### Fusionar Ramas

```bash
# Mergear rama de feature a dev-desarrollo
git checkout dev-desarrollo
git merge feat/nombre-descriptivo

# Con rebase (mantiene historia limpia)
git rebase dev-desarrollo
```

## Resolución de Conflictos

### Cuando ocurre un conflicto

```bash
# Ver archivos con conflicto
git status

# El archivo mostrará algo como:
<<<<<<< HEAD
Código actual
=======
Código entrante
>>>>>>> rama
```

### Pasos para resolver

1. Abre el archivo en tu editor
2. Elige cuál código mantener
3. Elimina marcadores (`<<<<`, `====`, `>>>>`)
4. Guarda el archivo
5. Ejecuta:

```bash
git add archivo_resuelto
git commit -m "fix: Resolver conflicto de merge en archivo_resuelto"
```

## Estructura de Carpetas para Desarrollo

```
MateAPP/
├── app/
│   ├── controllers/
│   ├── services/
│   ├── views/
│   ├── css/
│   └── img/
├── docs/              # Documentación
├── tests/             # Pruebas (futuro)
└── node_modules/      # Dependencias (si aplica)
```

## Herramientas Recomendadas

### IDE / Editores
- **Visual Studio Code** - Ligero y poderoso
- **WebStorm** - Especializado en web
- **Sublime Text** - Rápido y simple

### Extensiones VS Code
- Live Server
- Git Graph
- Prettier
- ESLint
- HTML CSS Support

### Navegadores para Testing
- Chrome DevTools
- Firefox Developer Edition
- Safari Developer Tools

## Troubleshooting

### Problema: "Git command not found"
```bash
# Instalar Git
# Windows: Descargar desde git-scm.com
# macOS: brew install git
# Linux: sudo apt install git
```

### Problema: "Permission denied"
```bash
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu@email.com"

# Agregar clave a GitHub en Settings > SSH Keys
```

### Problema: "Your branch is ahead of origin/main"
```bash
# Hacer push de tus cambios
git push origin rama-actual
```

### Problema: "Cannot delete branch main"
```bash
# Cambiar a otra rama primero
git checkout dev-desarrollo

# Luego intentar eliminar
git branch -d nombre-rama
```

## Contacto y Soporte

Para problemas o dudas:
- Contactar al **Documentador**: Rodrigo Vargas
- **Líder del proyecto**: Misael Villegas
- **Integrador**: Jesus Alejandro

---

**Actualizado:** 9 de junio de 2026  
**Versión:** 1.0.0  
**Aplicable a:** MateAPP v1.0.0+
