from pyowm.owm import OWM
owm = OWM('c0779d2b68b69ef6b733d5629c17506f')
reg = owm.city_id_registry()
print(reg.ids_for('London'))