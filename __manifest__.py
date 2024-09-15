{
    'name': "To-Do List Module",
    'version': '17.0.0.1.0',
    'depends': ['mail','sale_management','contacts'],
    'author': "Mounir",
    'category': 'To-Do app',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/todo_views.xml',
        'views/menu.xml',

    ],
    # 'assets':{
    #     'web.assets_backend':['']
    # },
    'installable': True,
    'application':True,
}

