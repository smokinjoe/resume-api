from arrested import Resource, Endpoint, GetObjectMixin, GetListMixin
from flask import jsonify
# from arrested.contrib.kim_arrested import KimEndpoint
# from arrested.contrib.sql_alchemy import DBObjectMixin

from resume_api.models import db, Project, EmploymentExperience, School, TechnicalExperience, User, WeaponOfChoice
# from .mappers import ProjectMapper, EmploymentExperienceMapper, SchoolMapper, TechnicalExperienceMapper, UserMapper, WeaponOfChoiceMapper

resume_resource = Resource('resume', __name__, url_prefix='/resume')

class ResumeIndexEndpoint(Endpoint, GetObjectMixin):
    name = 'object'
    # name = 'list'
    # many = True

    def get_object(self):
        # stmt = {
        #     "projects": jsonify(json_list=[i.serialize for i in Project.query.all()]),
        #     "employmentExperiences": jsonify(json_list=[i.serialize for i in EmploymentExperience.query.all()]),
        #     "schools": jsonify(json_list=[i.serialize for i in School.query.all()]),
        #     "technicalExperiences": jsonify(json_list=[i.serialize for i in TechnicalExperience.query.all()]),
        #     "user": jsonify(json_list=[i.serialize for i in User.query.all()]),
        #     "weaponsOfChoice": jsonify(json_list=[i.serialize for i in WeaponOfChoice.query.all()])
        # }
        # return jsonify(result=stmt)
        # stmt = {
        #     "projects": Project.query.all(),
        #     "employmentExperiences": EmploymentExperience.query.all(),
        #     "schools": School.query.all(),
        #     "technicalExperiences": TechnicalExperience.query.all(),
        #     "user": User.query.all(),
        #     "weaponsOfChoice": WeaponOfChoice.query.all()
        # }
        # return stmt
        stmt = {
            "projects": {
                "id": 1,
                "title": "Lorem ipsum"
            }
        }
        return stmt

resume_resource.add_endpoint(ResumeIndexEndpoint)
