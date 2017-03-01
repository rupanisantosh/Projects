class ParetoRouter(object):
    """
    A router to control all database operations on models in
    the myapp2 application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on myapp2 models to 'my_db_2'
        """
        if model._meta.app_label == 'pareto' and model._meta.db_table == 'abc_multiloc_analysis':
            return 'primary'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'pareto' and model._meta.db_table == 'abc_multiloc_analysis':
            return 'primary'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the 'myapp2' app only appears on the 'other' db
        """
        if db == 'primary':
            return model._meta.app_label == 'pareto'
        elif model._meta.app_label == 'pareto' and model._meta.db_table == 'abc_multiloc_analysis':
            return False
        return None