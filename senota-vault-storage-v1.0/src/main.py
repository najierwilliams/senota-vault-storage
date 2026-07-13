from fastapi import FastAPI
app=FastAPI(title='SENOTA Vault Storage')
@app.get('/')
def root(): return {'service':'senota-vault-storage','version':'1.0.0'}
