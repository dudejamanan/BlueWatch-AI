from fastapi import FastAPI
from app.core.logging import logger

from app.core.config import settings
from app.api.routes.root import router as root_router
from app.api.routes.health import router as health_router
from app.api.routes.state import router as state_router
from app.api.routes.district import router as district_router
from app.api.routes.unit_type import router as unit_type_router
from app.api.routes.unit import router as unit_router
from app.api.routes.rank import router as rank_router
from app.api.routes.designation import router as designation_router
from app.api.routes.employee import router as employee_router
from app.api.routes.act import router as act_router
from app.api.routes.section import router as section_router
from app.api.routes.crime_head import router as crime_head_router
from app.api.routes.crime_sub_head import router as crime_sub_head_router
from app.api.routes.crime_head_act_section import (
    router as crime_head_act_section_router,
)
from app.api.routes.case_category import router as case_category_router
from app.api.routes.gravity_offence import router as gravity_offence_router
from app.api.routes.occupation_master import router as occupation_master_router
from app.api.routes.religion_master import router as religion_master_router
from app.api.routes.caste_master import router as caste_master_router
from app.api.routes.case_status_master import router as case_status_master_router
from app.api.routes.court import router as court_router
from app.api.routes.case_master import router as case_master_router
from app.api.routes.victim import router as victim_router

from app.api.routes.accused import router as accused_router
from app.api.routes.complainant import router as complainant_router


app = FastAPI(
    title=settings.project_name,
    version=settings.api_version,
)
logger.info("BlueWatch API started successfully.")

app.include_router(root_router)
app.include_router(health_router)
app.include_router(state_router)
app.include_router(district_router)
app.include_router(unit_type_router)
app.include_router(unit_router)
app.include_router(rank_router)
app.include_router(designation_router)
app.include_router(employee_router)
app.include_router(act_router)
app.include_router(section_router)
app.include_router(crime_head_router)
app.include_router(crime_sub_head_router)
app.include_router(crime_head_act_section_router)
app.include_router(case_category_router)
app.include_router(gravity_offence_router)
app.include_router(occupation_master_router)
app.include_router(religion_master_router)
app.include_router(caste_master_router)
app.include_router(case_status_master_router)
app.include_router(court_router)
app.include_router(case_master_router)
app.include_router(victim_router)

app.include_router(accused_router)


app.include_router(complainant_router)