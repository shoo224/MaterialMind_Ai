import os
import tempfile

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from db.database import get_db
from services.ingestion.ingestion_service import ingest_materials


router = APIRouter(
    prefix="/api/ingestion",
    tags=["Data Ingestion"]
)


@router.post("/materials")
async def upload_materials(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.filename or not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported"
        )

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".csv"
        ) as temp_file:

            temp_file.write(await file.read())
            temp_path = temp_file.name

        inserted_count = ingest_materials(
            temp_path,
            db
        )

        return {
            "message": "Materials ingested successfully",
            "inserted": inserted_count
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Failed to ingest materials"
        )

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)