# 📌 Project: Tasks Dashboard

## 🎯 Objetivo

Construir un dashboard web para gestionar tareas (CRUD) consumiendo una API existente.

---

## 📡 API

La API ya está implementada.

Documentación disponible en:

- OpenAPI: `/docs/openapi.json`
- Documentación legible: `/docs/API.md`

👉 El modelo debe usar estas fuentes como **única verdad** sobre endpoints, payloads y respuestas.

---

## ⚙️ Alcance

El dashboard debe permitir:

- Crear tareas
- Listar tareas
- Filtrar tareas por estado
- Actualizar tareas
- Eliminar tareas

---

## 📌 Reglas importantes

- No inventar endpoints
- No asumir campos que no estén en la documentación
- No modificar el contrato de la API
- No agregar lógica backend (solo frontend)

---

## 🧠 Consumo de API

- Usar los endpoints exactamente como están definidos en OpenAPI
- Respetar tipos de datos y estructura de payloads
- Manejar errores básicos (422, 404, etc.)

---

## 🎨 UI (simple)

- Tabla de tareas
- Formulario para crear/editar
- Botones para editar y eliminar
- Filtro por estado

---

## 🚫 Fuera de alcance

- Autenticación
- Roles/usuarios
- Backend adicional
- Persistencia local fuera de la API

---

## 💡 Nota

Si hay dudas sobre la API, priorizar siempre:

> `/docs/openapi.json` sobre cualquier otra fuente