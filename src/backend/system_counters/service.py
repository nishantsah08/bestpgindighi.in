from sqlalchemy.orm import Session
from . import models

def get_next_svh_id(db: Session) -> int:
    counter = db.query(models.SystemCounter).filter(models.SystemCounter.counter_name == "contact_svh_id").with_for_update().first()
    if not counter:
        counter = models.SystemCounter(counter_name="contact_svh_id", current_value=1)
        db.add(counter)
    else:
        counter.current_value += 1
    db.commit()
    return counter.current_value
