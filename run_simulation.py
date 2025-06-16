
import mujoco
import mujoco.viewer
import numpy as np
import time

# Cargar el modelo
model = mujoco.MjModel.from_xml_path("qube_servo.xml")
data = mujoco.MjData(model)

# Crear viewer interactivo
with mujoco.viewer.launch_passive(model, data) as viewer:
    print("Simulando Qube-Servo 3 (cerrar ventana para salir)...")
    start = time.time()
    while viewer.is_running():
        step_start = time.time()

        # Avanza la simulación
        mujoco.mj_step(model, data)

        # Pausa para mantener el tiempo real
        time.sleep(max(0, model.opt.timestep - (time.time() - step_start)))
