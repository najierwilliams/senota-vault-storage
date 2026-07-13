class VaultPolicy:
    DEFAULT_RETENTION_DAYS=30

    @staticmethod
    def archive_enabled(secure_vault: bool)->bool:
        return secure_vault
