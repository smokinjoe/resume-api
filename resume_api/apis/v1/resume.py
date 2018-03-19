from arrested import Resource, Endpoint, GetObjectMixin

from resume_api.models import db, Project, EmploymentExperience, School, TechnicalExperience, WeaponOfChoice

resume_resource = Resource('resume', __name__, url_prefix='/resume')

class ResumeIndexEndpoint(Endpoint, GetObjectMixin):
    name = 'object'

    def get_object(self):
        stmt = {
            'projects': [i.serialize for i in Project.query.all()],
            'employmentExperiences': [i.serialize for i in EmploymentExperience.query.all()],
            'schools': [i.serialize for i in School.query.all()],
            'technicalExperiences': [i.serialize for i in TechnicalExperience.query.all()],
            'weaponsOfChoice': [i.serialize for i in WeaponOfChoice.query.all()]
        }
        return stmt

resume_resource.add_endpoint(ResumeIndexEndpoint)
