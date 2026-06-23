class RulesEngine:

    def evaluate(self, metrics):
        resultados = {}

        for parte, angulo in metrics.item():
            
            
            if angulo > 120:
                feedback = "Angulo del codo muy abierto"
            elif angulo < 90:
                feedback = "Angulo del codo muy cerrado"
            else:
                feedback = "Angulo del codo correcto"

            resultados[parte] = {
                "angulo": angulo,
                "correcto": check(angulo),
                "feedback": feedback
            }

        return resultados


def check(self, angle):
    return 90 <= angle <= 120