from pydantic import BaseModel, ConfigDict, EmailStr, Field


class CreateUserShortDto(BaseModel):
    username: str = Field(..., min_length=5, max_length=32)
    chat_id: int


class CreateUserFullDto(CreateUserShortDto):
    email: EmailStr
    name: str = Field(..., min_length=1, max_length=64)
    surname: str = Field(..., min_length=1, max_length=64)
    phone: str = Field(pattern=r"^[0-9]+$", max_length=12)

    model_config = ConfigDict(regex_engine="python-re")


class CreateQuestionDto(BaseModel):
    text: str = Field(..., min_length=1, max_length=256)
    owner: int


class QuestionSchema(BaseModel):
    text: str = Field(..., min_length=1, max_length=256)
    answer: str = Field(..., min_length=1, max_length=256)


class InformationSchema(BaseModel):
    faq: dict[int, QuestionSchema]
    info: dict[int, QuestionSchema]


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return f"{self.text}: {self.answer}"
