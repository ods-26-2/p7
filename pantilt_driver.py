import time
from adafruit_servokit import ServoKit

class PanTilt:
    def __init__(self, channels: int = 16, pan_channel: int = 0, tilt_channel: int = 1):
        """Inicializa a controladora PCA9685 via barramento I2C."""
        self.kit = ServoKit(channels=channels)
        self.pan_ch = pan_channel
        self.tilt_ch = tilt_channel

        # Limites mecanicos de seguranca para evitar travamento físico dos servos
        self.PAN_MIN = 0.0
        self.PAN_MAX = 180.0
        self.TILT_MIN = 30.0
        self.TILT_MAX = 150.0

        # Posicao inicial ao ligar (Homing)
        self.home()

    def home(self):
        """Leva a camera para o centro neutro (90 graus em ambos os eixos)."""
        return self.set_angle(90.0, 90.0)

    def set_angle(self, pan: float, tilt: float):
        """
        Move os servos respeitando os limites mecanicos (clamping).
        Retorna os angulos reais aplicados.
        """
        clamped_pan = max(self.PAN_MIN, min(self.PAN_MAX, float(pan)))
        clamped_tilt = max(self.TILT_MIN, min(self.TILT_MAX, float(tilt)))

        self.kit.servo[self.pan_ch].angle = clamped_pan
        self.kit.servo[self.tilt_ch].angle = clamped_tilt

        return clamped_pan, clamped_tilt

if __name__ == "__main__":
    print("[TESTE] Inicializando e centralizando...")
    pt = PanTilt()
    time.sleep(1)

    print("[TESTE] Movendo Pan para 45°...")
    pt.set_angle(45.0, 90.0)
    time.sleep(1)

    print("[TESTE] Movendo Pan para 135° e Tilt para 60°...")
    pt.set_angle(135.0, 60.0)
    time.sleep(1)

    print("[TESTE] Retornando ao ponto zero (Homing)...")
    pt.home()
    print("[TESTE] Concluido com sucesso!")
