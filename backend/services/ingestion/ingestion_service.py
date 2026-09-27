import pandas as pd
from sqlalchemy.orm import Session

from models.material import Material


REQUIRED_COLUMNS = {
    "material_code",
    "description",
    "category",
    "unit",
    "manufacturer",
    "supplier",
    "specification"
}


def ingest_materials(
    file_path: str,
    db: Session
) -> int:

    df = pd.read_csv(file_path)

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(sorted(missing_columns))}"
        )

    df = df.fillna("")

    inserted_count = 0

    for _, row in df.iterrows():

        material = Material(
            material_code=str(row["material_code"]).strip(),
            description=str(row["description"]).strip(),
            category=str(row["category"]).strip(),
            unit=str(row["unit"]).strip(),
            manufacturer=str(row["manufacturer"]).strip(),
            supplier=str(row["supplier"]).strip(),
            specification=str(row["specification"]).strip()
        )

        db.add(material)
        inserted_count += 1

    db.commit()

    return inserted_count