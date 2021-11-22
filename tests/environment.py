import pseudodb as pdb


def before_feature(context, feature):

    if 'fixture.setup_db' in feature.tags:
        db = pdb.PseudoDatabase()
        context.db = db
        context.exception = None

        return context

    return context
