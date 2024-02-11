{
    'name':'Contract Payment Module',
    'version':'1.0',
    'category':'Custom',
    'author':'Eng.Abdulla Bashir',
    'website':'https://3bdalla3adil.github.io',
    'description':'Module to manage contract payments',
    'license':'LGPL-3',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
    ],
    'installable':True,
    'application':True,
}
