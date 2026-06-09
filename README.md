# 📚 MateAPP - Aplicación de Educación Matemática

## 🎯 Objetivo del Proyecto

MateAPP es una aplicación web interactiva diseñada para facilitar el aprendizaje de matemáticas de manera didáctica y accesible. El objetivo principal es proporcionar a estudiantes una plataforma donde puedan:

- Practicar ejercicios matemáticos de diferentes niveles de dificultad
- Acceder a contenido educativo estructurado y bien organizado
- Obtener retroalimentación inmediata sobre su desempeño
- Mejorar sus habilidades matemáticas a través de una experiencia interactiva y amigable

## 👥 Integrantes y Roles

| Integrante | Rol |
|-----------|-----|
| Raúl Guadalajara | Desarrollador Full Stack | 
| Jesus Alejandro | Integrador | 
| Misael Villegas | Lider | 
| Fany Salas | Diseñador | 
| Rodrigo Vargas | Documentador | 

## 🔄 Flujo de Trabajo Utilizado

### Estructura de Ramas

El proyecto utiliza un modelo de ramas para organizar el desarrollo:

```
main (Rama principal - Producción)
├── dev-desarrollo (Rama de desarrollo - Funcionalidades backend)
└── dev-diseno (Rama de diseño - Funcionalidades frontend y UI/UX)
```

### Descripción del Flujo

- **main**: Rama principal que contiene el código listo para producción
- **dev-desarrollo**: Rama dedicada al desarrollo de funcionalidades backend, lógica de negocio y APIs
- **dev-diseno**: Rama dedicada al diseño frontend, interfaz de usuario y experiencia del usuario (UI/UX)

### Proceso de Trabajo

1. Se crea una rama específica (`dev-desarrollo` o `dev-diseno`) desde `main`
2. Los cambios se desarrollan y prueban en la rama correspondiente
3. Una vez completados y validados, se integran a la rama principal mediante pull requests
4. La rama principal siempre contiene código estable y listo para usar

## 🛠️ Stack Tecnológico

- **Frontend**: HTML, CSS, JavaScript
- **Estructura**: 
  - JavaScript: 48.6%
  - HTML: 36.8%
  - CSS: 14.6%

## 📦 Instalación y Uso

```bash
# Clonar el repositorio
git clone https://github.com/RaulGuadalajara/MateAPP.git

# Navegar al directorio
cd MateAPP

# Trabajar en la rama correspondiente
git checkout dev-desarrollo  # Para desarrollo backend
# o
git checkout dev-diseno      # Para desarrollo frontend
```

## 📝 Notas

Este proyecto es una práctica educativa que implementa un flujo de trabajo profesional con ramificación de Git para mantener la organización y claridad en el desarrollo de funcionalidades.

---

**Desarrollado por:** Raúl Guadalajara  
**Tipo de Proyecto:** Aplicación Educativa  
**Año:** 2026
