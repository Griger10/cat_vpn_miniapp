from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        {"ru": "ru"},
        [
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=[
                        "src/backend/core/locales/ru/txt.ftl",
                    ],
                    use_isolating=False,
                ),
            ),
        ],
        root_locale="ru",
    )
    return translator_hub
