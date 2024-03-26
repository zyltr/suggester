import secrets
import string

from .modifier import Modifier


def generate(
        length: int = 16,
        modifiers: Modifier = Modifier.DIGITS | Modifier.LOWERCASE | Modifier.UPPERCASE,
) -> str:
    if length < 0:
        raise ValueError("Length must be nonzero.")

    characters = ""

    if modifiers & Modifier.DIGITS:
        characters += string.digits
    if modifiers & Modifier.LOWERCASE:
        characters += string.ascii_lowercase
    if modifiers & Modifier.PUNCTUATION:
        characters += string.punctuation
    if modifiers & Modifier.UPPERCASE:
        characters += string.ascii_uppercase

    if len(characters) <= 0:
        return ""

    return "".join(secrets.choice(characters) for _ in range(length))
