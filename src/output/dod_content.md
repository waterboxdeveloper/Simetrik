# Definition of Done - E137 - Data Normalization in Unions - Prueba Técnica

## 1. Objetivo de la Épica

1. Detener la inserción y propagación de registros con errores de casteo en una unión, evitando la generación de registros vacíos que afecten conciliaciones y reportes.
1. Generar una tabla intermedia a nivel de sistema que permita identificar los registros no insertados por errores en casteo, la columna afectada, el recurso padre del cual provienen los registros no insertados y el grupo conciliable de los mismos.
1. Implementar una interfaz de usuario que permita:
  - Editar el casteo de la columna con errores y reprocesar los registros.
  - Descartar los registros no procesados si el usuario lo desea.
  - Procesar los registros con errores en casteos con valores vacíos si el usuario lo elige.
## 2. Necesidad y contexto

Los usuarios enfrentan problemas con la carga y procesamiento de datos debido a errores de casteo, generando registros vacíos que afectan resultados de conciliaciones, exportaciones de datos y errores en la contabilizacion.

Actualmente, los implementadores recurren a prácticas subóptimas como castear todas las columnas a texto en la unión y luego ajustar en el spreadsheet, lo que va en contra de la normalización de formatos.

2.1. Problema actual

- Alto volumen de errores en cargas de datos: 30-40% de los tickets de soporte están relacionados con problemas de casteo.
- Impacto en usuarios clave: 5 comentarios recientes en NPS mencionan dificultades con cargas y procesamiento de datos. Clientes que han mencionado este problema incluyen: Ebanx, Hotmart, RecargaPay, PagBank.
- Prácticas manuales ineficientes: Un 20% de las uniones han agregado columnas manuales para corregir errores post-implementación.
- Inconsistencias en conciliaciones: Contabilidad errónea debido a registros vacíos inesperados.
- Exportaciones incorrectas: Archivos con valores NULL que no deberían estar vacíos.
## 3. Beneficio para nuestros usuarios 

- Reducción de errores: Se minimiza el riesgo de inconsistencias por reprocesos manuales.
- Ahorro de tiempo: Se elimina la necesidad de reconstruir manualmente configuraciones complejas en el sistema para dar solución a las inconsistencias de registros vacíos por errores en el casteo dentro de uniones.
- Mayor confiabilidad: no se propagarán registros que contengan información incompleta.
## 4. Glosario, Riesgo y valor de negocio 

Posibles riesgos del desarrollo:

- Impacto en el rendimiento: El proceso de eliminación y reinserción de registros puede ser intensivo en grandes datasets.
- Propagación incompleta de los cambios: Si el sistema no logra identificar correctamente todos los registros con estado Nulls.
# Gestiona inconsistencias de formatos en Uniones

## Objetivo

Evitar la inserción y propagación de registros vacíos producidos por errores de casteo dentro de una Unión y ofrecer a los usuarios una interfaz clara para revisar, corregir o descartar dichos registros.

> ¿Qué resuelve?

  - Reduce los errores de conciliación y exportación, derivados de valores null inesperados.
  - Ahorra tiempo al eliminar correcciones manuales en hojas de cálculo externas.
  - Aumenta la confiabilidad de los datos al impedir que se propaguen registros incompletos.
  ![](output/images/dod_image_1760820460.png)

---

## Explicación por pasos

| Paso | Acción |
| --- | --- |
| 1 | Desde el spreadsheet de la Unión, abre Editar configuración ▸ Gestionar inconsistencias. Si existen registros bloqueados, verás un indicador rojo. |
| 2 | Revisa la alerta que indica cuántas columnas presentan errores. |
| 3 | Haz clic en Gestionar formato junto a la columna afectada.
En el panel lateral elige: •Asignar nuevo formato • Procesar con errores • ó Descartar los registros |
| 4 | Presiona Reprocesar registros. |

![](output/images/dod_image_1760820461.png)

---

## Conoce los elementos clave de la Gestión de inconsistencias

| Elemento | Descripción |
| --- | --- |
| Vista de Gestión | Tabla que lista columnas con errores, su fuente, grupo conciliable y cantidad de registros bloqueados. |
| Panel lateral | Permite asignar nuevos casteos o decidir qué hacer con los registros afectados. |
| Preferencias de la Unión | Configuración general que define si se detiene la inserción de null o se permiten valores vacíos. |
| Roles autorizados | Solo Supervisor, Constructor o roles personalizados con permisos equivalentes pueden reprocesar los datos. |

---

## Domina el funcionamiento de la Gestión de inconsistencias

### ✅ Buenas prácticas

- Revisa con frecuencia el indicador de inconsistencias para evitar cuellos de botella.
- Define casteos precisos (p. ej. fecha, hora, moneda) durante la configuración inicial de la Unión.
- Coordina con tu equipo los horarios de reprocesamiento para minimizar bloqueos en trabajos dependientes.
### ❌ Evita

- Procesar con errores por defecto sin validar el impacto en conciliaciones.
- Castear todo a texto como solución rápida—afecta la normalización y dificulta reportes.
- Dejar columnas críticas sin preferencias explícitas; el comportamiento por defecto puede no ser el deseado.
---

## Requisitos Previos

- Contar con rol Supervisor o Constructor (o permisos equivalentes).
- La Unión debe estar configurada y tener al menos una fuente con registros nuevos.
- Haber habilitado la opción Gestionar inconsistencias manualmente si deseas detener la inserción de null.
## Consideraciones Adicionales

- Durante el reprocesamiento la Unión se bloquea hasta finalizar su ejecución; planifica ventanas de mantenimiento.
- Solo se soportan columnas fecha, hora y fecha‑hora en esta primera versión.
- Si persisten errores luego de reprocesar, la alerta volverá a mostrarse con la cantidad de registros restante por procesar.
## Preguntas Frecuentes

| Pregunta | Respuesta breve |
| --- | --- |
| ¿Puedo excluir una sola columna del bloqueo? | Sí. En Preferencias de la Unión ▸ Nivel columna define excepciones para permitir o bloquear null. |
| ¿Qué ocurre con las exportaciones programadas? | Los registros se incluyen solo después de un reprocesamiento exitoso. |
| ¿Qué pasa si cierro la vista sin reprocesar? | Los cambios se descartan y los registros permanecen bloqueados. |

## Contenido Relacionado

- Casteo de columnas en recursos
- Crear uniones de fuentes
