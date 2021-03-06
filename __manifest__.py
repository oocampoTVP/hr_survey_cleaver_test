# -*- coding: utf-8 -*-
{
    'name': "RH Formularios. Test de Cleaver",
    'version': '1.0',
    'category': 'Human Resources Survey Cleaver Test.',
    'summary': 'Survey Cleaver Test',
    'description': """
        Creación del Test de Cleaver con su reporte gráfico completo en XLSX
    """,
    'author': "Edgar Ocampo (Python Developer)",
    'website': "http://www.sindominio.mx",
    'depends': ['survey', 'hr_recruitment'],
    'data': [
        'security/hr_recruitment_survey_security.xml',
        'security/ir.model.access.csv',
	    'data/survey_cleaver_test.xml',
        'views/hr_job_views.xml',
        'views/hr_applicant_views.xml',
        'views/res_config_setting_views.xml',
        'views/export_test_xlsx.xml',
    ],
    'demo': [
        'data/hr_job_demo.xml',
    ],
    'test': ['test/recruitment_process.yml'],
    'auto_install': False,
}
