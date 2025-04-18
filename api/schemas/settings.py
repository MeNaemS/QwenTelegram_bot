from dataclasses import dataclass


@dataclass(slots=True)
class Bot:
    name: str
    token: str


@dataclass(slots=True)
class DB:
    username: str
    password: str
    host: str
    port: int
    database: str


@dataclass(slots=True)
class OpenAI:
    api_key: str


@dataclass(slots=True)
class API:
    db: DB
    openai: OpenAI


@dataclass(slots=True)
class JWT:
    secret_key: str
    algorithm: str
    expire: int


@dataclass(slots=True)
class Settings:
    jwt: JWT
    bot: Bot
    api: API
