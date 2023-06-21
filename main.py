import uvicorn
import fastapi
import models


app = fastapi.FastAPI(title="Contract Semnaturi Digitale API")


@app.post("/adauga-utilizator")
def post_adauga_utilizator(utilizator: models.Utilizator):
    models.adauga_utilizator(utilizator)
    return {"message": "Utilizator adaugat"}


@app.post("/adauga-contract")
def post_adauga_contract(contract: models.Contract):
    models.adauga_contract(contract)
    return {"message": "Contract adaugat"}


@app.post("/valideaza-contract")
def post_valideaza_contract(contract: models.Contract):
    contract = models.valideaza_contract(contract)
    return {"message": "Contract valid" if contract else "Contract invalid"}


if __name__ == "__main__":
    models.initializeaza_baza_de_date()
    uvicorn.run(app="main:app", port=3000, reload=True)
