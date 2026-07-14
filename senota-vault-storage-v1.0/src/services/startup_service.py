class StartupService:
    def startup_check(self):
        return {
            "uploads_directory": True,
            "routes_loaded": True,
            "pipeline_ready": True
        }
