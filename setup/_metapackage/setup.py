import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-openspp-openspp-grievance-redress-mechanism",
    description="Meta package for openspp-openspp-grievance-redress-mechanism Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-spp_helpdesk>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
