# Guía de Contribución - MateAPP

## Estándares de Commits

Este documento establece las mejores prácticas para realizar commits en el proyecto MateAPP.

### Formato de Mensaje de Commit

**Línea 1 (Asunto):**
```
[TIPO] Descripción clara en imperativo (máx 50 caracteres)
```

**Líneas 2+ (Cuerpo - opcional):**
```
Explicación más detallada de los cambios realizados.
Explicar por qué se realizaron los cambios, no qué se cambió.

- Punto 1 de cambio
- Punto 2 de cambio
```

### Tipos de Commits

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **feat** | Nueva funcionalidad | `feat: Agregar validación de email en formulario` |
| **fix** | Corrección de error | `fix: Corregir error de validación en login` |
| **refactor** | Cambio de código sin afectar funcionalidad | `refactor: Simplificar lógica de autenticación` |
| **style** | Cambios de estilos CSS o formato | `style: Mejorar diseño responsivo de navbar` |
| **docs** | Cambios de documentación | `docs: Actualizar README con instrucciones` |
| **test** | Agregación de tests | `test: Agregar pruebas unitarias a authService` |
| **chore** | Tareas de mantenimiento | `chore: Actualizar dependencias de npm` |

### Ejemplos de Buenos Commits

#### ✅ Correcto
```
feat: Implementar sistema de autenticación con JWT

- Crear servicio de autenticación
- Validar credenciales contra base de datos
- Generar y verificar tokens
- Establecer tiempo de expiración
```

#### ✅ Correcto
```
fix: Corregir error de validación en formulario de registro

El validador de email no aceptaba direcciones válidas 
con dominio .co. Se actualizo la expresión regular.
```

#### ❌ Incorrecto
```
fix bug
```

#### ❌ Incorrecto
```
Hice cambios en varios archivos
```

#### ❌ Incorrecto
```
actualizaciones
```

### Flujo de Trabajo

1. **Crear rama de feature** desde `dev-desarrollo` o `dev-diseno`
   ```bash
   git checkout -b feat/nombre-descriptivo
   ```

2. **Realizar cambios** con commits descriptivos
   ```bash
   git commit -m "feat: Agregar nueva funcionalidad"
   ```

3. **Hacer push** a la rama
   ```bash
   git push origin feat/nombre-descriptivo
   ```

4. **Crear Pull Request** con descripción detallada

5. **Revisión de código** por otro integrante

6. **Merge** a rama de desarrollo

7. **Release** a main cuando esté listo

### Checklist antes de Commit

- [ ] Código compilado y sin errores
- [ ] Cambios probados localmente
- [ ] Archivo `.gitignore` actualizado (si aplica)
- [ ] Mensajes de commit descriptivos
- [ ] No incluye cambios sin relación
- [ ] Archivos no necesarios excluidos (node_modules, .env, etc.)

---

**Actualizado:** 9 de junio de 2026  
**Responsable:** Equipo de desarrollo MateAPP
