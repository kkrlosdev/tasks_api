# 📌 Tasks API

API REST para gestión de tareas.

---

## 🔹 Health Check

### GET `/`
Verifica que la API está activa.

**Response 200**
```json
{}
```

---

## 🔹 Obtener tareas

### GET `/tasks`

Obtiene todas las tareas. Permite filtrar por estado.

**Query params**
- `status` (int, opcional)

**Ejemplo**
```bash
GET /tasks?status=1
```

**Response 200**
```json
[]
```

---

## 🔹 Crear tarea

### POST `/tasks`

Crea una nueva tarea.

**Body**
```json
{
  "name": "Tarea 1",
  "begin_date": "18-03-2026",
  "end_date": "20-03-2026",
  "short_description": "Descripción corta",
  "long_description": "Descripción larga",
  "status": 1
}
```

**Response 200**
```json
{}
```

---

## 🔹 Actualizar tarea

### PUT `/tasks/{id}`

Actualiza completamente una tarea.

**Path param**
- `id` (int)

**Body**
```json
{
  "id": 1,
  "name": "Tarea actualizada",
  "begin_date": "18-03-2026",
  "end_date": "20-03-2026",
  "short_description": "Nueva descripción corta",
  "long_description": "Nueva descripción larga",
  "status": 2
}
```

**Response 200**
```json
{}
```

---

## 🔹 Eliminar tarea

### DELETE `/tasks/{id}`

Elimina una tarea por ID.

**Path param**
- `id` (int)

**Response**
- `204` → eliminado
- `404` → no existe

---

## ⚠️ Errores

### 422 Validation Error
Error de validación en request.

```json
{
  "detail": [
    {
      "loc": ["body", "field"],
      "msg": "error",
      "type": "validation_error"
    }
  ]
}
```

# Contratos de la API

- **El formato de fechas debe ser siempre DD-MM-YYYY. Ejemplo: 17-03-2020**