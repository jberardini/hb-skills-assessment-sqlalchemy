"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

eight = db.session.query(Brand).get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
chevrolet_corvette = db.session.query(Model).filter(Model.name=='Corvette', Model.brand_name=='Chevrolet').all()

# Get all models that are older than 1960.
old_models = db.session.query(Model).filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

new_brands = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = db.session.query(Model).filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

brands = db.session.query(Brand).filter(Brand.founded==1903, Brand.discontinued==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

old_or_discontinued = db.session.query(Brand).filter(or_(Brand.discontinued!=None, Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.

not_chevy=db.session.query(Model).filter(Model.brand_name!='Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = db.session.query(Model).filter(Model.year==year).all()

    for model in models:
        print model.name
        print model.brand_name
        if model.brand:
            print model.brand.headquarters
        print 


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     brands = db.session.query(Brand).all()

     for brand in brands:
        print brand.name
        for model in brand.models:
            print model.name
        print

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
# The returned value is : <flask_sqlalchemy.BaseQuery object at 0x7fbaab2fbbd0>.
# This value is a base query object.
# To return a brand object, we would need to add .one(), .all(), etc. to this query object.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
# Association tables contain foriegn keys to two or more additional tables in the
# database, and can be used to associate these additional tables to each other
# when their relationship is many to many. However, unlike middle tables,
# association tables don't contain meaningful information that a user might query.
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands = db.session.query(Brand).filter(Brand.name.like('%'+mystr+'%')).all()
    return brands

def get_models_between(start_year, end_year):
    models = db.session.query(Model).filter(Model.year >= start_year, Model.year < end_year).all()
    return models