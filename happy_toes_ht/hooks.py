app_name = "happy_toes_ht"
app_title = "Happy Toes HT"
app_publisher = "Happy Toes"
app_description = "Personalizaciones del ERP de Happy Toes sobre Frappe/Healthcare"
app_email = "sistemas1@happy-toes.net"

required_apps = ["healthcare"]

# Regla de Jorge (2026-11-01): un paciente sí puede tener dos o más citas el
# mismo día en la misma sucursal (dos servicios en una visita = dos citas).
# La app healthcare (Marley) lo rechaza de fábrica en
# PatientAppointment.validate_based_on_appointments_for; esta clase
# sobrescrita neutraliza solo ese rechazo exacto.
override_doctype_class = {
	"Patient Appointment": "happy_toes_ht.overrides.patient_appointment.CustomPatientAppointment"
}
