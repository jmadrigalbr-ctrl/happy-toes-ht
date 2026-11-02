# Happy Toes HT — Personalizaciones del ERP

Aplicación propia de Happy Toes para el sitio del ERP (Frappe Cloud, bench privado «Happy Toes»).
Se instala desde Frappe Cloud: Bench → Apps → Add App → Add from GitHub (repositorio público, rama `main`) y después Sitio → Apps → Install App.

## Qué hace hoy (v0.1.0)

Neutraliza UNA sola validación de fábrica de la app `healthcare` (Marley):
`PatientAppointment.validate_based_on_appointments_for()` rechazaba con
`DuplicateEntryError` la segunda cita del mismo paciente, en la misma sucursal, el mismo día.

Regla de Jorge (2026-11-01): dos servicios en una visita = DOS citas registradas,
una por servicio, contiguas. La sobrescritura (`overrides/patient_appointment.py`)
deja pasar únicamente ese error exacto («Patient already has an appointment…» /
«ya tiene una cita…»); cualquier otra validación del sistema sigue intacta.

## Reversa

Sitio → Apps → Uninstall App «happy_toes_ht». Sin la app, el candado de fábrica vuelve solo.

## Prueba tras instalar (obligatoria)

1. Paciente sintético: cita 1 (Pedicure Médico, 10:00, Tijuana Centro, fecha futura) → debe crear.
2. Al mismo paciente: cita 2 (Valoración Láser, 11:00, misma sucursal y fecha) → debe crear (antes: 409).
3. Editar la cita 2 (cambiar la hora) y guardarla → debe guardar (antes: 409).
4. Una cita normal con un dato obligatorio vacío → debe seguir rechazando (las demás validaciones viven).
5. Borrar los registros sintéticos (citas, contacto, paciente, cliente).
