import json
import os
import logging

logger = logging.getLogger(__name__)

USERS_DB_FILE = "backend_users_db.json"
PROJECTS_DB_FILE = "backend_projects_db.json"

class PersistentDict(dict):
    def __init__(self, filename, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    self.update(json.load(f))
                logger.info(f"Loaded data from {filename}")
            except Exception as e:
                logger.error(f"Error loading {filename}: {e}")

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save()

    def __delitem__(self, key):
        super().__delitem__(key)
        self._save()

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save()

    def _save(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(dict(self), f, indent=2)
            logger.info(f"Saved data to {self.filename}")
        except Exception as e:
            logger.error(f"Error saving {self.filename}: {e}")

users_db = PersistentDict(USERS_DB_FILE)
projects_db = PersistentDict(PROJECTS_DB_FILE)
