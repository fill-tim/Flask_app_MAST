from dataclasses import dataclass


@dataclass
class DataCreate:
    text: str 
    date: str
    time: str
    click_count: int
