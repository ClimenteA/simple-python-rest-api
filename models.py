import hashlib
from typing import Optional
from pydantic import root_validator
from sqlmodel import Field, Session, SQLModel, create_engine, select


engine = create_engine("sqlite:///database.db")


def initializeaza_baza_de_date():
    SQLModel.metadata.create_all(engine)


class Utilizator(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    nume: str
    prenume: str
    semnatura_digitala: str

    @root_validator
    def prepare_fields(cls, values: dict):
        values["id"] = None
        values["semnatura_digitala"] = hashlib.sha256(
            values["semnatura_digitala"].encode("utf-8")
        ).hexdigest()
        return values


class Contract(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    contract_sha256: str = Field(unique=True)
    nume_contract: str
    parti_contractate: str
    contract_base64: str

    @root_validator
    def prepare_fields(cls, values: dict):
        values["id"] = None
        values["contract_sha256"] = hashlib.sha256(
            str(values["contract_base64"] + values["parti_contractate"]).encode("utf-8")
        ).hexdigest()
        return values


def adauga_utilizator(utilizator: Utilizator):
    with Session(engine) as session:
        session.add(utilizator)
        session.commit()
    return utilizator


def adauga_contract(contract: Contract):
    with Session(engine) as session:
        session.add(contract)
        session.commit()
    return contract


def valideaza_contract(contract: Contract):
    contract_sha256 = hashlib.sha256(
        str(contract.contract_base64 + contract.parti_contractate).encode("utf-8")
    ).hexdigest()

    with Session(engine) as session:
        statement = select(Contract).where(Contract.contract_sha256 == contract_sha256)
        results = session.exec(statement)

    return bool(results.all())
