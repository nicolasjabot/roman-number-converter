from fastapi import FastAPI, HTTPException, Query
from roman_cli import to_int_logic, to_roman_logic
from errors import RomanFormatError, ArabicRangeError, NumberError
from postgresql_db import get_connection

app = FastAPI()

@app.on_event("startup")
def init_db():
    with get_connection() as (conn, cur):
        cur.execute("""
            CREATE TABLE IF NOT EXISTS conversion_logs (
                id SERIAL PRIMARY KEY,
                input_value TEXT NOT NULL,
                result_value TEXT NOT NULL,
                conversion_direction TEXT NOT NULL,
                timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

# ------------------------------------------------------------------------------
@app.post("/to-int")
def to_int_endpoint(roman: str = Query(..., description="Roman numeral to convert")):
    try:
        result = to_int_logic(roman)
        return {"value": int(result)}
    except RomanFormatError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except NumberError as exc:
        raise HTTPException(status_code=422, detail=str(exc))

# ------------------------------------------------------------------------------
@app.post("/to-roman")
def to_roman_endpoint(number: int = Query(..., description="Integer to convert")):
    try:
        result = to_roman_logic(number)
        return {"value": result}
    except ArabicRangeError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except NumberError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
