import frappe
from healthcare.healthcare.doctype.patient_appointment.patient_appointment import (
	PatientAppointment,
)

# Fragmentos del mensaje de fábrica que se neutraliza, en inglés (idioma de la
# sesión del API) y en español (idioma del escritorio). El error trae el folio
# de la cita existente entre etiquetas HTML; ambos fragmentos identifican
# únicamente el candado «otra cita del mismo paciente, misma sucursal, mismo día».
_FRAGMENTOS_CANDADO = (
	"Patient already has an appointment",
	"ya tiene una cita",
)


class CustomPatientAppointment(PatientAppointment):
	"""Permite varias citas del mismo paciente el mismo día en la misma sucursal.

	Regla de Jorge (2026-11-01): cuando una visita trae dos servicios, se
	registra CADA servicio como su propia cita. La validación de fábrica
	lo impedía; aquí se deja pasar solo ese rechazo exacto y cualquier
	otro error de la validación original sigue su curso.
	"""

	def validate_based_on_appointments_for(self):
		try:
			super().validate_based_on_appointments_for()
		except frappe.DuplicateEntryError as exc:
			if not any(fragmento in str(exc) for fragmento in _FRAGMENTOS_CANDADO):
				raise
