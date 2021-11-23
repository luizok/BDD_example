import pseudodb as pdb


def before_feature(context, feature):

    if 'fixture.setup_db' in feature.tags:
        db = pdb.PseudoDatabase()
        context.db = db
        context.exception = None

    return context


def after_scenario(context, scenario):

    # TODO: Find a better way to check for exception attr
    if 'exception' in dir(scenario):
        context.exception = None

    return context
