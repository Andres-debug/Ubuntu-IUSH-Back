from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.prediction import StressPredictionInput, StressPredictionOutput
from typing import List

router = APIRouter()

def predict_stress_level(grades: List[float], attendance: List[str], hours: int) -> str:
    """
    Simula un modelo de predicción para el nivel de estrés basado en las notas,
    asistencia y horas de cada materia.
    """
    avg_grade = sum(grades) / len(grades) if grades else 0
    attendance_score = attendance.count("PRESENT") / len(attendance) if attendance else 0

    # Regla simple para predecir el nivel de estrés
    if avg_grade < 3.0 or attendance_score < 0.7 or hours > 40:
        return "ALTO"
    elif avg_grade < 4.0 or attendance_score < 0.9:
        return "MEDIO"
    return "BAJO"

@router.post("/predict-stress", response_model=StressPredictionOutput)
def predict_academic_stress(
    input_data: StressPredictionInput,
    db: Session = Depends(get_db),
):
    """
    Endpoint para predecir el nivel de estrés académico de un estudiante.
    
    - `input_data`: Datos de entrada que incluyen calificaciones, asistencia y horas totales.
    """
    if not input_data.grades or input_data.attendance < 0 or input_data.total_hours <= 0:
        raise HTTPException(status_code=400, detail="Datos insuficientes para realizar la predicción.")

    # Simulación de predicción
    avg_grade = sum(input_data.grades) / len(input_data.grades)
    stress_level = "ALTO" if avg_grade < 3.0 or input_data.attendance < 0.7 or input_data.total_hours > 40 else "BAJO"

    return StressPredictionOutput(
        stress_level=stress_level,
        confidence_score=0.85  # Valor simulado
    )