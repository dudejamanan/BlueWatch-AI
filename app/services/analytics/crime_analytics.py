from sqlalchemy import extract, func
from sqlalchemy.orm import Session

from app.database.models.accused import Accused
from app.database.models.arrest_surrender import ArrestSurrender
from app.database.models.case_master import CaseMaster
from app.database.models.case_status_master import CaseStatus
from app.database.models.crime_head import CrimeHead
from app.database.models.unit import Unit
from app.database.models.victim import Victim


class CrimeAnalytics:

    @staticmethod
    def total_cases(db: Session):
        return db.query(
            func.count(CaseMaster.CaseMasterID)
        ).scalar()

    @staticmethod
    def monthly_trend(db: Session):
        return (
            db.query(
                extract("year", CaseMaster.CrimeRegisteredDate).label("year"),
                extract("month", CaseMaster.CrimeRegisteredDate).label("month"),
                func.count(CaseMaster.CaseMasterID).label("cases"),
            )
            .group_by(
                extract("year", CaseMaster.CrimeRegisteredDate),
                extract("month", CaseMaster.CrimeRegisteredDate),
            )
            .order_by(
                extract("year", CaseMaster.CrimeRegisteredDate),
                extract("month", CaseMaster.CrimeRegisteredDate),
            )
            .all()
        )

    @staticmethod
    def cases_by_police_station(db: Session):
        return (
            db.query(
                Unit.UnitName.label("police_station"),
                func.count(CaseMaster.CaseMasterID).label("cases"),
            )
            .join(
                CaseMaster,
                CaseMaster.PoliceStationID == Unit.UnitID,
            )
            .group_by(Unit.UnitName)
            .order_by(
                func.count(CaseMaster.CaseMasterID).desc()
            )
            .all()
        )

    @staticmethod
    def crime_head_distribution(db: Session):
        return (
            db.query(
                CrimeHead.CrimeGroupName,
                func.count(CaseMaster.CaseMasterID).label("cases"),
            )
            .join(
                CaseMaster,
                CaseMaster.CrimeMajorHeadID == CrimeHead.CrimeHeadID,
            )
            .group_by(CrimeHead.CrimeGroupName)
            .order_by(
                func.count(CaseMaster.CaseMasterID).desc()
            )
            .all()
        )

    @staticmethod
    def case_status_distribution(db: Session):
        return (
            db.query(
                CaseStatus.CaseStatusName,
                func.count(CaseMaster.CaseMasterID).label("cases"),
            )
            .join(
                CaseMaster,
                CaseMaster.CaseStatusID == CaseStatus.CaseStatusID,
            )
            .group_by(CaseStatus.CaseStatusName)
            .order_by(
                func.count(CaseMaster.CaseMasterID).desc()
            )
            .all()
        )

    @staticmethod
    def victim_gender_distribution(db: Session):
        return (
            db.query(
                Victim.GenderID,
                func.count(Victim.VictimMasterID).label("count"),
            )
            .group_by(Victim.GenderID)
            .order_by(Victim.GenderID)
            .all()
        )

    @staticmethod
    def accused_gender_distribution(db: Session):
        return (
            db.query(
                Accused.GenderID,
                func.count(Accused.AccusedMasterID).label("count"),
            )
            .group_by(Accused.GenderID)
            .order_by(Accused.GenderID)
            .all()
        )

    @staticmethod
    def victim_age_distribution(db: Session):
        return (
            db.query(
                Victim.AgeYear,
                func.count(Victim.VictimMasterID).label("count"),
            )
            .group_by(Victim.AgeYear)
            .order_by(Victim.AgeYear)
            .all()
        )

    @staticmethod
    def accused_age_distribution(db: Session):
        return (
            db.query(
                Accused.AgeYear,
                func.count(Accused.AccusedMasterID).label("count"),
            )
            .group_by(Accused.AgeYear)
            .order_by(Accused.AgeYear)
            .all()
        )

    @staticmethod
    def police_victim_cases(db: Session):
        return (
            db.query(
                func.count(Victim.VictimMasterID)
            )
            .filter(
                Victim.VictimPolice.is_(True)
            )
            .scalar()
        )

    @staticmethod
    def arrest_statistics(db: Session):
        return db.query(
            func.count(ArrestSurrender.ArrestSurrenderID)
        ).scalar()

    @staticmethod
    def arrests_by_police_station(db: Session):
        return (
            db.query(
                Unit.UnitName,
                func.count(ArrestSurrender.ArrestSurrenderID).label("arrests"),
            )
            .join(
                ArrestSurrender,
                ArrestSurrender.PoliceStationID == Unit.UnitID,
            )
            .group_by(Unit.UnitName)
            .order_by(
                func.count(ArrestSurrender.ArrestSurrenderID).desc()
            )
            .all()
        )

    @staticmethod
    def repeat_offenders(db: Session):
        return (
            db.query(
                Accused.PersonID,
                func.count(Accused.CaseMasterID).label("cases"),
            )
            .group_by(Accused.PersonID)
            .having(
                func.count(Accused.CaseMasterID) > 1
            )
            .order_by(
                func.count(Accused.CaseMasterID).desc()
            )
            .all()
        )

    @staticmethod
    def top_repeat_offenders(db: Session, limit: int = 10):
        return (
            db.query(
                Accused.PersonID,
                Accused.AccusedName,
                func.count(Accused.CaseMasterID).label("cases"),
            )
            .group_by(
                Accused.PersonID,
                Accused.AccusedName,
            )
            .having(
                func.count(Accused.CaseMasterID) > 1
            )
            .order_by(
                func.count(Accused.CaseMasterID).desc()
            )
            .limit(limit)
            .all()
        )

    @staticmethod
    def cases_registered_today(db: Session):
        from datetime import date

        return (
            db.query(
                func.count(CaseMaster.CaseMasterID)
            )
            .filter(
                CaseMaster.CrimeRegisteredDate == date.today()
            )
            .scalar()
        )

    @staticmethod
    def yearly_trend(db: Session):
        return (
            db.query(
                extract("year", CaseMaster.CrimeRegisteredDate).label("year"),
                func.count(CaseMaster.CaseMasterID).label("cases"),
            )
            .group_by(
                extract("year", CaseMaster.CrimeRegisteredDate)
            )
            .order_by(
                extract("year", CaseMaster.CrimeRegisteredDate)
            )
            .all()
        )