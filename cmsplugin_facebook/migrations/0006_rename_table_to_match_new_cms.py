# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from . import rename_tables_new_to_old, rename_tables_old_to_new


class Migration(SchemaMigration):
    cms_plugin_table_mapping = (
        # (old_name, new_name),
        ('cmsplugin_facebooklikebox', 'cmsplugin_facebook_facebooklikebox'),
        ('cmsplugin_facebooklikebutton', 'cmsplugin_facebook_facebooklikebutton'),
    )

    def forwards(self, orm):
        rename_tables_old_to_new(db, self.cms_plugin_table_mapping)

    def backwards(self, orm):
        rename_tables_new_to_old(db, self.cms_plugin_table_mapping)
