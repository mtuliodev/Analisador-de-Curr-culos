import uuid
from models.job import Job
from database import AnalyzeDatabase

database = AnalyzeDatabase()

name = 'DESCRIÇÃO DA VAGA'

activities = '''
ATIVIDADES
'''

prerequisites = '''
REQUISITOS
'''

differentials = '''
DIFERENCIAIS
'''

job = Job(
    id=str(uuid.uuid4()),
    name=name,
    main_activities=activities,
    prerequisites=prerequisites,
    differentials=differentials,
)

database.jobs.insert(job.model_dump())